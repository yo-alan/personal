# coding=utf-8

import sys
from conexion import Conexion
from datetime import date, datetime

class Licencia(object):
	
	_cambios = True
	_nuevo = True
	_id = int()
	_id_empleado = int()
	_desde = str()
	_hasta = str()
	_dias_tomados = int()
	_tipo = str()
	_comentario = str()
	
	def __init__(self, id_bbdd=0):
		
		if id_bbdd < 1:
			return
		
		consulta = "SELECT id, id_empleado, desde, hasta, dias_tomados, tipo, comentario FROM licencia WHERE id = " + str(id_bbdd)
		
		Conexion.ejecutar(consulta)
		
		resultset = Conexion.fetchone()
		
		Conexion.cerrar()
		
		if resultset is None:
			return
		
		self._id = resultset[0]
		self.id_empleado = resultset[1]
		self.desde = resultset[2]
		self.hasta = resultset[3]
		self.dias_tomados = resultset[4]
		self.tipo = resultset[5]
		self.comentario = resultset[6]
		self._cambios = False
		self._nuevo = False
	
	"""Inicio: Metodos estaticos"""
	
	@staticmethod
	def licencia(id_empleado, desde, ):
		
		l = Licencia()
		
		consulta = "SELECT id, id_empleado, desde, hasta, dias_tomados, tipo, comentario FROM licencia WHERE id_empleado = " + str(id_empleado) + " AND desde = cast('" + str(desde) + "' as date)"
		
		Conexion.ejecutar(consulta)
		
		resultset = Conexion.fetchone()
		
		Conexion.cerrar()
		
		if resultset is None:
			return
		
		l._id = resultset[0]
		l.id_empleado = resultset[1]
		l.desde = resultset[2]
		l.hasta = resultset[3]
		l.dias_tomados = resultset[4]
		l.tipo = resultset[5]
		l.comentario = resultset[6]
		l._cambios = False
		l._nuevo = False
		
		return l
	
	@staticmethod
	def de_empleado(id_empleado, tipo=""):
		
		if id_empleado < 1:
			return
		
		if tipo != "":
			consulta = "SELECT id FROM licencia WHERE tipo = '" + str(tipo) + "' AND id_empleado = " + str(id_empleado) + " ORDER BY desde"
		else:
			consulta = "SELECT id FROM licencia WHERE id_empleado = " + str(id_empleado) + " ORDER BY desde"
		
		Conexion.ejecutar(consulta)
		
		resultset = Conexion.fetchall()
		
		Conexion.cerrar()
		
		ls = []
		
		for datos in resultset:
			
			l = Licencia(datos[0])
			
			ls.append(l)
			
		return ls
	
	@staticmethod
	def licencias():
		
		ls = []
		
		consulta = "SELECT id FROM licencia"
		
		Conexion.ejecutar(consulta)
		
		resultset = Conexion.fetchall()
		
		Conexion.cerrar()
		
		for datos in resultset:
			
			l = Licencia(datos[0])
			
			ls.append(l)
		
		return ls
	
	"""Fin: Metodos estaticos"""
	
	def guardar(self, ):
		
		if not self._cambios:
			return
		
		if self.id_empleado == 0:
			raise Exception("El empleado no es válido.")
		
		if self.desde == "":
			raise Exception("La fecha desde no es válida.")
		
		if self.hasta == "":
			raise Exception("La fecha hasta no es válida.")
		
		if self.dias_tomados < 1:
			raise Exception("Las fechas no son válidas.")
		
		if self.tipo == "":
			raise Exception("El tipo de licencia no es válido.")
		
		if self._id_empleado == 0:
			raise Exception("El empleado no es válido.")
		
		dic  = {"a1" : "id_empleado", 
				"a2" : "desde", 
				"a3" : "hasta", 
				"a4" : "dias_tomados", 
				"a5" : "tipo", 
				"a6" : "comentario", 
				}
		
		vals = {"v1" : self.id_empleado, 
				"v2" : self.desde, 
				"v3" : self.hasta, 
				"v4" : self.dias_tomados, 
				"v5" : self.tipo, 
				"v6" : self.comentario, 
				}
		
		#VALIDO QUE EXISTA EL EMPLEADO
		consulta = "SELECT id FROM empleado WHERE id = " + str(self.id_empleado)
		
		Conexion.ejecutar(consulta)
		
		resultset = Conexion.fetchone()
		
		Conexion.cerrar()
		
		if resultset is None:
			raise Exception("El empleado no es válido.")
		
		#VALIDO QUE NO EXISTA UNA LICENCIA EN EL MISMO PERIODO DE TIEMPO
		consulta = "SELECT id FROM licencia " +\
					"WHERE (desde <= cast('" + str(self.desde) + "' as date) AND hasta >= cast('" + str(self.desde) + "' as date) " + \
					"OR desde <= cast('" + str(self.hasta) + "' as date) AND hasta >= cast('" + str(self.hasta) + "' as date) " +\
					"OR desde >= cast('" + str(self.desde) + "' as date) AND hasta <= cast('" + str(self.hasta) + "' as date)) " +\
					"AND id != " + str(self.id) +\
					" AND id_empleado = " + str(self.id_empleado)
		
		Conexion.ejecutar(consulta)
		
		resultset = Conexion.fetchone()
		
		Conexion.cerrar()
		
		if resultset is not None:
			raise Exception("El empleado ya se está tomando una licencia en esta fecha.")
		
		if self.tipo == "58":
			
			if self.dias_tomados > 1:
				raise Exception("La cantidad de días no es válida para una licencia de tipo 58.")
			
			ls = Licencia.de_empleado(self.id_empleado, "58")
			
			cant_por_anio = 0
			for l in ls:
				anio = l.desde.split('/')[2]
				if anio == self.desde.split('/')[2] and l.id != self.id:
					cant_por_anio = cant_por_anio + 1
			
			if cant_por_anio >= 6:
				raise Exception("El empleado ya se tomó 6 artículos 58 este año.")
			
			cant_por_mes = 0
			for l in ls:
				mes = l.desde.split('/')[1]
				if mes == self.desde.split('/')[1] and l.id != self.id:
					cant_por_mes = cant_por_mes + 1
			
			if cant_por_mes >= 2:
				raise Exception("El empleado ya se tomó 2 artículos 58 este mes.")
		
		if self._nuevo:
			
			consulta = "INSERT INTO licencia('a1', 'a2', 'a3', 'a4', 'a5', 'a6') VALUES('v1', 'v2', 'v3', 'v4', 'v5', 'v6') RETURNING id"
			
			for i in range(1, 7):
				
				if vals["v" + str(i)]:
					
					consulta = consulta.replace("'a" + str(i) + "'", str(dic["a" + str(i)]))
					
					if isinstance(vals["v" + str(i)], int):
						consulta = consulta.replace("'v" + str(i) + "'", str(vals["v" + str(i)]))
					else:
						if '/' in str(vals["v" + str(i)]):
							consulta = consulta.replace("'v" + str(i) + "'", "cast('" + str(vals["v" + str(i)]) + "' as date)")
						else:
							consulta = consulta.replace("'v" + str(i) + "'", "'" + str(vals["v" + str(i)]) + "'")
				else:
					if "'v" + str(i) + "', " in consulta:
						consulta = consulta.replace("'a" + str(i) + "', ", "")
						consulta = consulta.replace("'v" + str(i) + "', ", "")
					elif ", " + "'v" + str(i) + "')" in consulta:
						consulta = consulta.replace(", " + "'a" + str(i) + "'", "")
						consulta = consulta.replace(", " + "'v" + str(i) + "'", "")
			
		else:
			
			consulta = "SELECT id FROM licencia WHERE desde = cast('" + str(self.desde) + "' as date) AND id_empleado = " + str(self.id_empleado)
			
			Conexion.ejecutar(consulta)
			
			resultset = Conexion.fetchone()
			
			Conexion.cerrar()
			
			if resultset is not None:
				for id_bbdd in resultset:
					if id_bbdd != self.id:
						raise Exception("Ya existe esta licencia para este empleado.")
			
			consulta = "UPDATE licencia SET 'a1' = 'v1', 'a2' = 'v2', 'a3' = 'v3', 'a4' = 'v4', 'a5' = 'v5', 'a6' = 'v6' WHERE id = " + str(self.id)
			
			for i in range(1, 7):
				
				consulta = consulta.replace("'a" + str(i) + "'", str(dic["a" + str(i)]))
				
				if isinstance(vals["v" + str(i)], int) or isinstance(vals["v" + str(i)], float):
					consulta = consulta.replace("'v" + str(i) + "'", str(vals["v" + str(i)]))
				else:
					if '/' in str(vals["v" + str(i)]):
						consulta = consulta.replace("'v" + str(i) + "'", "cast('" + str(vals["v" + str(i)]) + "' as date)")
					else:
						consulta = consulta.replace("'v" + str(i) + "'", "'" + str(vals["v" + str(i)]) + "'")
		
		Conexion.ejecutar(consulta)
		
		if self._nuevo:
			self._id = Conexion.fetchone()[0]
			self._nuevo = False
			self._cambios = False
		
		Conexion.cerrar()
	
	def eliminar(self, ):
		
		if self._nuevo:
			return
		
		if self.id == 0:
			return
		
		consulta = "DELETE FROM licencia WHERE id = " + str(self.id)
		Conexion.ejecutar(consulta)
		Conexion.cerrar()
		
		self._nuevo = True
		self._cambios = True
	
	"""Inicio: Getters y Setters"""
	
	@property
	def id(self):
		return self._id
	
	@property
	def id_empleado(self):
		return self._id_empleado
	
	@id_empleado.setter
	def id_empleado(self, id_empleado):
		
		try:
			id_empleado = int(id_empleado)
			
			if id_empleado < 1:
				raise ValueError
			
		except ValueError:
			raise Exception("El empleado no es válido.")
		
		if self._id_empleado != id_empleado:
			self._id_empleado = id_empleado
			self._cambios = True
	
	@property
	def desde(self):
		return self._desde
	
	@desde.setter
	def desde(self, desde):
		
		desde = str(desde)
		
		dia = ""
		mes = ""
		anio = ""
		
		if "/" in desde:
			dia, mes, anio = desde.split('/')
		elif "-" in desde:
			anio, mes, dia = desde.split('-')
		else:
			raise Exception("La fecha desde posee un formato no válido.")
		
		dia = int(dia)
		mes = int(mes)
		anio = int(anio)
		
		try:
			datetime(anio, mes, dia)
		except ValueError:
			raise Exception("La fecha desde no es válida.")
		
		dia = str(dia)
		mes = str(mes)
		anio = str(anio)
		
		if self._desde != dia + "/" + mes + "/" + anio:
			self._desde = dia + "/" + mes + "/" + anio
			self._cambios = True
		
		if self._hasta != "":
			
			ddia, dmes, danio = str(self._desde).split('/')
			hdia, hmes, hanio = str(self._hasta).split('/')
			
			comp_desde = datetime(int(danio), int(dmes), int(ddia))
			comp_hasta = datetime(int(hanio), int(hmes), int(hdia))
			
			self.dias_tomados = (comp_hasta - comp_desde).days + 1
	
	@property
	def hasta(self):
		return self._hasta
	
	@hasta.setter
	def hasta(self, hasta):
		
		hasta = str(hasta)
		
		dia = ""
		mes = ""
		anio = ""
		
		if "/" in hasta:
			dia, mes, anio = hasta.split('/')
		elif "-" in hasta:
			anio, mes, dia = hasta.split('-')
		else:
			raise Exception("La fecha hasta posee un formato no válido.")
		
		dia = int(dia)
		mes = int(mes)
		anio = int(anio)
		
		try:
			datetime(anio, mes, dia)
		except ValueError:
			raise Exception("La fecha hasta no es válida.")
		
		dia = str(dia)
		mes = str(mes)
		anio = str(anio)
		
		if self._hasta != dia + "/" + mes + "/" + anio:
			self._hasta = dia + "/" + mes + "/" + anio
			self._cambios = True
		
		if self._desde != "":
			
			ddia, dmes, danio = str(self._desde).split('/')
			hdia, hmes, hanio = str(self._hasta).split('/')
			
			comp_desde = datetime(int(danio), int(dmes), int(ddia))
			comp_hasta = datetime(int(hanio), int(hmes), int(hdia))
			
			self.dias_tomados = (comp_hasta - comp_desde).days + 1
	
	@property
	def dias_tomados(self):
		return self._dias_tomados
	
	@dias_tomados.setter
	def dias_tomados(self, dias_tomados):
		
		try:
			dias_tomados = int(dias_tomados)
			
			if dias_tomados < 1:
				raise ValueError
			
		except ValueError:
			raise Exception("La cantidad de días no es válida.")
		
		if self._dias_tomados != dias_tomados:
			self._dias_tomados = dias_tomados
			self._cambios = True
	
	@property
	def tipo(self):
		return self._tipo
	
	@tipo.setter
	def tipo(self, tipo):
		
		if tipo is None or (isinstance(tipo, str) and tipo == ""):
			raise Exception("El tipo de licencia es un campo requerido.")
		
		tipo = tipo.capitalize()
		
		tipos = ['18', '3', '53', '58', 'Comisión', 'Enfermedad', 'Franco', 'Otro']
		
		if tipo not in tipos:
			raise Exception("El tipo de licencia no es válido.")
		
		if self._tipo != tipo:
			self._tipo = tipo
			self._cambios = True
	
	@property
	def comentario(self):
		return self._comentario
	
	@comentario.setter
	def comentario(self, comentario):
		
		if comentario is None:
			return
		
		if self._comentario == comentario:
			return
		
		comentario.replace(';', ',')
		
		self._comentario = comentario
		self._cambios = True
	
	"""Fin: Getters y Setters"""
