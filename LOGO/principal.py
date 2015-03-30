# coding=utf-8

import datetime, sys, os, time

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_logo import Ui_Logo

class Logo(QMainWindow):
	
	def __init__(self, ):
		QMainWindow.__init__(self, None)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.ui = Ui_Logo()
		self.ui.setupUi(self)
		self.setStyleSheet("background-image: url(./LOGO/personal.png); background-repeat: no-repeat;")
		
		self.center()
		
		self.cerrar()
	
	def mostrar(self, ):
		self.show()
	
	def cerrar(self, ):
		time.sleep(10)
		self.close()
	
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	

#~ def main():
	#~ 
	#~ app = QApplication(sys.argv)
	#~ l = Logo()
	#~ 
	#~ return app.exec_()
#~ 
#~ if __name__ == '__main__':
	#~ exit(main())
