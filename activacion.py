"""
Proyecto:	'SYMULA'
Autor:		Emanuel GP
Modulo:		Activacion
"""

import math

def identidad(potencial):
	"""Funcion de Transferencia Identidad Lineal"""
	return potencial

def hardlim(potencial):
	"""Funcion de Transferencia Escalon Binario"""
	if potencial > 0.0:
		return 1.0
	else:
		return 0.0

def hardlims(potencial):
	"""Funcion de Transferencia Escalon Bipolar"""
	if potencial > 0.0:
		return 1.0
	else:
		return -1.0

def logistica(potencial):
	"""Funcion de Transferencia Logistica"""
	return (1.0 / (1.0 + (math.pow(math.e, -potencial))))

def tangente(potencial):
	"""Funcion de Transferencia Tangente Sigmoidea"""
	return ((2.0 / (1.0 + (1.0 + (math.pow(math.e, -potencial))))) - 1.0)

def hiperbolica(potencial):
	"""Funcion de Transferencia Tangente Hiperbolica"""
	return ((math.pow(math.e, potencial)) - ((math.pow(math.e, -potencial)))) / ((math.pow(math.e, potencial)) + ((math.pow(math.e, -potencial))))
