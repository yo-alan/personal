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
		
		self.ui.buttonBox.button(QDialogButtonBox.Ok).setText("Aceptar")
		self.ui.buttonBox.button(QDialogButtonBox.Cancel).setText("Cancelar")
		
		self.error = Error(self)
		
		self.ui.leCuil.textChanged.connect(lambda : self.cambioCuil())
	
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def cambioCuil(self, ):
		c = str(self.ui.leCuil.text())
		
		if len(c) < 8:
			return
		elif len(c) > 8 and "-" not in c:
			c = c[:2] + "-" + c[2:]
		elif len(c) == 12 and not c.endswith('-') and c[10] != '-':
			c = c[:11] + "-" + c[11:]
		elif len(c) == 13 and c[11] != '-':
			c = c[:12]
		
		self.ui.leCuil.setText(c)
	
	def mostrar(self, ):
		
		self.center()
		
		self.show()
	
	def closeEvent(self, event):
		pass
	
	def reject(self, ):
		
		self.limpiar()
		
		self.done(QDialog.Rejected)
	
	def accept(self, ):
		try:
			e = Empleado()
			
			e.cuil = str(self.ui.leCuil.text())
			
			if '-' in e.cuil:
				
				p = ""
				doc = ""
				s = ""
				
				try:
					p, doc, s = e.cuil.split('-')
				except Exception as ex:
					raise Exception("El cuil no cumple con el formato necesario: " + str(ex))
				
				e.documento = doc
				
			else:
				e.documento = str(self.ui.leCuil.text())
			
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
			
			e.guardar()
			
			self.limpiar()
			
			self.done(QDialog.Accepted)
			
		except Exception as ex:
			self.error.setText("Ha ocurrido un error mientras intentaba agregar un empleado nuevo.".decode('utf-8'))
			self.error.setDetailedText(str(ex).decode('utf-8'))
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
		
