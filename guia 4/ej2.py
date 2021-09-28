# Ejercicio 4.2. Escribir una implementación propia de la función abs, que devuelva el valor absoluto
# de cualquier valor que reciba.

def absoluto(nro):
    if nro<0:
        return -(nro)
    return nro

#o tmb:

def absoluto2(n):
    return (n ** 2) ** (1/2)

#print(absoluto(-565))