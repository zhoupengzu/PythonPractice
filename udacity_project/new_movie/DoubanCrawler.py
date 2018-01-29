# 获取豆瓣上的最后的电影

import time
import csv
import codecs
from functools import reduce
import requests
import expanddouban
from bs4 import BeautifulSoup

"""
每一部Movie的详细信息
"""
class Movie():
    NAME = "name"
    RATE = "rate"
    LOCATION = "location"
    CATEGORY = "category"
    INFO_LINK = "info_link"
    COVER_LINK = "cover_link"

    def __init__(self, name="", rate="", location="", category="", info_link="", cover_link=""):
        self.__name = name
        self.__rate = rate
        self.__location = location
        self.__category = category
        self.__info_link = info_link
        self.__cover_link = cover_link

    def printInfo(self):
        descri = "姓名:{},分数:{},地区:{},分类:{},链接:{},海报:{}".format(
            self.__name, self.__rate, self.__location, self.__category, self.__info_link, self.__cover_link)
        print(descri)

    def getSingleInfoWithDic(self):
        return {Movie.NAME: self.__name, Movie.RATE: self.__rate, Movie.LOCATION: self.__location, Movie.CATEGORY: self.__category, Movie.INFO_LINK: self.__info_link, Movie.COVER_LINK: self.__cover_link}


class MovieTool(object):
    # 获取豆瓣电影的基础url
    BASE_URL = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"
    HTML_PARSER = "html.parser"
    ALL_CATEGORY = "全部类型"
    ALL_LOCATION = "全部地区"

    def __init__(self, category="", location="", load_more=False):
        self.__category = category
        self.__location = location
        self.__all_html = self.__getHtml(load_more=load_more)
        self.__all_category = {}
        self.__getAllLocationAndCategory()

    def __organizeMovieUrl(self, *args):
        '''
        组织url
        '''
        url = MovieTool.BASE_URL
        if len(args):
            url = url + ',' + ",".join(args)
        return url

    def __getMovieUrl(self):
        '''
        根据地区和类型获取电影的url
        '''
        return self.__organizeMovieUrl(self.__category, self.__location)

    def __getHtml(self, load_more=False):
        '''
        获取html
        '''
        url = self.__getMovieUrl()
        html = expanddouban.getHtml(url, load_more)
        return html

    def __analysisMovieHtml(self):
        '''
        解析拿到的html
        '''
        result = []
        soup = BeautifulSoup(self.__all_html, MovieTool.HTML_PARSER)
        app_div = soup.find(id="app")
        list_wp = app_div.find(class_="list-wp")
        all_link = list_wp.find_all('a', recursive=False)
        for ele in all_link:
            info_link = ele['href']
            cover_link = ele.find('img')['src']
            p = ele.find('p', recursive=False)
            span_list = p.find_all('span')
            title = ""
            rate = ""
            for span in span_list:
                if 'title' in span['class']:
                    title = span.string
                elif 'rate' in span['class']:
                    rate = span.string
            result.append(self.__convertToMovie(
                info_link=info_link, cover_link=cover_link, name=title, rate=rate))
        if len(result) == 0:
            result.append(self.__convertToMovie())
        return result

    def __convertToMovie(self, **args):
        movie = Movie(**args, category=self.__category,
                      location=self.__location)
        return movie

    def __getAllLocationAndCategory(self):
        soup = BeautifulSoup(self.__all_html, MovieTool.HTML_PARSER)
        all_category = soup.find_all("ul", attrs={"class": "category"})
        category_dic = {}
        for category in all_category:
            category_span = category.find_all("span")
            category_str = ""
            for index in range(len(category_span)):
                span = category_span[index]
                span_str = span.string
                if not category_str:
                    category_str = span_str
                # 这里要剔除类似于“全部类型”之类的
                if not category_str:
                    category_str = ""
                    continue
                if not span_str:
                    continue
                if index == 0:
                    category_dic[category_str] = []
                else:
                    temp_category_list = category_dic.get(category_str, [])
                    temp_category_list.append(span_str)
                    category_dic[category_str] = temp_category_list
        self.__all_category = category_dic

    def getHtml(self):
        return self.__all_html

    def getLocationAndCategory(self, key_words=""):
        return self.__all_category.get(key_words, self.__all_category)

    def getMovies(self):
        '''
        返回获得的豆瓣的电影信息
        该结果以列表的形式返回，每一项都是一个Movie对象
        '''
        result = self.__analysisMovieHtml()
        return result


