
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

    def __init__(self, category = "", location = ""):
        self.__category = category
        self.__location = location

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

    def __analysisHtml(self, html=""):
        '''
        解析拿到的html
        '''
        result = []
        soup = BeautifulSoup(html, MovieTool.HTML_PARSER)
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

    @classmethod
    def getMovies(cls, category="", location="", load_more = False):
        '''
        返回获得的豆瓣的电影信息
        该结果以列表的形式返回，每一项都是一个Movie对象
        '''
        tool = MovieTool(category, location)
        all_html = tool.__getHtml(load_more=load_more)
        result = tool.__analysisHtml(all_html)
        for movie in result:
            movie.printInfo()
        return result



