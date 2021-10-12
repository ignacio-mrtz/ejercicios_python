# Escribir una función que reciba una matriz cuadrada (lista de listas), cuyos elementos son números, y que devuelva # la cantidad de elementos en el triángulo superior de la matriz que sean negativos.
# 
# Nota: el triángulo superior de una matriz abarca la diagonal principal, y todo lo que esté por arriba de ella.
# 
# Ejemplo: si la función recibe la matriz:
# 
# [
#     [0, 1, -3],
#     [0, -4, 5],
#     [-9, 8, 1],
# ]
# Entonces debe devolver 2, pues el triángulo superior está compuesto por los números 0, 1, -3, -4, 5 y 1.

def cant_negativos_triangulo_sup(matriz):
    '''recibe una matriz cuadrada (lista de listas), cuyos elementos son números, y devuelve la cantidad de elementos en el triángulo superior de la matriz que sean negativos. el triángulo superior de una matriz abarca la diagonal principal, y todo lo que esté por arriba de ella.'''
    contador=0
    e=0
    for i in range(0,len(matriz)):
        for j in range(e,len(matriz)):
            if matriz[i][j]<0:
                contador+=1
        e+=1
    return contador

print(cant_negativos_triangulo_sup([
    [0, 1, -3],
    [0, -4, 5],
    [-9, 8, 1],
]))