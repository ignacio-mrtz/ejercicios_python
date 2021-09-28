# Ejercicio 5.2. Escribir una función que reciba un número entero 𝑘 e imprima su descomposición
# en factores primos

def es_primo(nro):
    if nro<=1:
        return False
    for i in range (2,nro):
        if nro%i == 0:
            return False
    return True

def imprimir_descomposicion_en_primos(k):
    divisor = 2
    while k > 1:
        if k % divisor == 0:
            k //= divisor
            print(divisor)
        else:
            divisor = siguiente_primo(divisor)

def siguiente_primo(n):
    while True:
        n += 1
        if es_primo(n):
            break
    return n


imprimir_descomposicion_en_primos(4913)
    


