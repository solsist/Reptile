# coding:utf-8

import requests
import json
from jsonpath import jsonpath
url = 'https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?&for_mobile=1&start=0&count=18'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Referer': 'https://m.douban.com/tv/american',
}
content = requests.get(url, headers=headers).content.decode()
dict_data = json.loads(content)
count = jsonpath(dict_data, '$.count')[0]
name = jsonpath(dict_data, '$..title')
value = jsonpath(dict_data, '$..value')
for i in range(count):
    print(i + 1, name[i], value[i])
