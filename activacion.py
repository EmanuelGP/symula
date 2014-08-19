"""
Proyecto:	'SYMULA'
Autor:		Emanuel GP
Modulo:		Activacion
"""

import math

def activacion_identidad(potencial):
	"""Funcion de Transferencia Identidad Lineal"""
	return potencial

def activacion_hardlim(potencial):
	"""Funcion de Transferencia Escalon Binario"""
	if potencial > 0.0:
		return 1.0
	else:
		return 0.0

def activacion_hardlims(potencial):
	"""Funcion de Transferencia Escalon Bipolar"""
	if potencial > 0.0:
		return 1.0
	else:
		return -1.0

def activacion_logistica(potencial):
	"""Funcion de Transferencia Logistica"""
	return (1.0 / (1.0 + (math.pow(math.e, -potencial))))

def activacion_tangente(potencial):
	"""Funcion de Transferencia Tangente Sigmoidea"""
	return ((2.0 / (1.0 + (1.0 + (math.pow(math.e, -potencial))))) - 1.0)

def activacion_hiperbolica(potencial):
	"""Funcion de Transferencia Tangente Hiperbolica"""
	return ((math.pow(math.e, potencial)) - ((math.pow(math.e, -potencial)))) / ((math.pow(math.e, potencial)) + ((math.pow(math.e, -potencial))))
