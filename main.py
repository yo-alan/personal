#! /usr/bin/python
# coding=utf-8

import sys, os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from c.principal import Principal

def inicio():
	
	try:
		f = open("config/personal.pid", "r")
		
		f.close()
		
		exit(1)
	except Exception as ex:
		f = open("config/personal.pid", "w")
		
		f.write(str(os.getpid()) + "\n")
		
		f.close()
	
def fin():
	
	try:
		os.remove("config/personal.pid")
	except Exception as ex:
		print "Ocurrió un error:", ex

def main():
	
	try:
		app = QApplication(sys.argv)
		p = Principal()
		p.mostrar()
	except Exception as ex:
		print ex
		fin()
		exit(1)
	
	return app.exec_()

if __name__ == '__main__':
	
	inicio()
	
	r = main()
	
	fin()
	
	exit(r)
