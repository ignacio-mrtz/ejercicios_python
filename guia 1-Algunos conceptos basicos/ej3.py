# Ejercicio 1.3. Escribir funciones que permitan:
# a) Calcular el perímetro de un rectángulo dada su base y su altura.
# b) Calcular el área de un rectángulo dada su base y su altura.
# c) Calcular el área de un rectángulo (alineado con los ejes 𝑥 e 𝑦) dadas sus coordenadas
# 𝑥1, 𝑥2, 𝑦1, 𝑦2.
# d) Calcular el perímetro de un círculo dado su radio.
# e) Calcular el área de un círculo dado su radio.
# f) Calcular el volumen de una esfera dado su radio.
# g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

from math import pi,sqrt

def perimetro_rectangulo(base, altura):
    perimetro = base * 2 + altura *2
    return perimetro

def area_rectangulo(base, altura):
    area = base * altura
    return area

def area_rectangulo_con_coordenadas(x1, x2, y1, y2):
    area = (x2 - x1) * (y2 - y1)
    return area

def perimetro_circulo(radio):
    area = pi * (radio**2)
    return area

def volumen_esfera(radio):
    volumen = (4/3) * pi * (radio**3)
    return volumen

def hipotenusa(cateto1, cateto2):
    hipotenusa = sqrt((cateto1**2)+(cateto2**2))
    return hipotenusa






