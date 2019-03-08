#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from get_fshare import FSAPI
import unittest

finished = open("finished.txt").readlines()
bot = FSAPI('utvyoxrk@emlpro.com', 'ahihihi')
bot.login()
print(finished[0])
res = bot.get_file_info(finished[0])
print(res)

for url in finished:
    pass