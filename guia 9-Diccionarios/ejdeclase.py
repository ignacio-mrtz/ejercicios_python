#Escribir una funcion que reciba 2 listas con palabras y determine si ambas listas tienen las mismas palabras

import ej2

def tienen_mismas_palabras(lista1, lista2):
    diccionario1 = ej2.contar_palabras_2(lista1)
    diccionario2 = ej2.contar_palabras_2(lista2)
    return diccionario1==diccionario2

a=["hola", "como", "estas","todo","bien","bien"]
b=["bien", "hola", "como", "estas","todo"]


print(tienen_mismas_palabras(a,b))