# 先获取所有的地区
# print("开始获取全部类型和全部地区：")
movie = MovieTool()
all_category = movie.getLocationAndCategory(MovieTool.ALL_CATEGORY)
all_location = movie.getLocationAndCategory(MovieTool.ALL_LOCATION)
# print(all_location)
# print(all_category)
# print("获取全部类型和全部地区完成")
# 为防止被封，睡眠2秒
# print("==========================")
time.sleep(2)
all_location = ['美国', '香港', '台湾']
all_cycle_count = 3
if len(all_category) < 3:
    all_cycle_count = len(all_category)

# print("开始获取电影信息...")
# 取前面的至多3个类型
all_movies = []
for index in range(all_cycle_count):
    category = all_category[index]
    category_movies_list = []  # 每个分类下的
    for location in all_location:
        # print("正在获取类型：{},地区：{}".format(category, location))
        temp_movie = MovieTool(category = category, location = location, load_more = True)
        location_movies = temp_movie.getMovies()
        location_movies_list = [] # 每个地区下的
        for temp in location_movies:
            location_movies_list.append(temp.getSingleInfoWithDic())
        category_movies_list.append(location_movies_list)
        time.sleep(2)
    all_movies.append(category_movies_list)

# print("获取电影信息完成")
# print("开始构造电影信息数据表...")
with open("movies.csv", 'w', encoding='gb18030') as f:
    # f.write(codecs.BOM_UTF8)
    csv_writer = csv.writer(f)
    
    for movie_info in all_movies:
        for category_movie in movie_info:
            for location_movie in category_movie:
                if location_movie.get(Movie.NAME, '') or location_movie.get(Movie.RATE, '') or location_movie.get(Movie.INFO_LINK, '') or location_movie.get(Movie.COVER_LINK, ''):
                    info_arr = [location_movie.get(
                        Movie.NAME, ""), location_movie.get(Movie.RATE, ""), location_movie.get(Movie.LOCATION, ""), location_movie.get(Movie.CATEGORY, ""), location_movie.get(Movie.INFO_LINK, ""), location_movie.get(Movie.COVER_LINK, "")]
                    csv_writer.writerow(info_arr)

# print("构造完成")
# print("开始统计电影数据...")
result = ""
for category_movies in all_movies:
    category_movies.sort(key=lambda item: len(item), reverse=True)
    # 获取该类别的电影总数
    category_movies_count = reduce(lambda sum, item: sum + len(item), category_movies, 0)
    # 获取数量排名前三，不止三个
    most_three_list = []
    max_count = len(category_movies[0])
    count = 0 # 用来表示找到了第几个最大的数
    for index in range(len(category_movies)):
        location_movies = category_movies[index]
        if len(location_movies) < max_count:
            max_count = len(location_movies)
            count += 1
        if count > 2:
            break
        else:
            most_three_list.append(location_movies)
    for location_movies in most_three_list:
        if len(location_movies) == 0:
            continue
        locationDic = location_movies[0]
        if locationDic.get(Movie.NAME, '') or locationDic.get(Movie.RATE, '') or locationDic.get(Movie.INFO_LINK, '') or locationDic.get(Movie.COVER_LINK, ''):
            location = locationDic.get(Movie.LOCATION, "")
            result = result + "地区：{}, 百分比:{:.2f}\n".format(
            location, len(location_movies) / category_movies_count * 100)
        else:
            result = result + "地区：{}, 百分比:{:.2f}\n".format(
                location, 0)
        
        
with open("output.txt", 'w') as f:
     f.write(result)
            
# print("统计完成")

