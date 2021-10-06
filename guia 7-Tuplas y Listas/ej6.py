# Ejercicio 7.6. Dada una lista de números enteros y un entero k, escribir una función que:
# a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a
# k.
# b) Devuelva una lista con aquellos que son múltiplos de k.

def main_a(enteros,k):
    menores=list(filter(lambda x: x<k,enteros))
    mayores=list(filter(lambda x: x>k,enteros))
    iguales=list(filter(lambda x: x==k,enteros))
    return menores,mayores,iguales

#print(main_a([1,2,3,4,5,6],5))

#---------------------------------------------

def main_b(enteros,k):
    multiplos=list(filter(lambda x: x%k==0,enteros))
    return multiplos

print(main_b([5,7,8,10,15,11,5,155,2,9,0],5))
