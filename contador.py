#!/usr/bin/env python
# -*- coding: utf-8 -*-

def contador(tokens):
    '''
        Función para contar los distintos elementos dentro de los tokens.
        Imprime los resultados de los contadores.

        input: lista de tokens del bloque
        output: contador de whiles, contador de variables y contador de operadores
    '''

    #contar cada token y guardarlo en un diccionario
    dict_tokens = {}
    for token in tokens:
        if token in dict_tokens:
            dict_tokens[token] += 1
        else:
            dict_tokens[token] = 1

    #variable para contar whiles
    whiles_count = 0
    whiles_count = dict_tokens['while']

    #variable para contar variables
    var_names = 'abcdefghijklmnñopqrstuvwxyz'
    variables = []
    variables_count = 0
    for letter in var_names:
        if letter in dict_tokens:
            variables.append(letter)
            variables_count += 1

    #variable para contar operadores
    operadores_count = 0
    if '>' in dict_tokens:
        operadores_count += dict_tokens['>']
    if '<' in dict_tokens:
        operadores_count += dict_tokens['<']
    if '==' in dict_tokens:
        operadores_count += dict_tokens['==']

    print("\nNúmero total de ciclos while: ", whiles_count)
    print("\nNúmero total de variables: ", variables_count)
    print("\tVariables: ", variables)
    print("\nNúmero total de operadores: ", operadores_count)

    #return(whiles_count, variables_count, operadores_count)


'''
Pruebas
tokens = ['while','(', 'x', '<', 'y', ')', '{', 'while', '}']
print(contador(tokens))
'''