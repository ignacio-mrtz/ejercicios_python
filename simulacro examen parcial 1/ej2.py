#2. Se tiene una lista de listas que representa un laberinto en forma de matriz cuadrada (dos dimensiones). En cada #posición i, j habrá una tupla que indicará cuantos casilleros moverse y en qué dirección, por ejemplo (3,'v') debe #moverse 3 posiciones en sentido vertical hacia abajo; (-1, 'h') indica que se debe mover en una posición hacia la #izquierda. Implementar una función que reciba un laberinto de este tipo y que empezando por el 0, 0 indique en #cuántos pasos se sale del laberinto, es decir, llegar a la posición n-1, n-1 (está garantizado que se puede salir).
#Ejemplo:
matriz = [[(1, 'h'), (2, 'v'), (1, 'h')],
          [(1, 'v'), (1, 'h'), (1, 'v')], 
          [(1, 'h'), (-1, 'v'), (1, 'h')]]
#Resultado -> 5

def main(matriz):
    i=0
    j=0
    posicion=matriz[i][j]
    dimension_matriz=len(matriz[i])
    pasos=0
    while True:
        if posicion[1]=="h":
            j=j+posicion[0]
            posicion_nueva=matriz[i][j]
        if posicion[1]=="v":
            i=i+posicion[0]
            posicion_nueva=matriz[i][j]
        posicion=posicion_nueva
        pasos+=1
        if i==dimension_matriz-1 and j==dimension_matriz-1:
            return pasos

print(main(matriz))

        


    