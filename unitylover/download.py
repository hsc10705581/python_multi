#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

from urllib import request

urls = open("download_links.txt").readlines()
a = 0

for url in urls:
    a = a + 1
    request.urlretrieve(url)
    print(a)