#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

import requests
from bs4 import BeautifulSoup
import time
import random
import csv

html = requests.get("https://book.douban.com/tag/%E4%BA%92%E8%81%94%E7%BD%91")
soup = BeautifulSoup(html.text, 'lxml')
pics = soup.select("#subject_list  ul  li div.pic  a  img")
for pic in pics:
    response = requests.get(pic["src"], stream=True)
    with open('test.jpg', 'wb') as f:
        f.write(response.content)
    #print(response.content)
