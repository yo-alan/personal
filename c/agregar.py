#! /usr/bin/python
# coding=utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from c.error import Error
from v.ui_agregar import Ui_Agregar
from m.empleado import Empleado

class Agregar(QDialog):
	
	error = None
	
	def __init__(self, principal):
		QDialog.__init__(self, principal)
		self.ui = Ui_Agregar()
		self.ui.setupUi(self)
		
		self.error = Error(self)
		
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
		
		self.limpiar()
		
		print "Cancelado"
		self.done(QDialog.Rejected)
	
	def accept(self, ):
		
		e = Empleado()
		
		e.cuil = str(self.ui.leCuil.text())
		
		if '-' in e.cuil:
			try:
				p, doc, s = e.cuil.split('-')
				
				e.documento = doc
			except:
				pass
		else:
			e.documento = e.cuil
		
		e.nombre = str(self.ui.leNombre.text().toUtf8())
		e.apellido = str(self.ui.leApellido.text().toUtf8())
		e.fecha_nacimiento = str(self.ui.deFechaNacimiento.text())
		e.genero = str(self.ui.cmbGenero.currentText())
		e.domicilio = str(self.ui.leDomicilio.text().toUtf8())
		e.telefono = str(self.ui.leTelefono.text())
		e.fecha_ingreso = str(self.ui.deFechaIngreso.text())
		e.nro_legajo = str(self.ui.sbNroLegajo.text())
		e.sit_revista = str(self.ui.cmbRevista.currentText().toUtf8())
		e.cargo = str(self.ui.cmbCargo.currentText().toUtf8())
		
		try:
			e.guardar()
			
			self.limpiar()
			
			print "Aceptado"
			self.done(QDialog.Accepted)
			
		except Exception as e:
			self.error.ui.lblMensaje.setText(str(e).decode('utf-8'))
			self.error.mostrar()
	
	def limpiar(self, ):
		
		self.ui.sbNroLegajo.setValue(0)
		self.ui.leNombre.setText("")
		self.ui.leApellido.setText("")
		self.ui.leCuil.setText("")
		self.ui.leNivel.setText("")
		self.ui.leDomicilio.setText("")
		self.ui.leTelefono.setText("")
		self.ui.cmbGenero.setCurrentIndex(0)
		self.ui.cmbRevista.setCurrentIndex(0)
		self.ui.cmbCargo.setCurrentIndex(0)
		
