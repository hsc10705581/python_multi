#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

import pymysql
import time

mydb = pymysql.connect("106.14.207.184", "zpapp", "zpapp", "zpapp")
mycursor = mydb.cursor()

sql_old = "call follow_company_job(%s)"

start = time.time()
for i in range(100):
    mycursor.execute(sql_old, 1)
end = time.time()
old = end - start

sql_new = "call follow_company_job_o(%s)"
start_i = time.time()
for i in range(100):
    mycursor.execute(sql_new, 1)
end_i = time.time()
new = end_i - start_i

print("old version use: " + str(old) + ". new version use: " + str(new))