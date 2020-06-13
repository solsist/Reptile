# coding:utf-8

import requests

url = 'https://tieba.baidu.com/f'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}
keyword = input('请输入需要查询的贴吧:')
pn = int(input('请输入需要保存的页数:'))

for i in range(pn):
    params = {
        'kw': keyword,
        'pn': i * 50
    }

    response = requests.get(url, headers=headers, params=params)

    with open('{}{}.html'.format(keyword, i+1), 'wb') as f:
        f.write(response.content)
