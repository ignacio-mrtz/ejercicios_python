# Ejercicio 6.1. Escribir funciones que dada una cadena de caracteres:
# a) Imprima los dos primeros caracteres.
# b) Imprima los tres últimos caracteres.
# c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
# d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
# e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
# 'reflejoojelfer'.

def imprimir_dos_primeros_caracteres(string):
    print(string[0:2])

#imprimir_dos_primeros_caracteres("anfkndgklnag")

def imprimir_tres_ultimos_caracteres(string):
    print(string[-3:])

#imprimir_tres_ultimos_caracteres("dhadhfhfghkuy")

def imprimir_cada_dos_caracteres(string):
    print(string[::2])

#imprimir_cada_dos_caracteres("0123456789")}

def imprimir_sentido_normal_e_inverso(string):
    print(string+string[::-1])

def imprimir_sentido_normal_e_inverso2(string):
    print(string+string[::-1])

#imprimir_sentido_normal_e_inverso2("hola")
