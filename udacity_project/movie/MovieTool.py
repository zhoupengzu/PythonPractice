
"""
获取电影的工具类
"""
import requests
import expanddouban
from bs4 import BeautifulSoup
from Movie import Movie

class MovieTool(object):
    # 获取豆瓣电影的基础url
    BASE_URL = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"
    HTML_PARSER = "html.parser"
    ALL_CATEGORY = "全部类型"
    ALL_LOCATION = "全部地区"

    def __init__(self, category = "", location = "", load_more = False):
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
        app_div = soup.find(id = "app")
        list_wp = app_div.find(class_ = "list-wp")
        all_link = list_wp.find_all('a', recursive = False)
        for ele in all_link:
            info_link = ele['href']
            cover_link = ele.find('img')['src']
            p = ele.find('p', recursive = False)
            span_list = p.find_all('span')
            title = ""
            rate = ""
            for span in span_list:
                if 'title' in span['class']:
                    title = span.string
                elif 'rate' in span['class']:
                    rate = span.string
            result.append(self.__convertToMovie(info_link = info_link, cover_link = cover_link, name = title, rate = rate))    
        return result

    def __convertToMovie(self, **args):
        movie = Movie(**args, category= self.__category, location=self.__location)
        return movie

    def __getAllLocationAndCategory(self):
        soup = BeautifulSoup(self.__all_html, MovieTool.HTML_PARSER)
        all_category = soup.find_all("ul",attrs={"class":"category"})
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
    
    def getLocationAndCategory(self, key_words = ""):
        return self.__all_category.get(key_words, self.__all_category)

    def getMovies(self):
        '''
        返回获得的豆瓣的电影信息
        该结果以列表的形式返回，每一项都是一个Movie对象
        '''
        result = self.__analysisMovieHtml()
        return result



