#Escribir una funcion que reciba 2 listas con palabras y determine si ambas listas tienen las mismas palabras

import ej2

def tienen_mismas_palabras(lista1, lista2):
    diccionario1 = ej2.contar_palabras_2(lista1)
    diccionario2 = ej2.contar_palabras_2(lista2)
    return diccionario1==diccionario2

a=["hola", "como", "estas","todo","bien","bien"]
b=["bien", "hola", "como", "estas","todo"]


print(tienen_mismas_palabras(a,b))

#a mano:

def iguales(lista1, lista2):
    return incluido(lista1, lista2) and incluido(lista2, lista1) 

def incluido(lista1, lista2):
    for clave, valor in d1.items():
        if clave not in lista2:
            return False
        if lista2[clave] != lista1[clave]:
            return False
    return True
        


