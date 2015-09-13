#! /usr/bin/python
# coding=utf-8
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from c.principal import Principal
from util.sistema import *

def main():
	
	try:
		app = QApplication(sys.argv)
		p = Principal()
		p.mostrar()
	except Exception as ex:
		print ex
		erase_pid_file()
		return 1
	
	return app.exec_()

if __name__ == '__main__':
	
	create_pid_file()
	
	r = main()
	
	erase_pid_file()
	
	exit(r)
