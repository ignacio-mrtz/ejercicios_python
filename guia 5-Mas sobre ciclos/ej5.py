# Ejercicio 5.5. Algoritmo de Euclides
# a) Implementar el algoritmo de Euclides para calcular el mรกximo comรบn divisor de dos
# nรบmeros ๐ y ๐, dado por los siguientes pasos.
# 1. Teniendo ๐ y ๐, se obtiene ๐, el resto de la divisiรณn entera de ๐/๐.
# 2. Si ๐ es cero, ๐ es el mcd de los valores iniciales.
# 3. Se reemplaza ๐ โ ๐, ๐ โ ๐, y se vuelve al primer paso.
# b) Hacer un seguimiento del algoritmo implementado para los siguientes pares de nรบmeros:
# (15, 9); (9, 15); (10, 8); (12, 6).


def maximo_comun_divisor_de_2_numeros(n,m):
    mcd=0
    r=m%n
    if n==0:
        mcd=m
    elif m==0:
        mcd=n
    elif r==0:
        mcd==n
    else:
        while r!=0:
            q=m//n
            r=m%n
            m=n
            n=r
            print(m)
    print("el mcd es:", m)

maximo_comun_divisor_de_2_numeros(192,270)



            
            
        