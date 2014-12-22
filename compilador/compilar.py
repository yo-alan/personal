#! /usr/bin/python
# coding=utf-8

from directorio import Compilador

def main():
	
	fuente = "/home/alan/Escritorio/python/MVC"
	destino = "/home/alan/Escritorio/python/Personal"
	ignorar = "/home/alan/Escritorio/python/MVC/compilador/ignorar"
	
	c = Compilador(fuente, destino, ignorar)
	
	return c.actualizar()

if __name__ == '__main__':
	exit(main())
