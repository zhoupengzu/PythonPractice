# 关键字可变参数
# 使用两个**表示

def printCityInfo(**cityInfo):
    print(cityInfo)
    print(type(cityInfo))  # <class 'dict'>
    for key, value in cityInfo.items():
        print(key, ':', value)
    
printCityInfo(bg='10', tg='20', ng='30')

dic = {'bg' : '10', 'tg' : '20', 'ng' : '30'}
printCityInfo(**dic)
