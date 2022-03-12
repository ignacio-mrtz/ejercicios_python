# Ejercicio 4.1. Escribir dos funciones que resuelvan los siguientes problemas:
# a) Dado un número entero 𝑛, indicar si es par o no.
# b) Dado un número entero 𝑛, indicar si es primo o no.

def es_par(nro):
    if nro%2 == 0:
        return true
    else:
        return false

#o tmb:

def es_par(n):
    return n % 2 == 0

#--------------------------------------------

# 1er solucion
def es_primo(n):
    if n>1:
        for i in range(2, n):
            if(n % i == 0):
                return False
    return True

# 2da resolucion
def es_primo(n):
    """Dado un número entero n, indica si es primo o no."""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True