#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

base_url = "http://pu.guitarworld.com.cn/gtqupu.php?mod=list&ct=hot&tm=wk&page="

urls = []
name = []

fp = open("result.txt", 'w')
for i in range(131):
    print(1+i)
    url = base_url + str(i+1)
    html = requests.get(url, headers=headers)
    html.encoding = "utf-8"
    soup = BeautifulSoup(html.text, "lxml")
    results = soup.find_all("a", {"target": "_blank"})
    for result in results:
        if result["href"][0:4] == "http":
            info = "曲谱名: " + result.text + " 链接: " + result["href"] + "\n"
            try:
                fp.write(info)
            except UnicodeEncodeError:
                continue

fp.close()
