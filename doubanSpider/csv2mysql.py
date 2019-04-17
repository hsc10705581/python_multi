#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

import xlrd
import pymysql

mydb = pymysql.connect("localhost", "root", "root", "e-book")
mycursor = mydb.cursor()

data = xlrd.open_workbook("web.xlsx")
table = data.sheets()[0]

sql = "insert into `book` (`title`, `author`, `translator`, `grade`, `press`, `date`, `numOfPeople`, `price`, `introduction`,`isbn`, `b_ID`, `stock`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
id = 0
for i in range(table.nrows):
    print(table.row_values(i))
    if table.row_values(i)[0] == "互联网":
        info = table.row_values(i)
        id = id + 1
        val = (info[1], info[2], info[3], str(info[4]), info[5], info[6], info[7], info[8], info[9], info[10], id, "0")
        mycursor.execute(sql, val)
        mydb.commit()