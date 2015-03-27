# coding=utf-8

import os

def create_pid_file():
	
	try:
		f = open("config/personal.pid", "r")
		
		f.close()
		
		exit(1)
	except Exception as ex:
		f = open("config/personal.pid", "w")
		
		f.write(str(os.getpid()) + "\n")
		
		f.close()

def erase_pid_file():
	
	try:
		os.remove("config/personal.pid")
	except Exception as ex:
		print "Ocurrió un error:", ex
