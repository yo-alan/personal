#! /usr/bin/python
# coding=utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from v.ui_lic_buscar import Ui_Lic_Buscar

class Lic_Buscar(QDialog):
	
	def __init__(self, principal):
		QDialog.__init__(self, principal)
		self.ui = Ui_Lic_Buscar()
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
		
		
		
		print "Estoy cerrando la ventana"
	
	def reject(self, ):
		
		
		
		print "Cancelado"
		self.done(1)
		
	def accept(self, ):
		
		
		
		print "Aceptado"
		self.done(0)
	
