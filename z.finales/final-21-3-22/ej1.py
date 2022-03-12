
def transponer(m):
    # HACER: implementar la funcion

def pruebas():
    m = [
        [1, 2],
        [3, 4],
        [5, 6],
    ]

    mt = transponer(m)

    assert mt == [
        [1, 3, 5],
        [2, 4, 6],
    ]

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
