# coding=utf-8
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from v.ui_acerca_de import Ui_Acerca_de

class Acerca_de(QDialog):
	
	def __init__(self, principal):
		QDialog.__init__(self, principal)
		self.ui = Ui_Acerca_de()
		self.ui.setupUi(self)
		
		self.ui.buttonBox.button(QDialogButtonBox.Ok).setText("Aceptar")
	
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def mostrar(self):
		
		self.show()
		
		self.center()
	
	def closeEvent(self, event):
		pass
	
	def reject(self, ):
		self.done(QDialog.Rejected)
		
	def accept(self, ):
		self.done(QDialog.Accepted)
