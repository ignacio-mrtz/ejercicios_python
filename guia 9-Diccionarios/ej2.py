# Ejercicio 9.2. Diccionarios usados para contar.

# a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
# de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
# hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.

import random

def contar_palabras(cadena):
    copia_cadena=cadena.lower()
    lista=copia_cadena.split()
    diccionario={}
    for palabra in lista:
        if palabra in diccionario:
            diccionario[palabra]=diccionario[palabra]+1
        else:
            diccionario[palabra]=1
    return diccionario

cadena="Que lindo día que hace hoy"
#print(contar_palabras(cadena))

def contar_palabras_2(lista):
    diccionario={}
    for palabra in lista:
        diccionario[palabra] = diccionario.get(palabra,0) + 1
    return diccionario

lista=["hola", "como", "estas","todo","bien"]
#print(contar_palabras_2(cadena))

# b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena
# de texto, y los devuelva en un diccionario.

def main_b(cadena):
    diccionario={}
    for x in cadena:
        if diccionario.get(x, ''):
            diccionario[x]=diccionario[x]+1
        else:
            diccionario[x]=1
    return diccionario

#print(main_b(cadena))

def main_b_2(cadena):
    diccionario={}
    for letra in cadena:
        diccionario[letra] = diccionario.get(letra,0) + 1
    return diccionario

#print(main_b_2(cadena))

# c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
# realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos
# dados.
# Nota: utilizar el módulo random para obtener tiradas aleatorias.

def main_c(iteraciones):
    diccionario={}
    for i in range(0,iteraciones):
        dado1=random.randint(0,6)
        dado2=random.randint(0,6)

        diccionario[dado1+dado2] = diccionario.get(dado1+dado2,0) + 1 

    return diccionario

#print(main_c(5))


