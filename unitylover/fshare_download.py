#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from get_fshare import FSAPI
import unittest

finished = open("api_urls.txt").readlines()
bot = FSAPI('utvyoxrk@emlpro.com', 'ahihihi')
bot.login()
#res = bot.download("https://www.fshare.vn/file/ATXZV4QZKLZX")
save = open("download_links.txt", "w")
a = 0

for url in finished:
    a = a + 1
    print(bot.download(url), file=save)
    print(a)
save.close()