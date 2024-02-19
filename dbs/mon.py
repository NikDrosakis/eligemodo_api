#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
mongo = client.gaia

def ins(col,json):
	col = mongo[col]
	result = col.insert_one(json)
	return format(result.inserted_id)
    
def f(col,json)
    return mycol.find(json)    