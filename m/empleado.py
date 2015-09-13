# coding=utf-8
from datetime import datetime

from conexion import Conexion
from licencia import Licencia

def esalfa(s):
	
	cs = s
	
	if 'á' in s:
		s = s.replace('á', '')
	if 'é' in s:
		s = s.replace('é', '')
	if 'í' in s:
		s = s.replace('í', '')
	if 'ó' in s:
		s = s.replace('ó', '')
	if 'ú' in s:
		s = s.replace('ú', '')
	if 'ñ' in s:
		s = s.replace('ñ', '')
	
	if s.isalpha():
		return True
	
	return False
	

def quitar_doble_espacios(s):
	
	while s.find("  ") != -1:
		s = s.replace("  ", " ")
	
	if s == "":
		return s
	
	if s[len(s)-1] == " ":
		s = s[0:len(s)-1]
	
	if s[0] == " ":
		s = s[1:]
	
	return s

class Empleado(object):
	
	_cambios = True
	_nuevo = True
	_id = int()
	_documento = int()
	_nombre = str()
	_apellido = str()
	_fecha_nacimiento = str()
	_genero = str()
	_domicilio = str()
	_telefono = str()
	_fecha_ingreso = str()
	_cuil = str()
	_nro_legajo = str()
	_sit_revista = str()
	_cargo = str()
	_observaciones = str()
	
	def __init__(self, documento=0):
		
		if int(documento) != 0:
			e = Empleado.empleado(documento)
			
			self._id = e.id
			self.documento = e.documento
			self.nombre = e.nombre
			self.apellido = e.apellido
			self.fecha_nacimiento = e.fecha_nacimiento
			self.genero = e.genero
			self.domicilio = e.domicilio
			self.telefono = e.telefono
			self.fecha_ingreso = e.fecha_ingreso
			self.cuil = e.cuil
			self.nro_legajo = e.nro_legajo
			self.sit_revista = e.sit_revista
			self.cargo = e.cargo
			self.observaciones = e.observaciones
			self._cambios = False
			self._nuevo = False
			
	
	def __int__(self):
		return self._id
	
	def __str__(self):
		return self.apellido + ", " + self.nombre + " (" + str(self.documento) + ")"
	
	def __eq__(self, o):
		
		if not isinstance(o, Empleado):
			return False
		
		if self.documento != "" and o.documento != "":
			return self.documento == o.documento
		else:
			return False
	
	@staticmethod
	def empleado(documento):
		
		e = Empleado()
		
		consulta = "SELECT * FROM empleado WHERE documento = " + str(documento)
		
		Conexion.ejecutar(consulta)
		
		resultset = Conexion.fetchone()
		
		Conexion.cerrar()
		
		if resultset is not None:
			
			e._id = resultset[0]
			e.documento = resultset[1]
			e.nombre = resultset[2]
			e.apellido = resultset[3]
			e.fecha_nacimiento = resultset[4]
			e.genero = resultset[5]
			e.domicilio = resultset[6]
			e.telefono = resultset[7]
			e.fecha_ingreso = resultset[8]
			e.cuil = resultset[9]
			e.nro_legajo = resultset[10]
			e.sit_revista = resultset[11]
			e.cargo = resultset[12]
			e.observaciones = resultset[13]
			e._cambios = False
			e._nuevo = False
		
		return e
	
	@staticmethod
	def empleados():
		
		empleados = []
		
		consulta = "SELECT documento FROM empleado ORDER BY apellido, nombre"
		
		Conexion.ejecutar(consulta)
		
		resultset = Conexion.fetchall()
		
		Conexion.cerrar()
		
		for item in resultset:
			
			e = Empleado.empleado(item[0])
			
			empleados.append(e)
		
		return empleados
	
	def guardar(self):
		
		if not self._cambios:
			return
		
		if self.documento == 0:
			raise Exception("El campo 'documento' no puede estar vacío.")
		
		if self.nombre == "":
			raise Exception("El campo 'nombre' no puede estar vacío.")
		
		if self.apellido == "":
			raise Exception("El campo 'apellido' no puede estar vacío.")
		
		if self.fecha_nacimiento == "":
			raise Exception("El campo 'fecha de nacimiento' no puede estar vacío.")
		
		if self.genero == "":
			raise Exception("El campo 'género' no puede estar vacío.")
		
		if self.domicilio == "":
			raise Exception("El campo 'domicilio' no puede estar vacío.")
		
		if self.fecha_ingreso == "":
			raise Exception("El campo 'fecha de ingreso' no puede estar vacío.")
		
		if self.nro_legajo == "":
			raise Exception("El campo 'número de legajo' no puede estar vacío.")
		
		if self.sit_revista == "":
			raise Exception("El campo 'situación de revista' no puede estar vacío.")
		
		if self.cargo == "":
			raise Exception("El campo 'cargo' no puede estar vacío.")
		
		dic  = {"a1" : "documento", 
				"a2" : "nombre", 
				"a3" : "apellido", 
				"a4" : "fecha_nacimiento", 
				"a5" : "genero", 
				"a6" : "domicilio", 
				"a7" : "telefono", 
				"a8" : "fecha_ingreso", 
				"a9" : "cuil", 
				"a10" : "nro_legajo", 
				"a11" : "sit_revista", 
				"a12" : "cargo", 
				"a13" : "observaciones", 
				}
		
		vals = {"v1" : self._documento, 
				"v2" : self._nombre, 
				"v3" : self._apellido, 
				"v4" : self._fecha_nacimiento, 
				"v5" : self._genero, 
				"v6" : self._domicilio, 
				"v7" : self._telefono, 
				"v8" : self._fecha_ingreso, 
				"v9" : self._cuil, 
				"v10" : self._nro_legajo, 
				"v11" : self._sit_revista, 
				"v12" : self._cargo, 
				"v13" : self._observaciones, 
				}
		
		if self._nuevo:
			
			consulta = "SELECT id FROM empleado WHERE documento = " + str(self.documento)
			
			Conexion.ejecutar(consulta)
			
			id_bbdd = Conexion.fetchone()
			
			Conexion.cerrar()
			
			if id_bbdd is not None:
				raise Exception("Ya existe un empleado con ese documento: " + str(self.documento))
			
			consulta = "INSERT INTO empleado('a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'a11', 'a12') \
						VALUES('v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v10', 'v11', 'v12', 'v13') RETURNING id"
			
			for i in range(1, 14):
				
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
			
			consulta = "SELECT id FROM empleado WHERE documento = " + str(self.documento)
			
			Conexion.ejecutar(consulta)
			
			resultset = Conexion.fetchone()
			
			Conexion.cerrar()
			
			if resultset is not None:
				for id_bbdd in resultset:
					if id_bbdd != self.id:
						print id_bbdd, "", self.id
						raise Exception("Ya existe un empleado con ese documento: ", self.documento)
						
			
			consulta = "UPDATE empleado SET 'a1' = 'v1',\
											'a2' = 'v2',\
											'a3' = 'v3',\
											'a4' = 'v4',\
											'a5' = 'v5',\
											'a6' = 'v6',\
											'a7' = 'v7',\
											'a8' = 'v8',\
											'a9' = 'v9',\
											'a10' = 'v10',\
											'a11' = 'v11',\
											'a12' = 'v12',\
											'a13' = 'v13'\
											WHERE id = " + str(self.id)
			
			for i in range(1, 14):
				
				consulta = consulta.replace("'a" + str(i) + "'", str(dic["a" + str(i)]))
				
				if isinstance(vals["v" + str(i)], int) or isinstance(vals["v" + str(i)], float):
					consulta = consulta.replace("'v" + str(i) + "'", str(vals["v" + str(i)]))
				else:
					if '/' in str(vals["v" + str(i)]):
						consulta = consulta.replace("'v" + str(i) + "'", "cast('" + str(vals["v" + str(i)]) + "' as date)")
					else:
						consulta = consulta.replace("'v" + str(i) + "'", "'" + str(vals["v" + str(i)]) + "'")
		
		Conexion.ejecutar(consulta)
		
		self._cambios = False
		
		if self._nuevo:
			self._id = Conexion.fetchone()[0]
			self._nuevo = False
		
		Conexion.cerrar()
	
	def eliminar(self):
		
		if self._nuevo:
			return
		
		if self.id == 0:
			return
		
		ls = Licencia.de_empleado(self._id)
		
		for l in ls:
			l.eliminar()
		
		consulta = "DELETE FROM empleado WHERE id = " + str(self.id)
		
		Conexion.ejecutar(consulta)
		
		Conexion.cerrar()
	
	"""GETTERS Y SETTERS..."""
	
	@property
	def id(self):
		return self._id
	
	@property
	def documento(self):
		return self._documento
	
	@documento.setter
	def documento(self, documento):
		
		if documento is None or (isinstance(documento, str) and documento == ""):
			raise Exception("El documento no puede estar vacío.")
		
		if isinstance(documento, str):
			try:
				documento = int(documento)
			except ValueError as ex:
				raise Exception("El número de documento posee caracteres no válidos: " + str(ex))
		
		if documento < 1000000 or documento > 99999999:
			raise Exception("El documento no está en rango del valores permitidos.")
		
		if self._documento != documento:
			self._documento = documento
			self._cambios = True
	
	@property
	def nombre(self):
		return self._nombre
	
	@nombre.setter
	def nombre(self, nombre):
		
		if not isinstance(nombre, str):
			raise Exception("El nombre tiene que ser una cadena de caracteres.")
		
		nombre_copia = nombre
		
		nombre = ""
		
		for n in nombre_copia.split(' '):
			
			if esalfa(n):
				nombre = nombre + " " + n.capitalize()
			else:
				raise Exception("El nombre posee caracteres no permitidos.")
		
		if nombre.startswith(' '):
			nombre = nombre[1:]
		
		if self._nombre != nombre:
			self._nombre = nombre
			self._cambios = True
		
	
	@property
	def apellido(self):
		return self._apellido
	
	@apellido.setter
	def apellido(self, apellido):
		
		if not isinstance(apellido, str):
			raise Exception("El apellido no es válido.")
		
		apellido_copia = apellido
		
		apellido = ""
		
		for a in apellido_copia.split(' '):
			
			if esalfa(a):
				apellido = apellido + " " + a.capitalize()
			else:
				raise Exception("El apellido posee caracteres no permitidos.")
		
		if apellido.startswith(' '):
			apellido = apellido[1:]
		
		if self._apellido != apellido:
			self._apellido = apellido
			self._cambios = True
		
	
	@property
	def fecha_nacimiento(self):
		return self._fecha_nacimiento
	
	@fecha_nacimiento.setter
	def fecha_nacimiento(self, fecha_nacimiento):
		
		if fecha_nacimiento is None or fecha_nacimiento == "":
			raise Exception("La fecha de nacimiento no puede estar vacía.")
		
		fecha_nacimiento = str(fecha_nacimiento)
		
		if fecha_nacimiento.find('-') != -1:
			
			anio, mes, dia = fecha_nacimiento.split('-')
			
			fecha_nacimiento = str(int(dia)) + '/' + str(int(mes)) + '/' + str(int(anio))
			
		if fecha_nacimiento.find('/') != -1:
			
			dia, mes, anio = fecha_nacimiento.split('/')
			
			datetime(int(anio), int(mes), int(dia))
			
			fecha_nacimiento = str(int(dia)) + '/' + str(int(mes)) + '/' + str(int(anio))
			
			if self._fecha_nacimiento != fecha_nacimiento:
				self._fecha_nacimiento = fecha_nacimiento
				self._cambios = True
		else:
			raise Exception("La fecha de nacimiento no cumple con el formato de una fecha.")
		
	@property
	def genero(self):
		return self._genero
	
	@genero.setter
	def genero(self, genero):
		
		if genero == "" or genero is None:
			raise Exception("El género no puede estar vacío.")
		
		genero = genero.capitalize()
		
		if genero == "Femenino":
			genero = 'F'
		elif genero == "Masculino":
			genero = 'M'
		
		if genero != 'F' and genero != 'M':
			raise Exception("El género no es valido.")
		
		if self._genero != genero:
			self._genero = genero
			self._cambios = True
	
	@property
	def domicilio(self):
		return self._domicilio
	
	@domicilio.setter
	def domicilio(self, domicilio):
		
		if domicilio is None:
			return
		
		if "\"" in domicilio:
			domicilio.replace("\"", "\\\"")
		
		if self._domicilio.capitalize() != domicilio.capitalize():
			self._domicilio = domicilio
			self._cambios = True
	
	@property
	def telefono(self):
		return self._telefono
	
	@telefono.setter
	def telefono(self, telefono):
		
		if telefono is None:
			telefono = ""
		
		if self._telefono != str(telefono):
			self._telefono = str(telefono)
			self._cambios = True
	
	@property
	def fecha_ingreso(self):
		return self._fecha_ingreso
	
	@fecha_ingreso.setter
	def fecha_ingreso(self, fecha_ingreso):
		
		if fecha_ingreso == "" or fecha_ingreso is None:
			raise Exception("La fecha de ingreso no puede estar vacía.")
		
		fecha_ingreso = str(fecha_ingreso)
		
		if fecha_ingreso.find('-') != -1:
			
			anio, mes, dia = fecha_ingreso.split('-')
			
			fecha_ingreso = str(int(dia)) + '/' + str(int(mes)) + '/' + str(int(anio))
			
		if fecha_ingreso.find('/') != -1:
			
			dia, mes, anio = fecha_ingreso.split('/')
			
			datetime(int(anio), int(mes), int(dia))
			
			fecha_ingreso = str(int(dia)) + '/' + str(int(mes)) + '/' + str(int(anio))
			
			if self._fecha_ingreso != fecha_ingreso:
				self._fecha_ingreso = fecha_ingreso
				self._cambios = True
		else:
			raise Exception("La fecha de ingreso no cumple con el formato de una fecha.")
	
	@property
	def cuil(self):
		return self._cuil
	
	@cuil.setter
	def cuil(self, cuil):
		
		if cuil is None or len(cuil) < 9:
			
			if self._cuil != cuil:
				self._cuil = cuil
				self._cambios = True
			
			return
		
		if cuil != "" and '-' in cuil:
			try:
				pre = cuil[:2]
				doc = cuil[3:11]
				suf = cuil[12:]
				
				if cuil[2] != '-' or cuil[11] != '-':
					raise
				
				if (int(doc) < 1000000 or int(doc) > 99999999) and self.documento != int(doc):
					cuil = ""
				
			except Exception as ex:
				raise Exception("El formato del número de cuil no es válido: " + str(cuil))
		else:
			raise Exception("El formato del número de cuil no es válido: " + str(cuil))
		
		if self._cuil != cuil or (cuil == "" and self._cuil != ""):
			self._cuil = cuil
			self._cambios = True
	
	@property
	def nro_legajo(self):
		return self._nro_legajo
	
	@nro_legajo.setter
	def nro_legajo(self, nro_legajo):
		
		if nro_legajo is None:
			raise Exception("El número de legajo no puede estar vacío.")
		
		if isinstance(nro_legajo, str):
			
			if not nro_legajo.isdigit():
				raise Exception("El número de legajo tiene caracteres no válidos.")
			
			nro_legajo = int(nro_legajo)
		
		if nro_legajo < 1:
			raise Exception("El número de legajo no puede ser menor a 1")
		
		if self._nro_legajo != nro_legajo:
			self._nro_legajo = nro_legajo
			self._cambios = True
	
	@property
	def sit_revista(self):
		return self._sit_revista
	
	@sit_revista.setter
	def sit_revista(self, sit_revista):
		
		if not isinstance(sit_revista, str):
			raise Exception("La situación de revista no puede estar vacía.")
		
		situaciones = ['Transitoria', 'Temporaria', 'Permanente',\
						'Pasantía', 'Comisión']
		
		if not sit_revista.capitalize() in situaciones:
			raise Exception("La situación de revista no corresponde a un valor disponible.")
		
		if sit_revista.capitalize() != self._sit_revista:
			self._sit_revista = sit_revista.capitalize()
			self._cambios = True
	
	@property
	def cargo(self):
		return self._cargo
	
	@cargo.setter
	def cargo(self, cargo):
		
		if not isinstance(cargo, str):
			raise Exception("El cargo no puede estar vacío.")
		
		cargos = ['Administrativo', 'Jerárquico', 'Obrero',\
					'Profesional', 'Servicio']
		
		if not cargo.capitalize() in cargos:
			raise Exception("El cargo no corresponde a un valor disponible.")
		
		if cargo.capitalize() != self._cargo:
			self._cargo = cargo.capitalize()
			self._cambios = True
	
	@property
	def observaciones(self):
		return self._observaciones
	
	@observaciones.setter
	def observaciones(self, observaciones):
		
		if not isinstance(observaciones, str):
			return
		
		if "\"" in observaciones:
			observaciones.replace("\"", "\\\"")
		
		observaciones = quitar_doble_espacios(observaciones)
		
		if self._observaciones.capitalize() != observaciones.capitalize():
			self._observaciones = observaciones
			self._cambios = True
	
