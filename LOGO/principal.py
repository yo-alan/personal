# coding=utf-8

import datetime, sys, os, time

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_logo import Ui_Logo

class Principal(QMainWindow):
	
	def __init__(self, ):
		QMainWindow.__init__(self, None)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.ui = Ui_Logo()
		self.ui.setupUi(self)
		
		self.mostrar()
	
	def mostrar(self, ):
		self.show()
	

def main():
	
	app = QApplication(sys.argv)
	p = Principal()
	
	return app.exec_()

if __name__ == '__main__':
	exit(main())
