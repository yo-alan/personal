#! /usr/bin/python
# coding=utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from v.ui_eliminar import Ui_Eliminar
from m.empleado import Empleado

class Eliminar(QDialog):
	
	principal = None
	
	def __init__(self, principal):
		QDialog.__init__(self, principal)
		self.ui = Ui_Eliminar()
		self.ui.setupUi(self)
		
		self.principal = principal
		
	
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
		self.done(QDialog.Rejected)
		
	def accept(self, ):
		
		try:
			self.e.eliminar()
			
			self.principal.ui.lblEmpleado.setText("Apellido, Nombre (documento)")
			self.principal.ui.txtEObservaciones.setText("")
			self.principal.ui.txtEObservaciones.setEnabled(False)
			self.principal.ui.pbEditar.setEnabled(False)
			self.principal.ui.pbEliminar.setEnabled(False)
			self.principal.ui.pbLicAgregar.setEnabled(False)
			self.principal.ui.pbLicEditar.setEnabled(False)
			self.principal.ui.pbLicEliminar.setEnabled(False)
			self.principal.ui.aAgregarLicencia.setEnabled(False)
			self.principal.ui.aEditarLicencia.setEnabled(False)
			self.principal.ui.aEliminarLicencia.setEnabled(False)
			
			for i in range(0, 5):
				self.principal.ui.twDatosLaborales.setItem(i, 1, QTableWidgetItem())
			
			for i in range(0, 7):
				self.principal.ui.twDatosPersonales.setItem(i, 1, QTableWidgetItem())
			
			self.done(QDialog.Accepted)
			
		except Exception as ex:
			self.error.setText("Ha ocurrido un mientras intentaba eliminar un empleado.".decode('utf-8'))
			self.error.setDetailedText(str(ex).decode('utf-8'))
			self.error.mostrar()
