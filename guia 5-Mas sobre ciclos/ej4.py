# Ejercicio 5.4. Utilizando la función randrange del módulo random, escribir un programa que
# obtenga un número aleatorio secreto, y luego permita al usuario ingresar números y le indique
# si son menores o mayores que el número a adivinar, hasta que el usuario ingrese el número
# correcto.

from random import randrange

def adivine_el_numero():
    numero_aleatorio_secreto=randrange(101)
    while True:
        numero_elegido=input("ingrese un nro entero entre 0 y 100(presione * para terminar el juego): ")
        if numero_elegido == "*":
            print("saliste del juego")
            return 
        numero_elegido=int(numero_elegido)
        if numero_elegido == numero_aleatorio_secreto:
            break
        if 0 <= numero_elegido<numero_aleatorio_secreto:
            print("el numero secreto es mayor")
        elif numero_aleatorio_secreto<numero_elegido <= 100:
            print("el numero secreto es menor")
    print("adivinaste!!!!!!")

adivine_el_numero()