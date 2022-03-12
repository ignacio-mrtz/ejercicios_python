
#Escribir la función patron_tablero(n, k) (con 𝑘 < 𝑛), que devuelve una matriz de
#𝑛 × 𝑛 ceros y unos, formando un patrón de tablero de ajedrez donde cada casillero es de
#tamaño 𝑘 × 𝑘.
#Ejemplo: patron_tablero(10, 3):
#0001110001
#0001110001
#0001110001
#1110001110
#1110001110
#1110001110
#0001110001
#0001110001
#0001110001
#1110001110


def patron_tablero(n, k):
    # HACER: implementar
    matriz=[]
    for i in range(n):
        matriz.append([])
        


def pruebas():
    assert patron_tablero(10, 3) == [
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
    ]

    # OPCIONAL: escribir pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
