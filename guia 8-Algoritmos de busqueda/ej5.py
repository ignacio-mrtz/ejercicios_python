# Ejercicio 8.5. Escribir una función que reciba una lista ordenada y un elemento. Si el elemento
# se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverlo. Si
# no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición.
# (No utilizar lista.sort().)

def main(lista_ordenada, elemento):
    izq=0
    der=len(lista_ordenada)-1
    while der>=izq:
        medio=(der+izq)//2
        if lista_ordenada[medio]==elemento:
            return medio
        if lista_ordenada[medio]>elemento:
            der=medio-1
        else:
            izq=medio+1
    lista_ordenada.insert(medio,elemento)
    return medio

lista_ordenada=[1,3,4,5,6,9]
print(main(lista_ordenada,2))
print(lista_ordenada)



