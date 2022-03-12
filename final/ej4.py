# Ejercicio 4 Implementar la función intercambiar_diagonales(m) que recibe una matriz cuadrada
# (implementada como listas de listas), y devuelve una copia de la matriz intercambiando los
# elementos de ambas diagonales. Por ejemplo, para una matriz de 3x3:


def intercambiar_diagonales(m):
    # HACER: implementar
    l=len(m)
    copia=[]
    for f in m:
        copia.append(f[:])
    cant=1
    for fila in copia:
        fila[l-cant],fila[cant-1]=fila[cant-1],fila[l-cant]
        cant+=1
        if cant==l+1:
            return copia

def pruebas():
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    m2 = intercambiar_diagonales(m)
    assert m2 == [
        [3, 2, 1],
        [4, 5, 6],
        [9, 8, 7],
    ]

    # OPCIONAL: escribir pruebas adicionales
    j = [
        [1, 2, 3, 9],
        [4, 5, 6, 8],
        [7, 8, 9, 0],
        [7, 8, 9, 0]
    ]
    j2 = intercambiar_diagonales(j)
    assert j2 == [
        [9, 2, 3, 1],
        [4, 6, 5, 8],
        [7, 9, 8, 0],
        [0, 8, 9, 7]
    ]

    p = [
        [0, 2],
        [1, 3],
    ]
    p2 = intercambiar_diagonales(p)
    assert p2 == [
        [2, 0],
        [3, 1],
    ]

    assert not(p is p2)

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()

