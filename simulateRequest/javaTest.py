#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import requests
import threading
import time

def make_request_thread(url, id):
    response = requests.get(url)
    #print("finished thread " + str(id))
    print(response.text)

url = "http://localhost:8080/get-greeting/hsc"

class myThread (threading.Thread):
    def __init__(self, threadID, url):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.url = url
    def run(self):
        make_request_thread(self.url, self.threadID)

for i in range(100):
    thread = myThread(i, url)
    thread.start()
    time.sleep(0.1)


print("退出主线程")