# Ejercicio 7.10. Matrices.
# a) Escribir una función que reciba dos matrices y devuelva la suma.
# b) Escribir una función que reciba dos matrices y devuelva el producto.
# c) ⋆ Escribir una función que opere sobre una matriz y mediante eliminación gaussiana devuelva
# una matriz triangular superior.
# d) ⋆ Escribir una función que indique si un grupo de vectores, recibidos mediante una
# lista, son linealmente independientes o no.

def suma_de_matrices(matriz1,matriz2):
    if len(matriz1)==len(matriz2) and len(matriz1[1])==len(matriz2[1]):
        matriz_resultante=[]
        for i in range(0,len(matriz1)):
            matriz_resultante.append([])
            for j in range(0,len(matriz1[1])):
                suma=matriz1[i][j] + matriz2[i][j]
                matriz_resultante[i].append(suma)
    else:
        return
    return matriz_resultante

#print(suma_de_matrices([[1,2], [3,4], [5,6]],  [[9,8], [7,6], [5,4]]))

#resolucion de clase:

def sumar_matrices(m1, m2):
    # Chequear que se puedan sumar
    res = tuple()
    for i in range(len(m1)):
        fila = m1[i]
        nueva_fila = tuple()
        for j in range(len(fila)):
            nueva_fila = nueva_fila + (m1[i][j] + m2[i][j], )
        res += (nueva_fila, )
    return res

def imprimir_matriz(m):
    for fila in m:
        for e in fila:
            print(e, end="\t")
        print()

m1 = [[4,1,4], [8,7,1]] # 2x3
m2 = [[1,2,0], [4,5,6]] # 2x3

#imprimir_matriz(sumar_matrices(m1, m2))

#------------------------------------------------------------------------------------
