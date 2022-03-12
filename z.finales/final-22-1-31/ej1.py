#Escribir la función aplastar(lista) que recibe una lista cuyos elementos pueden ser
#números o listas (que a su vez pueden contener números o listas...), y devuelve una lista con
#todos los números encontrados. Por ejemplo:
#aplastar([[1], [2, [3]], 4, [3, [2, 4]]]) -> [1, 2, 3, 4, 3, 2, 4]
#Sugerencia: pensar el problema en forma recursiva.
#Nota: se puede usar type(x) is list para averiguar si un valor es una lista o no.

def aplastar(lista):
    # HACER: implementar en forma RECURSIVA
    lista_aplastada=[]
    return _aplastar(lista,lista_aplastada)

def _aplastar(lista,lista_aplastada):
    if type(lista) is not list:
        return lista_aplastada+[lista]
    for e in lista:
        lista_aplastada=_aplastar(e,lista_aplastada)
    return lista_aplastada
        
def pruebas():
    print(aplastar([[1], [2, [3]], 4, [3, [2, 4]]]))
    assert(aplastar([[1], [2, [3]], 4, [3, [2, 4]]])) == [1, 2, 3, 4, 3, 2, 4]

    # OPCIONAL: Pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
