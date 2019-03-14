#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

from get_fshare import FSAPI

def get_range_urls(begin, end, user_name, password):
    bot = FSAPI(user_name, password)
    bot.login()
    finished = open("api_urls.txt").readlines()
    links = open((str(begin) + "-" + str(end) + ".txt"), "w")
    count = 0
    for url in finished:
        count = count + 1
        if count < begin or count > end:
            continue
        print(bot.download(url), file=links)
        print(count)

get_range_urls(1201, 2000, "934936408@qq.com", "19990421hsc")