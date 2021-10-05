# Ejercicio 7.1. Escribir una función que reciba una tupla de elementos e indique si se encuentran
# ordenados de menor a mayor o no.

def ordenados_de_menor_a_mayor(tupla):
    copia_de_tupla=list(tupla)
    copia_de_tupla.sort()
    if tuple(copia_de_tupla)==tupla:
        print("ordenada de menor a mayor")
    else:
        print("desordenada")


ordenados_de_menor_a_mayor((1,3,5,6))