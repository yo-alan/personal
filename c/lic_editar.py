#! /usr/bin/python
# coding=utf-8

import datetime

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from c.error import Error
from v.ui_lic_editar import Ui_Lic_Editar
from m.licencia import Licencia
from m.empleado import Empleado

class Lic_Editar(QDialog):
	
	l = None
	error = None
	
	def __init__(self, principal):
		QDialog.__init__(self, principal)
		self.ui = Ui_Lic_Editar()
		self.ui.setupUi(self)
		
		self.error = Error(self)
		
		self.ui.deDesde.dateChanged.connect(lambda : self.actualizarFechas())
		self.ui.deHasta.dateChanged.connect(lambda : self.actualizarFechas())
		
		#CODIGO PARA HACER
	
	def mostrar(self, principal):
		
		self.center()
		
		self.ui.groupBox.setTitle("Empleado: " + str(principal.ui.lblEmpleado.text().toUtf8()).decode('utf-8'))
		
		fila = principal.ui.twLicencias.currentRow()
		
		item = principal.ui.twLicencias.item(fila, 1)
		
		if item is None:
			return
		
		desde = item.text()
		
		for l in principal.licencias:
			if l.desde == desde:
				self.l = l
				break
		
		tipos = {'18' : 0, '3' : 1, '53' : 2, '58' : 3, 'Comisión' : 4, 'Enfermedad' : 5, 'Franco' : 6, 'Otro' : 7}
		
		self.ui.cmbTipoLicencia.setCurrentIndex(tipos[self.l.tipo])
		
		fecha_desde = QDate()
		dia, mes, anio = self.l.desde.split('/')
		fecha_desde.setDate(int(anio), int(mes), int(dia))
		
		self.ui.deDesde.setDate(fecha_desde)
		
		fecha_hasta = QDate()
		dia, mes, anio = self.l.hasta.split('/')
		fecha_hasta.setDate(int(anio), int(mes), int(dia))
		
		self.ui.deHasta.setDate(fecha_hasta)
		
		if self.l.comentario != "":
			self.ui.leComentario.setText(self.l.comentario)
		
		self.show()
	
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
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
		
			tipo = self.ui.cmbTipoLicencia.currentText().toUtf8()
			desde = self.ui.deDesde.text()
			hasta = self.ui.deHasta.text()
			comentario = self.ui.leComentario.text().toUtf8()
			
			self.l.tipo = str(tipo)
			self.l.desde = str(desde)
			self.l.hasta = str(hasta)
			self.l.comentario = str(comentario)
			
			
			self.l.guardar()
			
			self.limpiar()
			
			self.done(QDialog.Accepted)
			
		except Exception as ex:
			self.error.setText("Ha ocurrido un mientras intentaba editar una licencia.".decode('utf-8'))
			self.error.setDetailedText(str(ex).decode('utf-8'))
			self.error.mostrar()
	
	def limpiar(self, ):
		
		self.ui.groupBox.setTitle("Empleado")
		self.ui.cmbTipoLicencia.setCurrentIndex(0)
		self.ui.leComentario.setText("")
		
