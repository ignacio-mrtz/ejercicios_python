# Ejercicio 2.4. Escribir un programa que utilice la función anterior para generar una tabla de
# conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10.

import ej3

for i in range (0, 121, 10):
    celsius = ej3.farenheit_a_celsius(i)
    print( i, " grados farenheit es igual a ", celsius, "grados celsius\n")



