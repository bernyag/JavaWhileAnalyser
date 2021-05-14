#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from tokenizador import tokenizador
from automataPila import automataPila
from Sintax import sintaxAnalyzer
from contador import contador

# Lee el archivo desde la terminal
file = sys.argv[1]

# lo convierte a una lista de tokens
tokenList = tokenizador(file)

# verifica si los whiles están bien aninados y si la sintaxis dentro del while es correcta
if automataPila(tokenList) and sintaxAnalyzer(tokenList):

	# imprime las estadisticas
	contador(tokenList)
	print ("\nEl bloque es valido")

else:
	print("Este bloque no es sintacticamente correcto")