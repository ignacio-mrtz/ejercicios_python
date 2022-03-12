# Ejercicio 2.8. Escribir un programa que tome una cantidad 𝑚 de valores ingresados por el usuario,
# a cada uno le calcule el factorial (utilizando la función escrita en el ejercicio 1.5) e imprima
# el resultado junto con el número de orden correspondiente

def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial= factorial * i
    return factorial

def main():
    m = int(input("cuantos numeros quiere ingresar: "))
    for i in range (1, m + 1):
        numero = int(input("ingrese el numero: "))
        resultado = factorial(numero)
        print("nro de orden", i, ". ", "factorial de", numero, ": ",resultado )

#main()

def main2():
    cont=1
    while True:
        numero=input("ingrese un nro para calcular su factorial(escriba '*' para terminar):")
        if numero=="*":
            return
        numero=int(numero)
        fact=factorial(numero)
        print(f"orden {cont}: el factorial de {numero} es {fact}")
        cont+=1

#main2()


