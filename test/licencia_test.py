#! /usr/bin/python
# coding=utf-8

import time
from m.licencia import Licencia

def main():
	
	#~ ls = Licencia.de_empleado(2, "Enfermedad")
	l = Licencia(51)
	
	l.id_empleado = 6
	l.desde = "10/5/2014"
	l.hasta = "1/5/2014"
	l.tipo = "58"
	l.comentario = ""
	
	l.guardar()
	
	
	#~ for l in ls:
	print l._id
	print l.id_empleado
	print l.desde
	print l.hasta
	print l.tipo
	print l.dias_tomados
	print l.comentario
	
	return 0

if __name__ == '__main__':
	exit(main())
