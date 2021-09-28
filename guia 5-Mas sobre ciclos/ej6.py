# Ejercicio 5.6. Potencias de dos.
# a) Escribir una función es_potencia_de_dos que reciba como parámetro un número natural,
# y devuelva True si el número es una potencia de 2, y False en caso contrario.
# b) Escribir una función que, dados dos números naturales pasados como parámetros,
# devuelva la suma de todas las potencias de 2 que hay en el rango formado por
# esos números (0 si no hay ninguna potencia de 2 entre los dos). Utilizar la función
# es_potencia_de_dos, descripta en el punto anterior.

def es_potencia_de_dos(nro):
    """se ingresa un nro natural y si es potencia de 2 devuelve true"""
    if nro<2:
        return False
    resultado=2
    while resultado<=nro:
        resultado*=2
        if resultado==nro:
            return "es potencia de 2"
    return False

#print(es_potencia_de_dos(32))

def suma_de_todas_las_potencias_de_2_en_el_rango(nro1,nro2):
    sum=0
    for i in range(nro1,nro2+1):
        if es_potencia_de_dos(i):
            sum+=i
            print(i, end=" ")#para ir viendo los valores q se suman
    return sum

print(suma_de_todas_las_potencias_de_2_en_el_rango(33,63))