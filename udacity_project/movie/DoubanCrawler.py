# 获取豆瓣上的最后的电影

import requests
import expanddouban

class BestMovie():
    # 获取豆瓣电影的基础url
    BASE_URL = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"

    def __organizeMovieUrl(self, *args):
        '''
        组织url
        '''
        url = BestMovie.BASE_URL
        if len(args):
            url = url + ',' + ",".join(args)
        return url

    def getMovieUrl(self, category = "", location = ""):
        '''
        根据地区和类型获取电影的url
        '''
        return self.__organizeMovieUrl(category, location)

    def getHtml(self, url):
        '''
        获取html
        '''
        html = expanddouban.getHtml(url, False)
        print(html)

best_movie = BestMovie()
movie_url = best_movie.getMovieUrl("大陆", "动作")
best_movie.getHtml(movie_url)
