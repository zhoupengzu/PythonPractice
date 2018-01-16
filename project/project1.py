# 爬虫

from urllib import request
# from http import client
import ssl
import re

class Spider():
    SPIDER_URL = 'https://www.panda.tv/cate?channel=web_pgc-tjw-ch_sydbdh'
    BASE_URL = 'https://www.panda.tv'
    REG_ITEM_PATTERN = '<a class="video-list-item-wrap" href=[\s\S]*?</a>'
    REG_HREF_TITLE_PATTERN = '<a class="video-list-item-wrap" href="([\s\S]*?)"[ ]{1,}[\s\S]*?>[\s\S]*?<div class="cate-title"[ ]?[\s\S]*?>([\s\S]*?)</div>[\s\S]*?</a>'
    REG_HTTPS = '^(https)'
    def go(self):
        self.__request_for_data()
    
    def __find_item(self, origin_str):
        regular_find = re.findall(Spider.REG_ITEM_PATTERN, origin_str)
        return regular_find

    def __find_href_title(self, origin_list):
        href_title_arr = []
        for item in origin_list:
            href_title = re.findall(Spider.REG_HREF_TITLE_PATTERN, item)
            href_title_group = href_title[0]
            href = href_title_group[0].strip()
            if not re.findall(Spider.REG_HTTPS, href):
                href = Spider.BASE_URL + href
            href_title_dic = {
                'href': href, 'title': href_title_group[1].strip()}
            href_title_arr.append(href_title_dic)
        return href_title_arr


    def __request_for_data(self):
        context = ssl._create_unverified_context()
        re_request = request.urlopen(Spider.SPIDER_URL, context=context)
        if re_request and re_request.getcode() == 200:
            origin_data = re_request.read()
            origin_data_str = str(origin_data, 'utf-8')
            transfer_obj = self.__find_item(origin_data_str)
            result = self.__find_href_title(transfer_obj)
            print(result)
        else:
            print('request failed')


spider = Spider()
spider.go()

