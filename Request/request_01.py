# coding=utf-8

import json
import urllib2


def as_complex(dct):
    return complex(dct["哈哈"])

# product_id = "59f2ddc9ca87a80cba000103"
# api_token = "c52ef25440bb7794cc4829e7aecbcd6b"
# version_url = "http://api.fir.im/apps/latest/"
# version_request_url = version_url + product_id + "?api_token=" + api_token
# # print version_request_url
# req = urllib2.Request(version_request_url)
# # print req
# resp = urllib2.urlopen(req)
# resp_data = resp.read()
# # print resp_data
# dic = json.loads(resp_data)
# # print dic['versionShort']


dic = json.dumps({'哈哈': "haha"})
obj_dic = json.loads(dic, encoding="utf-8")
print obj_dic;