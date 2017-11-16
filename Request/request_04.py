# coding=utf-8

import urllib2
import json

base_url = "http://localhost:8080/python_request/HelloPython.php?name=zhoupengzu"
req = urllib2.Request(base_url)
req_open = urllib2.urlopen(req)
data = req_open.read()
dic = data
# if isinstance(data, unicode):
#     print "is instance"
#     dic = data
# else:
#     temp_dic = json.loads(data, encoding="utf-8")
#     if isinstance(temp_dic, dict):
#         print "dict"
#     dic = temp_dic
print dic
