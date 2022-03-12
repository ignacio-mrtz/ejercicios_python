
#
# HACER: implementar la funcion
#

def pruebas():
    assert multi_merge([[1, 3, 5, 7, 9], [2, 4, 6, 8]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # OPCIONAL: agregar más casos de prueba. Sugerencias: probar distintos valores de k,
    # y listas de diferentes longitudes (no tienen por qué ser todas de la misma longitud).

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
