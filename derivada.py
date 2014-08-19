"""
Proyecto:	'SYMULA'
Autor:		Emanuel GP
Modulo:		Derivada
"""

import math
import activacion

def derivada_identidad(potencial):
	return 1.0

def derivada_logistica(potencial):
	return (activacion_logistica(potencial) * (1 - activacion_logistica(potencial)))

def derivada_tangente(potencial):
	return ((2*(math.pow(math.e, -potencial))) / math.pow((1.0 + (math.pow(math.e, -potencial))), 2))