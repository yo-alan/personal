#! /usr/bin/python
# coding=utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from c.error import Error
from v.ui_editar import Ui_Editar
from m.empleado import Empleado

class Editar(QDialog):
	
	e = None
	error = None
	
	def __init__(self, principal):
		QDialog.__init__(self, principal)
		self.ui = Ui_Editar()
		self.ui.setupUi(self)
		
		self.error = Error(self)
		
		self.ui.leCuil.textChanged.connect(lambda : self.cambioCuil())
		
		#CODIGO PARA HACER
	
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
	
	def mostrar(self, principal):
		
		self.center()
		
		empleado = str(principal.ui.lblEmpleado.text().toUtf8())
		
		documento = empleado.split('(')[1]
		
		documento = int(documento[:-1])
		
		for e in principal.empleados:
			if e.documento == documento:
				self.e = e
				break
		
		if self.e.cuil == "":
			self.ui.leCuil.setText(str(self.e.documento))
		else:
			self.ui.leCuil.setText(self.e.cuil)
		self.ui.leNombre.setText(self.e.nombre.decode('utf-8'))
		self.ui.leApellido.setText(self.e.apellido.decode('utf-8'))
		
		f_nacimiento = QDate()
		dia, mes, anio = self.e.fecha_nacimiento.split('/')
		f_nacimiento.setDate(int(anio), int(mes), int(dia))
		self.ui.deFechaNacimiento.setDate(f_nacimiento)
		
		generos = {'F' : 0, 'M' : 1}
		self.ui.cmbGenero.setCurrentIndex(generos[self.e.genero])
		self.ui.leDomicilio.setText(self.e.domicilio.decode('utf-8'))
		self.ui.leTelefono.setText(self.e.telefono)
		
		f_ingreso = QDate()
		dia, mes, anio = self.e.fecha_ingreso.split('/')
		f_ingreso.setDate(int(anio), int(mes), int(dia))
		self.ui.deFechaIngreso.setDate(f_ingreso)
		self.ui.sbNroLegajo.setValue(self.e.nro_legajo)
		
		revistas = {'Comisión' : 0, 'Pasantía' : 1, 'Permanente' : 2, 'Temporaria' : 3, 'Transitoria' : 4}
		self.ui.cmbRevista.setCurrentIndex(revistas[self.e.sit_revista])
		
		cargos = {'Administrativo' : 0, 'Jerárquico' : 1, 'Obrero' : 2, 'Profesional' : 3, 'Servicio' : 4}
		self.ui.cmbCargo.setCurrentIndex(cargos[self.e.cargo])
		
		self.show()
	
	def closeEvent(self, event):
		pass
	
	def reject(self, ):
		
		self.limpiar()
		
		self.done(QDialog.Rejected)
		
	def accept(self, ):
		
		self.e.cuil = str(self.ui.leCuil.text())
		
		self.done(QDialog.Accepted)
		
		if '-' in self.e.cuil:
			try:
				p, doc, s = self.e.cuil.split('-')
				
				self.e.documento = doc
			except:
				pass
		else:
			self.e.documento = self.e.cuil
		
		self.e.nombre = str(self.ui.leNombre.text().toUtf8())
		self.e.apellido = str(self.ui.leApellido.text().toUtf8())
		self.e.fecha_nacimiento = str(self.ui.deFechaNacimiento.text())
		self.e.genero = str(self.ui.cmbGenero.currentText())
		self.e.domicilio = str(self.ui.leDomicilio.text().toUtf8())
		self.e.telefono = str(self.ui.leTelefono.text())
		self.e.fecha_ingreso = str(self.ui.deFechaIngreso.text())
		self.e.nro_legajo = str(self.ui.sbNroLegajo.text())
		self.e.sit_revista = str(self.ui.cmbRevista.currentText().toUtf8())
		self.e.cargo = str(self.ui.cmbCargo.currentText().toUtf8())
		
		try:
			self.e.guardar()
			
			self.limpiar()
			
		except Exception as e:
			print e
		
		print "Aceptado"
		self.done(QDialog.Accepted)
	
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
		
