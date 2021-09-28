# Ejercicio 2.2. Utilizando la función del ejercicio anterior, escribir un programa que le pregunte
# al usuario la cantidad de pesos inicial, la tasa de interés y el número de años y muestre el monto
# final a obtener.

import ej1

def main():
    pesos = int(input("ingrese cantidad de pesos: "))
    tasa_de_interes = int(input("ingrese la tasa de interes: "))
    años = int(input("ingrese años: "))
    monto_final = ej1.main(pesos, tasa_de_interes, años)
    print("el monto final es : ", monto_final)

main()


