# Ejercicio 1.2. Utilizando la función del ejercicio anterior, escribir un programa (un archivo .py)
# que pida al usuario dos números, y luego muestre el producto.

from ej1 import multiplicacion

def main():
    numero1 = float(input("ingrese el primer numero: "))
    numero2 = float(input("ingrese el segundo numero: "))
    resultado = multiplicacion(numero1, numero2)
    print (resultado)

main()

# o tmb 

#import ej1

#def main():
    #numero1 = float(input("ingrese el primer numero: "))
    #numero2 = float(input("ingrese el segundo numero: "))
    #resultado = ej1.multiplicacion(numero1, numero2)
    #print (resultado)

#main()
