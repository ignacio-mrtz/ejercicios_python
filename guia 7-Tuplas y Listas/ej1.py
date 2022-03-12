# Ejercicio 7.1. Escribir una función que reciba una tupla de elementos e indique si se encuentran
# ordenados de menor a mayor o no.

def ordenados_de_menor_a_mayor(tupla):
    copia_de_tupla=list(tupla)
    copia_de_tupla.sort()
    if tuple(copia_de_tupla)==tupla:
        print("ordenada de menor a mayor")
    else:
        print("desordenada")

#ordenados_de_menor_a_mayor((1,3,5,6))

# o tmb:

def tupla_ordenada(tupla):
    copia=list(tupla)
    for i in range(0,len(copia)-1):
        if copia[i]>copia[i+1]:
            return False
    return True

print(tupla_ordenada((1,3,5,7)))