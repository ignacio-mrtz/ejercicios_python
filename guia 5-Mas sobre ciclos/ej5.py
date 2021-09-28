# Ejercicio 5.5. Algoritmo de Euclides
# a) Implementar el algoritmo de Euclides para calcular el máximo común divisor de dos
# números 𝑛 y 𝑚, dado por los siguientes pasos.
# 1. Teniendo 𝑛 y 𝑚, se obtiene 𝑟, el resto de la división entera de 𝑚/𝑛.
# 2. Si 𝑟 es cero, 𝑛 es el mcd de los valores iniciales.
# 3. Se reemplaza 𝑚 ← 𝑛, 𝑛 ← 𝑟, y se vuelve al primer paso.
# b) Hacer un seguimiento del algoritmo implementado para los siguientes pares de números:
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



            
            
        