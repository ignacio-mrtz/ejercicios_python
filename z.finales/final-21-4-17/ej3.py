
def interseccion(a, b):
    # HACER: implementar la funcion

def pruebas():
    assert interseccion([2],          [3])          == []
    assert interseccion([2],          [2])          == [2]
    assert interseccion([2, 2],       [2])          == [2]
    assert interseccion([2, 2],       [2, 2])       == [2, 2]
    assert interseccion([1, 2, 2, 4], [1, 2, 2, 3]) == [1, 2, 2]

    # OPCIONAL: pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
