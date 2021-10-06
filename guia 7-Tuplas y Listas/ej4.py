# Ejercicio 7.4. Vectores
# a) Escribir una función que reciba dos vectores y devuelva su producto escalar.
# b) Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.
# c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.
# d) Escribir una función que reciba un vector y devuelva su norma.


def producto_escalar(vector1,vector2):
    sum=0
    for i in range(0,len(vector1)):
        sum+=vector1[i]*vector2[i]
    return sum

#print(producto_escalar([1,5,7],[5,2,8]))

def vectores_ortogonales(vector1,vector2):
    sum=0
    for i in range(0,len(vector1)):
        sum+=vector1[i]*vector2[i]
    if sum==0:
        return True
    else:
        return False

def vectores_paralelos(vector1,vector2):
    division=vector1[0]/vector2[0]
    for i in range(1,len(vector1)):
        if vector1[i]==0 and vector2[i]==0:
            continue
        elif vector1[i]!=0 and vector2[i]==0:
            return False
        elif vector1[i]/vector2[i]!=division:
            return False
    return True

#print(vectores_paralelos([2,1,0],[4,2,0]))

def norma_de_vector(vector):
    sum=0
    for i in range(0,len(vector)):
        cuadrado=vector[i]**2
        sum+=cuadrado
    norma=(sum)**(1/2)
    return norma

#print(norma_de_vector([2,2,3]))
