# Ejercicio 9.2. Diccionarios usados para contar.
# a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
# de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
# hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.
# b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena
# de texto, y los devuelva en un diccionario.
# c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
# realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos
# dados.
# Nota: utilizar el módulo random para obtener tiradas aleatorias.
import random

def main_a(cadena):
    copia_cadena=cadena.lower()
    lista=copia_cadena.split()
    diccionario={}
    for x in lista:
        if diccionario.get(x, ''):
            numero_anterior=diccionario[x].pop()
            diccionario[x]=[numero_anterior+1]
        else:
            diccionario[x]=[1]
    return diccionario

cadena="Qué lindo día que hace hoy"
#print(main_a(cadena))

def main_b(cadena):
    diccionario={}
    for x in cadena:
        if diccionario.get(x, ''):
            numero_anterior=diccionario[x].pop()
            diccionario[x]=[numero_anterior+1]
        else:
            diccionario[x]=[1]
    return diccionario

#print(main_b(cadena))

# c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
# realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos
# dados.

def main_c(iteraciones):
    diccionario={}
    for i in range(0,iteraciones):
        dado1=random.randint(0,6)
        dado2=random.randint(0,6)

        if diccionario.get(dado1+dado2, ''):
            numero_anterior=diccionario[dado1+dado2].pop()
            diccionario[dado1+dado2]=[numero_anterior+1]
        else:
            diccionario[dado1+dado2]=[1]
    return diccionario

print(main_c(5))


