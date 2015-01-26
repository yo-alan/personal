#! /usr/bin/python
# coding=utf-8

import datetime

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from c.error import Error
from v.ui_lic_agregar import Ui_Lic_Agregar
from m.licencia import Licencia
from m.empleado import Empleado

def fecha_actual():
	return str(datetime.datetime.now().date())

class Lic_Agregar(QDialog):
	
	error = None
	
	def __init__(self, principal):
		QDialog.__init__(self, principal)
		self.ui = Ui_Lic_Agregar()
		self.ui.setupUi(self)
		
		self.ui.buttonBox.button(QDialogButtonBox.Ok).setText("Aceptar")
		self.ui.buttonBox.button(QDialogButtonBox.Cancel).setText("Cancelar")
		
		self.error = Error(self)
		
		self.ui.deDesde.dateChanged.connect(lambda : self.actualizarFechas())
		self.ui.deHasta.dateChanged.connect(lambda : self.actualizarFechas())
		
	
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def mostrar(self, principal):
		
		self.center()
		
		self.ui.groupBox.setTitle("Empleado: " + str(principal.ui.lblEmpleado.text().toUtf8()).decode('utf-8'))
		
		anio, mes, dia = fecha_actual().split('-')
		
		fecha = QDate()
		fecha.setDate(int(anio), int(mes), int(dia))
		self.ui.deDesde.setDate(fecha)
		self.ui.deHasta.setDate(fecha)
		
		self.show()
	
	def actualizarFechas(self, ):
		
		desde = str(self.ui.deDesde.text())
		hasta = str(self.ui.deHasta.text())
		
		qdhasta = QDate()
		
		ddia, dmes, danio = desde.split('/')
		hdia, hmes, hanio = hasta.split('/')
		
		if datetime.datetime(int(danio), int(dmes), int(ddia)) > datetime.datetime(int(hanio), int(hmes), int(hdia)):
			qdhasta.setDate(int(danio), int(dmes), int(ddia))
			
			self.ui.deHasta.setDate(qdhasta)
	
	def closeEvent(self, event):
		pass
	
	def reject(self, ):
		
		self.limpiar()
		
		self.done(QDialog.Rejected)
	
	def accept(self, ):
		
		try:
			empleado = str(self.ui.groupBox.title().toUtf8())
			
			documento = empleado.split('(')[1]
			
			documento = documento[:-1]
			
			e = Empleado.empleado(documento)
			
			tipo = self.ui.cmbTipoLicencia.currentText().toUtf8()
			desde = self.ui.deDesde.text()
			hasta = self.ui.deHasta.text()
			comentario = self.ui.leComentario.text().toUtf8()
			
			l = Licencia()
			
			l.id_empleado = e.id
			l.tipo = str(tipo)
			l.desde = str(desde)
			l.hasta = str(hasta)
			l.comentario = str(comentario)
			
			
			l.guardar()
			
			self.limpiar()
			
			self.done(QDialog.Accepted)
			
		except Exception as ex:
			self.error.setText("Ha ocurrido un error mientras intentaba agregar un licencia nueva.".decode('utf-8'))
			self.error.setDetailedText(str(ex).decode('utf-8'))
			self.error.mostrar()
	
	def limpiar(self, ):
		
		self.ui.groupBox.setTitle("Empleado")
		self.ui.cmbTipoLicencia.setCurrentIndex(0)
		self.ui.leComentario.setText("")
		
