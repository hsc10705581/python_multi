#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_extension("tampermonkey_v4.8.crx")
browser = webdriver.Chrome(chrome_options=options)
time.sleep(30)

fshare = []
for url in open("short_urls.txt"):
    browser.get(url)
    time.sleep(5)
    print(browser.current_url)
    fshare.append(browser.current_url)

f = open("short_urls.txt", "w")
for url in fshare:
    print(url, file=f)
f.close()