#! /usr/bin/python
# coding=utf-8

import datetime, sys, os

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from v.ui_principal import Ui_Principal
from c.agregar import Agregar
from c.editar import Editar
from c.eliminar import Eliminar
from c.buscar import Buscar
from c.lic_agregar import Lic_Agregar
from c.lic_editar import Lic_Editar
from c.lic_eliminar import Lic_Eliminar
from c.lic_buscar import Lic_Buscar
from c.acerca_de import Acerca_de

from m.empleado import Empleado
from m.licencia import Licencia

def destildar(s):
	
	tildes = {'á' : 'a', 'é' : 'e', 'í' : 'i', 'ó' : 'o', 'ú' : 'u'}
	
	try:
		for t in tildes:
			s = s.replace(t, tildes[t])
	except:
		pass
	
	return s

def fecha_actual():
	return str(datetime.datetime.now().date())

def reiniciar():
	
	python = sys.executable
	
	os.execl(python, python, * sys.argv)

class Principal(QMainWindow):
	
	buscar = None
	editar = None
	eliminar = None
	agregar = None
	
	lic_buscar = None
	lic_editar = None
	lic_eliminar = None
	lic_agregar = None
	
	e = None
	empleados = []
	licencias = []
	
	def __init__(self, ):
		QMainWindow.__init__(self, None)
		self.ui = Ui_Principal()
		self.ui.setupUi(self)
		
		self.agregar = Agregar(self)
		self.editar = Editar(self)
		self.eliminar = Eliminar(self)
		self.buscar = Buscar(self)
		
		self.lic_agregar = Lic_Agregar(self)
		self.lic_editar = Lic_Editar(self)
		self.lic_eliminar = Lic_Eliminar(self)
		self.lic_buscar = Lic_Buscar(self)
		
		self.acerca_de = Acerca_de(self)
		
		self.ui.leEmpleadoFilter.textChanged.connect(lambda : self.actualizarTwEmpleados())
		
		self.ui.twEmpleados.itemDoubleClicked.connect(lambda : self.empleadoDobleClick())
		
		self.ui.twLicencias.itemDoubleClicked.connect(lambda : self.lic_editar.mostrar(self))
		self.ui.twLicencias.cellClicked.connect(lambda : self.licenciasCellClicked())
		
		self.ui.cmbTipoLicencia.currentIndexChanged.connect(lambda : self.cambioTipoLicencia())
		self.ui.cmbPeriodo.currentIndexChanged.connect(lambda : self.cambioPeriodo())
		
		self.ui.pbAgregar.clicked.connect(lambda : self.agregar.mostrar())
		self.ui.pbEditar.clicked.connect(lambda : self.editar.mostrar(self))
		self.ui.pbEliminar.clicked.connect(lambda : self.eliminar.mostrar(self))
		
		self.ui.pbLicAgregar.clicked.connect(lambda : self.lic_agregar.mostrar(self))
		self.ui.pbLicEditar.clicked.connect(lambda : self.lic_editar.mostrar(self))
		self.ui.pbLicEliminar.clicked.connect(lambda : self.lic_eliminar.mostrar(self))
		
		self.agregar.accepted.connect(lambda : self.cargarEmpleados())
		self.editar.accepted.connect(lambda : self.cargarEmpleados())
		self.eliminar.accepted.connect(lambda : self.cargarEmpleados())
		
		self.lic_agregar.accepted.connect(lambda : self.actualizarTwLicencias())
		self.lic_editar.accepted.connect(lambda : self.actualizarTwLicencias())
		self.lic_eliminar.accepted.connect(lambda : self.actualizarTwLicencias())
		
		self.agregar.accepted.connect(lambda : self.actualizarTwEmpleados())
		self.editar.accepted.connect(lambda : self.actualizarTwEmpleados())
		
		self.ui.pbEditarObservaciones.clicked.connect(lambda : self.editarObservaciones())
		
		#ACCIONES
		self.ui.aAgregar.triggered.connect(lambda : self.agregar.mostrar())
		self.ui.aEditar.triggered.connect(lambda : self.editar.mostrar(self))
		self.ui.aEliminar.triggered.connect(lambda : self.eliminar.mostrar(self))
		
		self.ui.aAgregarLicencia.triggered.connect(lambda : self.lic_agregar.mostrar(self))
		self.ui.aEditarLicencia.triggered.connect(lambda : self.lic_editar.mostrar(self))
		self.ui.aEliminarLicencia.triggered.connect(lambda : self.lic_eliminar.mostrar(self))
		
		self.ui.aAcerca_de.triggered.connect(lambda : self.acerca_de.mostrar())
		
		self.ui.aReiniciar.triggered.connect(lambda : reiniciar())
		self.ui.aSalir.triggered.connect(lambda : exit())
	
	def mostrar(self, ):
		
		self.center()
		
		self.cargarEmpleados()
		
		self.show()
	
	def editarObservaciones(self, ):
		
		texto = str(self.ui.pbEditarObservaciones.text())
		
		if texto == "Editar":
			
			self.ui.txtEObservaciones.setEnabled(True)
			
			self.ui.pbEditarObservaciones.setText("Guardar")
		else:
			
			self.e.observaciones = str(self.ui.txtEObservaciones.toPlainText().toUtf8())
			
			try:
				self.e.guardar()
				
				self.ui.txtEObservaciones.setEnabled(False)
				
				self.ui.pbEditarObservaciones.setText("Editar")
			except Exception as e:
				print str(e)
	
	def actualizarTwLicencias(self, bbdd=True, periodo=None):
		
		self.ui.twLicencias.setRowCount(0)
		
		tipo = str(self.ui.cmbTipoLicencia.currentText().toUtf8())
		
		if bbdd:
			self.licencias = Licencia.de_empleado(self.e.id)
		
		if len(self.licencias) == 0:
			self.ui.pbLicEditar.setEnabled(False)
			self.ui.pbLicEliminar.setEnabled(False)
			return
		
		resultado = []
		
		for l in self.licencias:
			
			if periodo is not None:
				
				dia, mes, anio = l.desde.split('/')
				
				dtDesde = datetime.datetime(int(anio), int(mes), int(dia))
				
				if (tipo == "Todas" or l.tipo == tipo) and dtDesde >= periodo:
					resultado.append(l)
				
			elif (tipo == "Todas" or l.tipo == tipo):
				resultado.append(l)
			
		
		i = 0
		rows = 1
		for l in resultado:
			
			self.ui.twLicencias.setRowCount(rows)
			
			item = QTableWidgetItem()
			item.setText(str(l.tipo).decode('utf-8'))
			self.ui.twLicencias.setItem(i, 0, item)
			
			item = QTableWidgetItem()
			item.setText(str(l.desde))
			self.ui.twLicencias.setItem(i, 1, item)
			
			item = QTableWidgetItem()
			item.setText(str(l.hasta))
			self.ui.twLicencias.setItem(i, 2, item)
			
			item = QTableWidgetItem()
			item.setText(str(l.dias_tomados))
			self.ui.twLicencias.setItem(i, 3, item)
			
			item = QTableWidgetItem()
			item.setText(str(l.comentario).decode('utf-8'))
			self.ui.twLicencias.setItem(i, 4, item)
			
			i = i + 1
			rows = rows + 1
		
	
	def cambioPeriodo(self, ):
		
		periodo = str(self.ui.cmbPeriodo.currentText().toUtf8())
		
		anio, mes, dia = fecha_actual().split('-')
		
		p = None
		
		if periodo == "Última semana":
			actual = datetime.datetime(int(anio), int(mes), int(dia))
			
			p = datetime.datetime(int(anio), int(mes), int(dia) - actual.weekday())
		elif periodo == "Último mes":
			p = datetime.datetime(int(anio), int(mes), 1)
		elif periodo == "Último año":
			p = datetime.datetime(int(anio), 1, 1)
		
		self.actualizarTwLicencias(False, p)
	
	def cambioTipoLicencia(self, ):
		
		self.ui.pbLicEditar.setEnabled(False)
		self.ui.pbLicEliminar.setEnabled(False)
		
		self.actualizarTwLicencias(False)
	
	def licenciasCellClicked(self, ):
		
		self.ui.pbLicEditar.setEnabled(True)
		self.ui.pbLicEliminar.setEnabled(True)
		
		self.ui.aEditarLicencia.setEnabled(True)
		self.ui.aEliminarLicencia.setEnabled(True)
	
	def empleadoDobleClick(self, ):
		
		empleado = self.ui.lblEmpleado.text()
		
		doc2 = empleado.split('(')[1]
		
		doc2 = doc2[:-1]
		
		empleado = self.ui.twEmpleados.currentItem().text(0)
		
		documento = empleado.split('(')[1]
		
		documento = documento[:-1]
		
		if documento == doc2:
			return
		
		self.ui.pbLicEditar.setEnabled(False)
		self.ui.pbLicEliminar.setEnabled(False)
		self.ui.pbLicAgregar.setEnabled(True)
		self.ui.pbEliminar.setEnabled(True)
		self.ui.pbEditar.setEnabled(True)
		#self.ui.pbGrupoFamiliar.setEnabled(True)
		self.ui.pbEditarObservaciones.setEnabled(True)
		self.ui.aEditar.setEnabled(True)
		self.ui.aEliminar.setEnabled(True)
		self.ui.aAgregarLicencia.setEnabled(True)
		self.ui.cmbTipoLicencia.setCurrentIndex(0)
		self.ui.cmbPeriodo.setCurrentIndex(0)
		
		for e in self.empleados:
			if e.documento == int(documento):
				self.e = e
				break
		
		self.licencias = Licencia.de_empleado(self.e.id)
		
		self.ui.lblEmpleado.setText(empleado)
		
		
		item = QTableWidgetItem()
		item.setText(str(e.nombre).decode('utf-8'))
		self.ui.twDatosPersonales.setItem(0, 1, item)
		
		item = QTableWidgetItem()
		item.setText(str(e.apellido).decode('utf-8'))
		self.ui.twDatosPersonales.setItem(1, 1, item)
		
		item = QTableWidgetItem()
		item.setText(str(e.documento))
		self.ui.twDatosPersonales.setItem(2, 1, item)
		
		item = QTableWidgetItem()
		item.setText(str(e.fecha_nacimiento))
		self.ui.twDatosPersonales.setItem(3, 1, item)
		
		item = QTableWidgetItem()
		if e.genero == 'F':
			item.setText("Femenino")
		else:
			item.setText("Masculino")
		self.ui.twDatosPersonales.setItem(4, 1, item)
		
		item = QTableWidgetItem()
		item.setText(str(e.telefono))
		self.ui.twDatosPersonales.setItem(5, 1, item)
		
		item = QTableWidgetItem()
		item.setText(str(e.domicilio).decode('utf-8'))
		self.ui.twDatosPersonales.setItem(6, 1, item)
		
		
		item = QTableWidgetItem()
		item.setText(str(e.cuil))
		self.ui.twDatosLaborales.setItem(0, 1, item)
		
		item = QTableWidgetItem()
		item.setText(str(e.fecha_ingreso))
		self.ui.twDatosLaborales.setItem(1, 1, item)
		
		item = QTableWidgetItem()
		item.setText(str(e.nro_legajo))
		self.ui.twDatosLaborales.setItem(2, 1, item)
		
		item = QTableWidgetItem()
		item.setText(str(e.sit_revista).decode('utf-8'))
		self.ui.twDatosLaborales.setItem(3, 1, item)
		
		item = QTableWidgetItem()
		item.setText(str(e.cargo).decode('utf-8'))
		self.ui.twDatosLaborales.setItem(4, 1, item)
		
		self.ui.txtEObservaciones.setText(str(e.observaciones).decode('utf-8'))
		
		self.actualizarTwLicencias(False)
	
	def actualizarTwEmpleados(self, ):
		
		self.ui.twEmpleados.clear()
		
		items = []
		
		filtro = str(self.ui.leEmpleadoFilter.text().toUtf8()).lower().split(' ')
		
		for e in self.empleados:
			
			no = False
			for f in filtro:
				
				if f not in destildar(str(e)).lower() and f not in str(e).lower():
					no = True
			
			if no:
				continue
			
			item = QTreeWidgetItem()
			item.setText(0, str(e).decode('utf-8'))
			item.setToolTip(0, str(e).decode('utf-8'))
			
			items.append(item)
		
		self.ui.twEmpleados.addTopLevelItems(items)
	
	def estado(self, msg):
		
		estado = QLabel()
		estado.setText(msg.decode('utf-8'))
		self.ui.statusBar.addWidget(estado, 0)
	
	def cargarEmpleados(self, ):
		
		try:
			self.empleados = Empleado.empleados()
		except Exception as e:
			self.estado("Ha ocurrido un error, no existe una conexion a la base de datos.")
		
		self.actualizarTwEmpleados()
	
	def center(self, ):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	
	def keyPressEvent(self, event):
		
		if event.key() == Qt.Key_Return:
			if self.ui.twLicencias.hasFocus():
				self.lic_editar.mostrar(self)
		
		if QApplication.keyboardModifiers() != Qt.ControlModifier:
			return
		
		if event.key() == Qt.Key_F:
			self.ui.leEmpleadoFilter.setFocus(True)
	
	def closeEvent(self, event):
		pass
