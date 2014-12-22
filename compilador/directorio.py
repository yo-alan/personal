#! /usr/bin/python
# coding=utf-8

import os
import time
import filecmp
import py_compile
import shutil
from logger import log

class Compilador(object):
	
	directorioFuente = ""
	directorioDestino = ""
	ignorar = ""
	
	archivos = []
	
	def __init__(self, directorioFuente, directorioDestino, ignorar):
		self.directorioFuente = directorioFuente
		self.directorioDestino = directorioDestino
		self.ignorar = ignorar
	
	@staticmethod
	def camino(ruta):
		
		if os.path.isfile(ruta):
			Compilador.archivos.append(ruta)
		elif os.path.isdir(ruta):
			Compilador.archivos.append(ruta + "/")
			for item in os.listdir(ruta):
				Compilador.camino(ruta + "/" + item)
		else:
			raise Exception("No pude validar el directorio: '" + ruta + "'.")
	
	def comodin(self, criterio):
		
		criterio = criterio[1:]
		
		a = self.archivos[:]
		for i in a:
			if i.endswith(criterio):
				self.archivos.remove(i)
	
	def actualizar(self, ):
		
		if self.directorioFuente.endswith('/'):
			self.directorioFuente = self.directorioFuente[ : len(self.directorioFuente) - 1]
		
		if self.directorioDestino.endswith('/'):
			self.directorioDestino = self.directorioDestino[ : len(self.directorioDestino) - 1]
		
		Compilador.camino(self.directorioFuente)
		
		self.compilar()
		
		archivoIgnorar = []
		
		try:
			archivo = open(self.ignorar, "r+")
			
			archivoIgnorar = archivo.read().split('\n')
			
			archivo.close()
		except Exception as e:
			raise Exception("No pude determinar los archivos a ignorar: " + str(e))
		
		ai = archivoIgnorar[:]
		for a in ai:
			if a == '':
				archivoIgnorar.remove(a)
		
		for i in archivoIgnorar:
			
			if "*" in i:
				log("Ignoro con este patron: '" + i + "'")
				self.comodin(i)
			elif self.directorioFuente + "/" + i in self.archivos:
				
				if i.endswith('/'):
					copia = self.archivos[:]
					for a in copia:
						if "/" + i in a:
							log("Ignoro: '" + a + "'")
							self.archivos.remove(a)
				else:
					log("Ignoro: '" + i + "'")
					self.archivos.remove(self.directorioFuente + "/" + i)
			else:
				log("No esta: " + self.directorioFuente + "/" + i)
		
		for archivo in self.archivos:
			
			archivoViejo = archivo.replace(self.directorioFuente, self.directorioDestino)
			
			if os.path.isdir(archivo):
				
				if not os.path.isdir(archivoViejo):
					log("Carpeta nueva: '" + archivoViejo + "'")
					os.mkdir(archivoViejo)
				
				continue
			
			sincambios = False
			esArchivoNuevo = True
			if os.path.isfile(archivoViejo):
				
				if os.path.isfile(archivo) and filecmp.cmp(archivo, archivoViejo):
					log("Sin cambios: '" + archivoViejo + "'")
					sincambios = True
				else:
					esArchivoNuevo = False
					os.remove(archivoViejo)
			
			if not sincambios:
				
				destino = os.path.dirname(archivoViejo)
				
				if esArchivoNuevo:
					log("Archivo nuevo: '" + os.path.basename(archivo) + "' en '" + destino + "'")
				else:
					log("Archivo actualizado: '" + os.path.basename(archivo) + "' en '" + destino + "'")
				
				shutil.copy(archivo, destino)
				
			if archivo.endswith(".pyc"):
				os.remove(archivo)
		
		return 0

	def compilar(self, ):
		
		copia = self.archivos[:]
		
		for a in copia:
			if a.endswith('.py'):
				log("Compilo: " + str(a))
				py_compile.compile(str(a))
				
				partes = a.split(' ')
				a = ""
				for sep in partes:
					a = a + sep + "\\ "
				
				a = a[:-2]
				
				self.archivos.append(str(a) + "c")
