#! /usr/bin/python
# coding=utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from c.error import Error
from v.ui_lic_eliminar import Ui_Lic_Eliminar

class Lic_Eliminar(QMessageBox):
	
	l = None
	error = None
	
	def __init__(self, principal):
		QDialog.__init__(self, principal)
		self.ui = Ui_Lic_Eliminar()
		self.ui.setupUi(self)
		
		self.error = Error(self)
		
		self.setText("¿Estás seguro de querer eliminar esta licencia?".decode('utf-8'))
		self.setDetailedText("Esta acción no se puede deshacer.".decode('utf-8'))
		
		self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
		self.button(QMessageBox.Ok).clicked.connect(lambda : self.accept())
		
		self.setButtonText(QMessageBox.Ok, "Eliminar")
		self.setButtonText(QMessageBox.Cancel, "Cancelar")
		
		self.setIcon(QMessageBox.Warning)
	
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def mostrar(self, principal):
		
		self.center()
		
		fila = principal.ui.twLicencias.currentRow()
		
		item = principal.ui.twLicencias.item(fila, 1)
		
		if item is None:
			return
		
		desde = item.text()
		
		for l in principal.licencias:
			if l.desde == desde:
				self.l = l
				break
		
		self.show()
	
	def closeEvent(self, event):
		pass
	
	def reject(self, ):
		self.done(QDialog.Rejected)
	
	def accept(self, ):
		
		try:
			self.l.eliminar()
			
			self.done(QDialog.Accepted)
			
		except Exception as ex:
			self.error.setText("Ha ocurrido un error mientras intentaba eliminar una licencia.".decode('utf-8'))
			self.error.setDetailedText(str(ex).decode('utf-8'))
			self.error.mostrar()
		
