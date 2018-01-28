
"""
每一部Movie的详细信息
"""
class Movie():
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

        