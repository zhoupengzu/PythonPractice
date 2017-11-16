# coding=utf-8

import urllib2

base_url = "http://localhost:8080/python_request/HelloPython.php"
req = urllib2.Request(base_url)
req_open = urllib2.urlopen(req)
data = req_open.read()
print data
