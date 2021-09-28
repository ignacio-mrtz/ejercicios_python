# Ejercicio 2.7. Escribir un programa que le pregunte al usuario un número 𝑛 e imprima los
# primeros 𝑛 números triangulares, junto con su índice. Los números triangulares se obtienen
# mediante la suma de los números naturales desde 1 hasta 𝑛. Es decir, si se piden los primeros 5
# números triangulares, el programa debe imprimir:
# 1 - 1
# 2 - 3
# 3 - 6
# 4 - 10
# 5 - 15

def primeros_n_numero_triangulares():
    n = int(input("ingrese un numero natural: "))
    sum = 0
    for i in range (1, n+1):
        sum= sum + i
        print (i, "-" , sum)

primeros_n_numero_triangulares()

