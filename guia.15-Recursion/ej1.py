# Ejercicio 15.1. Escribir una función recursiva que reciba un número positivo 𝑛 y devuelva la cantidad de dígitos que tiene.

def cantidad_de_digitos(n):
    numero=str(n)
    if len(numero)==0:
        return 0
    return 1+ cantidad_de_digitos(numero[1:])


print(cantidad_de_digitos(123))
print(cantidad_de_digitos(1234))
print(cantidad_de_digitos(12223))
print(cantidad_de_digitos(123354))
print(cantidad_de_digitos(1341341))
print(cantidad_de_digitos(41343153))
