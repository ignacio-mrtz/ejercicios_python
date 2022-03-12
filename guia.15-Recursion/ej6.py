# Ejercicio 15.6. Escribir una función recursiva que calcule recursivamente el n-ésimo número triangular (el número 1 + 2 + 3 + ⋯ + 𝑛).

def numero_triangular(n):
    if n==1:
        return 1
    return n+numero_triangular(n-1)

print(numero_triangular(1))
print(numero_triangular(2))
print(numero_triangular(3))
print(numero_triangular(4))
print(numero_triangular(5))
print(numero_triangular(6))
print(numero_triangular(7))