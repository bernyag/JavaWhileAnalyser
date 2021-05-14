# -*- coding: utf-8 -*-
import sys
from tokenizador import tokenizador
from automataPila import automataPila
from Sintax import sintaxAnalyzer
from contador import contador
#Lee el archivo desde la terminal
file = sys.argv[1]

tokenList=tokenizador(file)
if(automataPila(tokenList)&sintaxAnalyzer(tokenList)):
	print(contador(tokenList))
else:
	print("Este bloque no es sintacticamente correcto")

