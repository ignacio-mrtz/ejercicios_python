# Ejercicio 2.9. Escribir un programa que imprima por pantalla todas las fichas de dominó, de
# una por línea y sin repetir

for i in range(1, 7):
    for j in range(i, 7):
        print("{}:{}".format(i, j))