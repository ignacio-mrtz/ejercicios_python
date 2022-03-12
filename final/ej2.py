# Ejercicio 2 Implementar en forma recursiva la función range(a, b, paso), que produce una lista
# de números con un comportamiento similar a la función range de Python, soportando al menos
# los siguientes casos:
# range(1, 7, 1) -> [1, 2, 3, 4, 5, 6]
# range(1, 7, 2) -> [1, 3, 5]
# range(7, 1, 1) -> []
# range(7, 1, -3) -> [7, 4]

def range(a, b, paso):
    # HACER: implementar en forma RECURSIVA
    lista=[]
    return _range(a,b,paso,lista)
    
def _range(a,b,paso,lista):
    if a==b or b-a<0 and paso>0 or b-a>0 and paso<0:
        return lista
    lista=[a] + _range(a+paso,b,paso,[])
    return lista


def pruebas():
    assert range(1, 7, 1) == [1, 2, 3, 4, 5, 6]
    assert range(1, 7, 2) == [1, 3, 5]
    assert range(7, 1, 1) == []
    assert range(7, 1, -3) == [7, 4]

    # OPCIONAL: escribir pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()

