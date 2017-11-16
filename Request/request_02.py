# coding=utf-8

"""
如果一个字符串已经是unicode了，再进行解码将出错，所以在解码前，需要用isinstance来检测其是否是unicode编码
解码：将str变成unicode
编码：将unicode变成str
"""

import json


json_dic = {"a": 1, "b": 2, "3": "c", "哈哈": "hello"}
# print json_dic["哈哈"]
encode_json = json.dumps(json_dic)
print encode_json
# if isinstance(encode_json, unicode):
#     print "is unicode"
unicode_change = encode_json.decode(encoding='UTF-8')
# if isinstance(unicode_change, unicode):
#     print "is unicode"
# print unicode_change
decode_json = json.loads(unicode_change)
# for key in decode_json.iterkeys():
#     print key
key = u"哈哈".encode("UTF-8")
print decode_json.get(key)
