# json

import json

origin_json_str = '{"name":"zhoupengzu","age":20}'

to_obj = json.loads(origin_json_str)
print(to_obj)

origin_obj = {
    "name":"zhoupengzu",
    "age": 20
}

to_json = json.dumps(origin_obj)
print(to_json)
print(type(to_json))  # <class 'str'>
