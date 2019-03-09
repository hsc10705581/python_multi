#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from get_fshare import FSAPI

finished = open("api_urls.txt").readlines()
bot = FSAPI('utvyoxrk@emlpro.com', 'ahihihi')
bot.login()

res = bot.get_file_info(finished[0])
print(res)