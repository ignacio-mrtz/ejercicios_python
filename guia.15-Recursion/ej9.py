# Ejercicio 15.9. Escribir una función recursiva para replicar los elementos de una lista una cantidad n de veces. Por ejemplo:
# replicar([1, 3, 3, 7], 2) -> ([1, 1, 3, 3, 3, 3, 7, 7])

def _replicar(lista, n, indice):
    if indice == len(lista):
        return []
    return [lista[indice]] * n + _replicar(lista, n, indice + 1)

def replicar(lista,n):
    _replicar(lista,n,0)
    

#otro ejercicio

def _contar_apariciones(lista, elemento, indice):
    if len(lista) == indice:
        return 0
    return _contar_apariciones(lista, elemento, indice + 1) + (0 if elemento != lista[indice] else 1)

def contar_apariciones(lista, elemento):
    return _contar_apariciones(lista, elemento, 0)