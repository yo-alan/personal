# coding=utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from v.ui_error import Ui_Error

class Error(QMessageBox):
	
	def __init__(self, principal):
		QMessageBox.__init__(self, principal)
		self.ui = Ui_Error()
		self.ui.setupUi(self)
		
		self.setButtonText(QMessageBox.Ok, "Aceptar")
		
		self.setIcon(QMessageBox.Critical)
	
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def mostrar(self, ):
		
		self.show()
		
		self.center()
	
	def closeEvent(self, event):
		pass
	
