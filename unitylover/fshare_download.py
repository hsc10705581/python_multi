#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from get_fshare import FSAPI
import unittest

finished = open("finished.txt").readlines()
bot = FSAPI('utvyoxrk@emlpro.com', 'ahihihi')
bot.login()
res = bot.download("https://www.fshare.vn/file/ATXZV4QZKLZX")
print(res)

for url in finished:
    pass