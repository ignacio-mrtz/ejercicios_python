# Ejercicio 1.5. Escribir una función que, dado un número entero 𝑛, permita calcular su factorial

def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial= factorial * i
    return factorial

#print(factorial(7))