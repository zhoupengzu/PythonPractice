# 获取豆瓣上的最后的电影

from MovieTool import MovieTool
from Movie import Movie

result = MovieTool.getMovies(load_more=True, location="美国")
# print(len(result))
for movie in result:
    movie.printInfo()

