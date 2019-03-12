#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from get_fshare import FSAPI

finished = open("api_urls.txt").readlines()
bot = FSAPI('utvyoxrk@emlpro.com', 'ahihihi')
bot.login()

res = bot.download("https://www.fshare.vn/file/QVXSVPNV74LG")
print(res)