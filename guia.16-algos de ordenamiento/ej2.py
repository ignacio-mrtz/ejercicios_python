#Ejercicio 16.2. Escribir una función merge_sort_3 que funcione igual que el merge sort pero en lugar de dividir los valores en dos partes iguales, los divida en tres (asumir que se cuenta con la función merge(lista_1, lista_2, lista_3)). ¿Cómo te parece que se va a comportar este método con respecto al merge sort original?

def merge_sort_3(L):
    if len(L)<2:
        return L[:]
    medio1=len(L)//3
    medio2=2*len(L)//3
    primera=merge_sort_3(L[:medio1])
    segunda=merge_sort_3(L[medio1:medio2])
    tercera=merge_sort_3(L[medio2:])
    return merge(primera,segunda,tercera)


    