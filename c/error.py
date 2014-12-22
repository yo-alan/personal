#! /usr/bin/python
# coding=utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from v.ui_error import Ui_Error

class Error(QDialog):
	
	def __init__(self, principal):
		QDialog.__init__(self, principal)
		self.ui = Ui_Error()
		self.ui.setupUi(self)
		
		#CODIGO PARA HACER
	
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def mostrar(self, ):
		
		self.center()
		
		self.show()
	
	def closeEvent(self, event):
		pass
	
	def reject(self, ):
		self.done(QDialog.Rejected)
	
	def accept(self, ):
		self.done(QDialog.Accepted)
	
