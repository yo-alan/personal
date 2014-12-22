#! /usr/bin/python
# coding=utf-8

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from c.principal import Principal

def main():
	
	app = QApplication(sys.argv)
	p = Principal()
	p.mostrar()
	
	return app.exec_()

if __name__ == '__main__':
	exit(main())
