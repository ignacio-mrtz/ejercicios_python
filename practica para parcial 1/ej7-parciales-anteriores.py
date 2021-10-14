# Del primer parcialito, segundo cuatrimestre de 2017
# 3) Escribir una funcion que dada una matriz representada como una lista de listas de
# numeros (donde cada sublista representa una fila), devuelva una lista con los maximos de cada
# columna. Ejemplo:
# maximos_columnas([[1, 2, 8, 4],
                   #[6, 7, 3, 3], -> [6, 7, 8, 9]
                   #[6, 5, 4, 9]])

def maximo_columnas(matriz):
    lista_maximos=[]
    for j in range(0,len(matriz[1])):
        maximo=matriz[0][j]
        for i in range(0,len(matriz)):
            if matriz[i][j]>=maximo:
                maximo=matriz[i][j]
        lista_maximos.append(maximo)
    return lista_maximos

print(maximo_columnas([[1, 2, 8, 4], [6, 7, 3, 3], [6, 5, 4, 9]]))
            


