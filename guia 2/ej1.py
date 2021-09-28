# Ejercicio 2.1. Escribir una función que reciba una cantidad de pesos, una tasa de interés y un
# número de años y devuelva el monto final a obtener. La fórmula a utilizar es:
# 𝐶𝑛 = 𝐶 × (1 + 𝑥/100)^𝑛
# Donde 𝐶 es el capital inicial, 𝑥 es la tasa de interés y 𝑛 es el número de años a calcular.

def main(pesos, tasa_de_interes, años):
    monto_final = pesos * ((1 + (tasa_de_interes / 100))**años)
    print(monto_final)
    return monto_final

#main(1500, 5, 10)