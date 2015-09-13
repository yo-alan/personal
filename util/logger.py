# coding=utf-8
import sys

def log(s):
	
	if sys.stdin.isatty():
		print s
