import random

DIMENSION_MATRIZ = 4
NRO_FINAL = 2048
VALORES_ALEATORIOS = [2,4]
TECLAS_UTILIZADAS = ["w", "s", "a" , "d"]# 1er elemento: arriba, 2do: abajo, 3ero: izquierda, 4to: derecha

def inicializar_juego():
    """crea una matriz cuadrada vacía de la dimension asignada en DIMENSION_MATRIZ y elige 2 veces al azar algun numero de la lista VALORES_ALEATORIOS """
    matriz = []
    for i in range(DIMENSION_MATRIZ):
        matriz.append([])
        for j in range(DIMENSION_MATRIZ):
            matriz[i].append("")

    contador=0
    while True:
        if contador==2:
            break;
        i=random.randint(0,DIMENSION_MATRIZ-1)
        j=random.randint(0,DIMENSION_MATRIZ-1)
        if matriz[i][j]=="":
            matriz[i][j]= random.choice(VALORES_ALEATORIOS)
            contador+=1
    return matriz


def mostrar_juego(matriz):
    """imprime la matriz en la terminal"""
    for i in range(0,DIMENSION_MATRIZ):
        for j in range(0, DIMENSION_MATRIZ):
            if j== DIMENSION_MATRIZ -1:
                print(f'\t{matriz[i][j]}')
                print(DIMENSION_MATRIZ * "................")
            else:
                print (f'\t{matriz[i][j]}\t',"|", end=" ")


def juego_ganado(matriz):
    """busca si el nro final se encuentra en la matriz. si lo encuentra devuelve True y el usuario gana el juego"""
    for i in range(0, DIMENSION_MATRIZ):
        if NRO_FINAL in matriz[i]:
            return True
    return False

def juego_perdido(matriz):
    """identifica si hay 2 nros iguales uno al lado del otro y si el tablero tiene algun lugar vacío. Si no sucede ninguna de las dos, devuelve True y el usuario pierde el juego"""
    for i in range (0, DIMENSION_MATRIZ):
        for j in range (0, DIMENSION_MATRIZ-1):
            if matriz[i][j] == matriz[i][j+1] or matriz[j][i] == matriz[j+1][i] or matriz[i][j] == "":
                return False
        if matriz[i][DIMENSION_MATRIZ-1] == "": # Esto es lo unico que se pondría separado, porque los ciclos verifican todas menos la ultima casilla de cada fila.
            return False
    return True

def pedir_direccion(matriz):
    while True:
        direccion = input(f'Elegí una dirección,{TECLAS_UTILIZADAS}: ')
        if direccion in TECLAS_UTILIZADAS:
            break;
    return direccion

def actualizar_juego(matriz, dir):
    """hace una copia de la matriz y la actualiza segun la dirección ingresada por el usuario"""
    copia_matriz = []
    for i in range (0,DIMENSION_MATRIZ):
        copia_matriz.append(matriz[i][:])

    if dir == TECLAS_UTILIZADAS[0]:
        transponer_matriz(copia_matriz)
        combinar_filas(copia_matriz)
        transponer_matriz(copia_matriz)

    elif dir == TECLAS_UTILIZADAS[1]:
        transponer_matriz(copia_matriz)
        invertir_filas(copia_matriz)
        combinar_filas(copia_matriz)
        invertir_filas(copia_matriz)
        transponer_matriz(copia_matriz)

    elif dir == TECLAS_UTILIZADAS[2]:
        combinar_filas(copia_matriz)

    elif dir == TECLAS_UTILIZADAS[3]:
        invertir_filas(copia_matriz)
        combinar_filas(copia_matriz)
        invertir_filas(copia_matriz)

    return copia_matriz
    

def insertar_nuevo_random(matriz):
    """recibe la copia actualizada de la matriz y le ingresa un nro random en algun lugar libre elegido al azar"""
    while True:
        i = random.randint(0,DIMENSION_MATRIZ-1)
        j = random.randint(0,DIMENSION_MATRIZ-1)
        if matriz[i][j] == "":
            matriz[i][j] = random.choice(VALORES_ALEATORIOS)
            break;
    return matriz



#///////////////////////////////////////FUNCIONES PARA ACTUALIZAR EL JUEGO////////////////////////////////////////

#FUNCION PARA TRANSPONER LA MATRIZ

def transponer_matriz(matriz):
    for i in range (len(matriz)):
        for j in range(len(matriz[0])):
            if i < j:
                matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

#FUNCION PARA INVERTIR LAS FILAS DE LA MATRIZ

def invertir_filas(matriz):
    for i in range(0,DIMENSION_MATRIZ):
        matriz[i].reverse()

#FUNCION PARA COMBINAR LOS ELEMENTOS DE LA FILA

def combinar_filas(matriz):
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz)):
            if matriz[i][j] == "":
                matriz[i][j] = 0

    for i in range(0,len(matriz)):
        mover_nros_a_izquierda(matriz[i])
        sumar_si_consecutivos_son_iguales(matriz[i])
        mover_nros_a_izquierda(matriz[i])

    for i in range (0,len(matriz)):
        for j in range(0,len(matriz)):
            if matriz[i][j] == 0:
                matriz[i][j] = ""


#FUNCIONES UTILIZADAS PARA COMBINAR LOS ELEMENTOS DE LA FILA

def mover_nros_a_izquierda(fila_de_matriz):
    contador = 0
    for i in range(0,len(fila_de_matriz)):
        if fila_de_matriz[i] == 0:
            fila_de_matriz.append(0)
            contador+=1

    for i in range(0,contador):
            fila_de_matriz.remove(0)

        
def sumar_si_consecutivos_son_iguales(fila_de_matriz):
    for i in range(0,len(fila_de_matriz)-1):
        if fila_de_matriz[i] == fila_de_matriz[i+1]:
            fila_de_matriz[i] = fila_de_matriz[i]+fila_de_matriz[i+1]
            fila_de_matriz[i+1] = 0





