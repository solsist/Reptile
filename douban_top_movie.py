# coding='utf-8'

import requests
from lxml import etree
import json

url = 'https://movie.douban.com/top250'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
response = requests.get(url, headers=headers).text

html = etree.HTML(response)
Node = html.xpath("//div[@class='info']")
with open('movie.json', 'w', encoding='utf-8') as f:
    for node in Node:
        movie_dict = {}
        movie_dict['电影名称'] = ''.join(node.xpath(".//a/span[1]/text()"))
        movie_dict['评分'] = ''.join(node.xpath(".//div[@class='star']/span[2]/text()"))
        movie_dict['评价'] = ''.join(node.xpath(".//p[@class='quote']/span/text()"))
        f.write(json.dumps(movie_dict, ensure_ascii=False) + '，\n')


