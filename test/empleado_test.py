#! /usr/bin/python
# coding=utf-8

from m.empleado import Empleado

def main():
	
	e = Empleado()
	
	e.documento = 25083157
	e.nombre = "guadalupe"
	e.apellido = "fania"
	e.fecha_nacimiento = "10/3/1976"
	e.genero = "f"
	e.domicilio = "cordoba 716"
	e.fecha_ingreso = "1/1/2008"
	e.cuil = "27-25083157-9"
	e.nro_legajo = 105
	e.sit_revista = "transitoria"
	e.cargo = "servicio"
	
	e.guardar()
	
	print "ID:", e.id
	print "DOCUMENTO:", e.documento
	print "NOMBRE:", e.nombre
	print "APELLIDO:", e.apellido
	print "FECHA DE NACIMIENTO:", e.fecha_nacimiento
	print "GENERO:", e.genero
	print "DOMICILIO:", e.domicilio
	print "TELEFONO:", e.telefono
	print "FECHA DE INGRESO:", e.fecha_ingreso
	print "CUIL:", e.cuil
	print "NRO DE LEGAJO:", e.nro_legajo
	print "SITUACION REVISTA:", e.sit_revista
	print "CARGO:", e.cargo
	
	return 0

if __name__ == '__main__':
	exit(main())
