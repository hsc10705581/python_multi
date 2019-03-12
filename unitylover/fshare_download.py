#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from get_fshare import FSAPI
import unittest

finished = open("api_urls.txt").readlines()
#bot = FSAPI('utvyoxrk@emlpro.com', 'ahihihi')
bot = FSAPI('934936408@qq.com', '19990421hsc')
bot.login()
#res = bot.download("https://www.fshare.vn/file/ATXZV4QZKLZX")
#save = open("download_links.txt", "w")
#name = open("name_list.txt", "w")
links = open("201-600.txt", "w")
a = 0

for url in finished:
    a = a + 1
    if a <= 200 or a > 600:
        continue
    #print(bot.download(url), file=save)
    #print(bot.get_file_info(url)["name"], file=name)
    print(bot.download(url), file=links)
    print(a)

links.close()