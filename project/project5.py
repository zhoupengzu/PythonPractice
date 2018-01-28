# 创建一个请求

import requests
from bs4 import BeautifulSoup

class Html():
    features = "html.parser"
    def __init__(self):
        self.__html_text = ""

    def __request(self,url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def __get_soup(self):
        soup = BeautifulSoup(self.__html_text, Html.features)
        return soup

    def begin_to_request(self,url):
        response_text = self.__request(url)
        if response_text:
            self.__html_text = response_text
        
    def get_html_title(self):
        soup = BeautifulSoup(self.__html_text, Html.features)
        print(soup.title)
        print(soup.title.name)
    def get_div_tag(self):
        soup = self.__get_soup()    
        print(soup.find(
            id='mw-content-text').find(class_="mw-parser-output").p.a.get('href'))

html = Html()
html.begin_to_request("https://en.wikipedia.org/wiki/Dead_Parrot_sketch")
# html.get_html_title()
html.get_div_tag()

