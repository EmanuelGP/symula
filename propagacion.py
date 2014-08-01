"""
Proyecto:	'SYMULA'
Autor:		Emanuel GP
Modulo:		Propagacion
"""

def suma_ponderada(umbral, entrada, pesos):
	potencial = 0.0
	for i in range(len(pesos)):
		potencial += pesos[i] * entrada[i]
	potencial += umbral
	return potencial