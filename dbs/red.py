#!/usr/bin/env python
# -*- coding: utf-8 -*-
from redis import StrictRedis

redis=StrictRedis(host='localhost',port=6379,db=1,password='n130177!',decode_responses=True)
#from sys import argv

def get(key):
	global redis	
	return redis.get(key)
	
def set(key,value):
	global redis
	return redis.set(key,value)