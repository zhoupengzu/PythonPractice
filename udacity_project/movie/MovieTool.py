
"""
获取电影的工具类
"""

import requests
import expanddouban


class MovieTool():
    # 获取豆瓣电影的基础url
    BASE_URL = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"

    def __init__(self):
        self.__name = ""
        self.

    def __organizeMovieUrl(self, *args):
        '''
        组织url
        '''
        url = MovieTool.BASE_URL
        if len(args):
            url = url + ',' + ",".join(args)
        return url

    def __getMovieUrl(self, category="", location=""):
        '''
        根据地区和类型获取电影的url
        '''
        return self.__organizeMovieUrl(category, location)

    def __getHtml(self, url, load_more = False):
        '''
        获取html
        '''
        html = expanddouban.getHtml(url, load_more)
        return getHtml
    @class
    def getMovies(cls,category, location):
        '''
        返回获得的豆瓣的电影信息
        该结果以列表的形式返回，每一项都是一个Movie对象
        '''

        pass
