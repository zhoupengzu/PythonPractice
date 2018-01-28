
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
        descri = "姓名:{},分数:{},地区:{},分类:{},链接:{},海报:{}".format(self.__name,self.__rate,self.__location,self.__category,self.__info_link,self.__cover_link)
        print(descri)
    def getSingleInfoWithDic(self):
        return {Movie.NAME: self.__name, Movie.RATE: self.__rate, Movie.LOCATION: self.__location, Movie.CATEGORY: self.__category, Movie.INFO_LINK: self.__info_link, Movie.COVER_LINK: self.__cover_link}
