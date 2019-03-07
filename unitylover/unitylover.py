#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_extension("tampermonkey_v4.8.crx")
browser = webdriver.Chrome(chrome_options=options)

def get_short_urls():
    short_urls = []
    for page in range(1, 93):
        print(page)
        response = requests.get("http://www.unityfreaks.com/downloadlist.php?page=" + str(page))
        soup = BeautifulSoup(response.text, "html.parser")
        tabs = soup.find_all(class_="btn btn-default")
        for tab in tabs:
            try:
                if tab.attrs["href"][0:13] == "http://gestyy":
                    short_urls.append(tab.attrs["href"])
            except KeyError:
                pass
        print("page " + str(page) + " finished.")
    return short_urls

short_urls = get_short_urls()
f = open("short_urls.txt", "w")
for url in short_urls:
    print(url, file=f)
f.close()

#browser.get("http://www.unityfreaks.com/downloadlist.php")

#soup = BeautifulSoup(browser.page_source, "html.parser")