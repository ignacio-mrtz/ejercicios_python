# Escribir una función que reciba una lista de tuplas de la forma (n, m) y devuelva dos listas.
# 
# La primera tendrá los elementos de la primer posicion de las tuplas
# La segunda, los que estén en la segunda posición.
# Ejemplo:
# 
# >>> partir_tuplas([(1,2),(1,2),(1,2),(8,9)]
# ([1,1,1,8],[2,2,2,9])

def partir_tuplas(lista):
    lista1=[]
    lista2=[]
    for i in range(0, len(lista)):
        lista1.append(lista[i][0])
        lista2.append(lista[i][1])
    return lista1,lista2



print(partir_tuplas([(1,2),(1,2),(1,2),(8,9)]))

#o tmb:

def partir_tuplas2(lista):
    '''Recibe una lista cuyos elementos son tuplas de dos elementos
    y genera dos listas, una con los primeros elementos de las tuplas,
    y otra con los segundos elementos de las mismas'''
    lista_n, lista_m = [], []
    for elemento in lista:
        lista_n.append(elemento[0])
        lista_m.append(elemento[1])
    return lista_n, lista_m