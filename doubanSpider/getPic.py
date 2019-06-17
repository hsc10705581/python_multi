#!/usr/bin/python3.7
# -*- coding: utf-8 -*-  

import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017')
mydb = myclient["e-book-images"]
mycol = mydb["bookimage"]

myquery = { "_id": 637}

mydoc = mycol.find(myquery)

for x in mydoc:
    with open('test.jpg', 'wb') as f:
       f.write(x["image_file"])