#! /usr/bin/python
# coding=utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from v.ui_eliminar import Ui_Eliminar
from m.empleado import Empleado

class Eliminar(QDialog):
	
	def __init__(self, principal):
		QDialog.__init__(self, principal)
		self.ui = Ui_Eliminar()
		self.ui.setupUi(self)
		
		#CODIGO PARA HACER
	
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def mostrar(self, principal):
		
		self.center()
		
		empleado = str(principal.ui.lblEmpleado.text().toUtf8())
		
		documento = empleado.split('(')[1]
		
		documento = int(documento[:-1])
		
		for e in principal.empleados:
			if e.documento == documento:
				self.e = e
				break
		
		self.show()
	
	def closeEvent(self, event):
		pass
	
	def reject(self, ):
		
		
		
		print "Cancelado"
		self.done(QDialog.Rejected)
		
	def accept(self, ):
		
		self.e.eliminar()
		
		print "Aceptado"
		self.done(QDialog.Accepted)
	
