# coding=utf-8
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from c.error import Error
from v.ui_eliminar import Ui_Eliminar

class Eliminar(QMessageBox):
	
	principal = None
	error = None
	
	def __init__(self, principal):
		QDialog.__init__(self, principal)
		self.ui = Ui_Eliminar()
		self.ui.setupUi(self)
		
		self.principal = principal
		
		self.error = Error(self)
		
		self.setText("<b>¿Estás seguro de querer eliminar este empleado?</b>".decode('utf-8'))
		self.setInformativeText("Esta acción no se puede deshacer.".decode('utf-8'))
		
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
		
		empleado = str(principal.ui.lblEmpleado.text().toUtf8())
		
		documento = empleado.split('(')[1]
		
		documento = int(documento[:-1])
		
		for e in principal.empleados:
			if e.documento == documento:
				self.e = e
				break
		
		self.setDefaultButton(QMessageBox.Ok)
		
		self.setDetailedText(("Está a punto de eliminar a '" + empleado + "' como empleado, esta acción no tiene vuelta atrás.").decode('utf-8'))
		
		self.show()
		
		self.center()
	
	def closeEvent(self, event):
		pass
	
	def reject(self, ):
		self.done(QDialog.Rejected)
	
	def accept(self, ):
		
		try:
			self.e.eliminar()
			
			self.done(QDialog.Accepted)
			
		except Exception as ex:
			self.error.setText("Ha ocurrido un error mientras intentaba eliminar un empleado.".decode('utf-8'))
			self.error.setDetailedText(str(ex).decode('utf-8'))
			self.error.mostrar()
