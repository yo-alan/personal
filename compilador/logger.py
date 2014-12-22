#! /usr/bin/python
# coding=utf-8

import datetime

def log(s):
	print str(datetime.datetime.now()).split('.')[0] + ": " + str(s)
