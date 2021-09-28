# Ejercicio 3.2. Usando las funciones del ejercicio anterior, escribir un programa que pida al usuario
# dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre
# por pantalla la duración total en horas, minutos y segundos.

import ej1

def main():
    h1 = int(input("ingrese hora 1: "))
    m1 = int(input("ingrese minutos 1: "))
    s1 = int(input("ingrese segundos 1: "))
    h2 = int(input("ingrese hora 2: "))
    m2 = int(input("ingrese minutos 2: "))
    s2 = int(input("ingrese segundos 2: "))
    sumatoria = ej1.duracion_en_segundos(h1,m1,s1) + ej1.duracion_en_segundos(h2,m2,s2)
    hf,mf,sf = ej1.duracion_en_hs_min_seg(sumatoria)
    print(hf,mf,sf)

main()