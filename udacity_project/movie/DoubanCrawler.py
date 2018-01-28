# 获取豆瓣上的最后的电影

from MovieTool import MovieTool
from Movie import Movie
import time
import csv
import codecs
from functools import reduce

# 先获取所有的地区
print("开始获取全部类型和全部地区：")
movie = MovieTool()
all_category = movie.getLocationAndCategory(MovieTool.ALL_CATEGORY)
all_location = movie.getLocationAndCategory(MovieTool.ALL_LOCATION)
print(all_location)
print(all_category)
print("获取全部类型和全部地区完成")
# 为防止被封，睡眠2秒
print("==========================")
time.sleep(2)
# all_location = ['美国', '香港', '台湾']
all_cycle_count = 3
if len(all_category) < 3:
    all_cycle_count = len(all_category)

print("开始获取电影信息...")
# 取前面的至多3个类型
all_movies = []
for index in range(all_cycle_count):
    category = all_category[index]
    category_movies_list = []  # 每个分类下的
    for location in all_location:
        print("正在获取类型：{},地区：{}".format(category, location))
        temp_movie = MovieTool(category = category, location = location, load_more = True)
        location_movies = temp_movie.getMovies()
        location_movies_list = [] # 每个地区下的
        for temp in location_movies:
            location_movies_list.append(temp.getSingleInfoWithDic())
        category_movies_list.append(location_movies_list)
        time.sleep(2)
    all_movies.append(category_movies_list)

print("获取电影信息完成")
print("开始构造电影信息数据表...")
with open("movies.csv", 'w', encoding='gb18030') as f:
    # f.write(codecs.BOM_UTF8)
    csv_writer = csv.writer(f)
    
    for movie_info in all_movies:
        for category_movie in movie_info:
            for location_movie in category_movie:
                info_arr = [location_movie.get(
                    Movie.NAME, ""), location_movie.get(Movie.RATE, ""), location_movie.get(Movie.LOCATION, ""), location_movie.get(Movie.CATEGORY, ""), location_movie.get(Movie.INFO_LINK, ""), location_movie.get(Movie.COVER_LINK, "")]
                csv_writer.writerow(info_arr)

print("构造完成")
print("开始统计电影数据...")
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
            
print("统计完成")

