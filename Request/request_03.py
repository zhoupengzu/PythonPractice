# coding=utf-8

import json
import urllib2,urllib

base_url = "http://api.fir.im/apps"
type = "ios"
bundle_id = "com.nonobank.MaiYabd"
api_token = "c52ef25440bb7794cc4829e7aecbcd6b"
file_path = "/Users/zhoupengzu/Desktop/MaiYafq_BD_ipa/MaiYafq_BD.ipa"
product_name = "麦芽分期BD"
product_version = "1.5.4"
product_build = "549"
release_type = "Inhouse"
change_log = "测试"

# 获取上传凭证
cer_base_data = {"type": type, "bundle_id": bundle_id, "api_token": api_token}
cer_url_data = urllib.urlencode(cer_base_data)
req_cer = urllib2.Request(base_url)
req_cer_open = urllib2.urlopen(req_cer, cer_url_data)
cer_resp_data = req_cer_open.read()
cer_resp_dic = json.loads(cer_resp_data)
cer_cert = cer_resp_dic.get("cert")
cer_binary = cer_cert.get("binary")
cer_key = cer_binary.get("key")
cer_token = cer_binary.get("token")
cer_upload_url = cer_binary.get("upload_url")

# 上传文件
upload_url = base_url + "/upload_url"
# with open(file_path, "rb") as file_ipa:
#     upload_file_data = file_ipa.read()
upload_file_data = open(file_path, 'rb')
upload_base_data = {"key": cer_key,
                    "token": cer_token,
                    "file": upload_file_data,
                    "x:name": product_name,
                    "x:version": product_version,
                    "x:build": product_build,
                    "x:release_type": release_type,
                    "x:changelog": change_log
                    }
upload_url_data = urllib.urlencode(upload_base_data)
upload_req = urllib2.Request(upload_url)
upload_req_open = urllib2.urlopen(upload_req, upload_url_data)
upload_resp_data = upload_req_open.read()

print upload_resp_data
