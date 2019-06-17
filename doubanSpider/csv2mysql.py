#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

import xlrd
import pymysql
import random


mydb = pymysql.connect("localhost", "root", "root", "e-book")
mycursor = mydb.cursor()

data = xlrd.open_workbook("web.xlsx")
table = data.sheets()[0]

sql = "insert into `book` (`title`, `author`, `translator`, `grade`, `press`, `date`, `num_of_people`, `price`, `introduction`,`isbn`, `b_id`, `stock`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
id = 0
for i in range(table.nrows):
    try:
        print(table.row_values(i))
        if table.row_values(i)[1] == "互联网":
            info = table.row_values(i)
            id = id + 1
            val = (info[2], info[3], info[4], str(info[5]), info[6], info[7], info[8], info[9], info[10], info[11], info[0], random.randint(0, 100))
            mycursor.execute(sql, val)
            mydb.commit()
    except UnicodeEncodeError:
        continue
    except pymysql.err.DataError:
        continue