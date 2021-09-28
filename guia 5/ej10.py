# Ejercicio 5.10. Escribir una función que reciba un número natural e imprima todos los números
# primos que hay hasta ese número.

def es_primo(nro):
    for i in range(2,nro):
        if nro%i==0:
            return False
    return True

#print(es_primo(29))

def nros_primos_hasta_n_nro(n):
    i=1
    while i<=n:
        if es_primo(i):
            print(i,end=", ")
        i+=1

nros_primos_hasta_n_nro(50)
 








