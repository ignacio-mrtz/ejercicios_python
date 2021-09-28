# Ejercicio 1.6. Escribir funciones que resuelvan los siguientes problemas:
# a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.
# b) Dado un número entero 𝑛, imprimir su tabla de multiplicar.

def cuentas(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    division = numero1 / numero2
    multiplicacion = numero1 * numero2
    print("la suma es: ", suma, "\nla resta es: ", resta, "\nla multiplicacion es: ", multiplicacion, "\nla division es: ", division)

#cuentas(2,5)

def tabla_de_multiplicacion(numero):
    for i in range(10):
        resultado= numero * i
        print( numero, "*", i," = ", resultado)

#tabla_de_multiplicacion(4)

