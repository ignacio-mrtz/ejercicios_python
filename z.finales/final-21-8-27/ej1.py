def union(a, b):
    # HACER: implementar en forma RECURSIVA

def pruebas():
    assert(union([1, 3, 5, 7], [2, 3, 6, 7]) == [1, 2, 3, 5, 6, 7])

    # OPCIONAL: Pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
