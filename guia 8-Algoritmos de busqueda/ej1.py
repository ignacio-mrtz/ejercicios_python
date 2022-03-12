# Ejercicio 8.1. Escribir una función que reciba una lista desordenada y un elemento, que:
# a) Busque todos los elementos que coincidan con el pasado por parámetro y devuelva la cantidad
# de coincidencias encontradas.
# b) Busque la primera coincidencia del elemento en la lista y devuelva su posición.
# c) Utilizando la función anterior, busque todos los elementos que coincidan con el pasado
# por parámetro y devuelva una lista con las posiciones.

def main_a(lista_desordenada, elemento):
    contador=0
    for x in lista_desordenada:
        if x==elemento:
            contador+=1
    return contador

def main_b(lista,elemento):
    for i,x in enumerate(lista):
        if x==elemento:
            return i
    return -1


def main_c(lista,elemento):
    posiciones_coincidencias=[]
    for i,x in enumerate(lista):
        if x==elemento:
            posiciones_coincidencias.append(i)
    return posiciones_coincidencias

#print(main_c([9,8,7,3,2,4,67,8,1,5,93,7,94,3,5,75,36,2,573,2],2))




