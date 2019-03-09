#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

finished = open("pan_urls.txt").readlines()
save = open("api_urls.txt", "w")

for url in finished:
    if(url[0:21] != "https://www.fshare.vn"):
        continue
    print(url[0:39], file=save)
save.close()