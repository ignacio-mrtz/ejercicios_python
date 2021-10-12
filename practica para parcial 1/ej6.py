# Escribir un programa que pida dos números enteros al usuario (a y b) e imprima los primeros a múltiplos de b.
# El programa debe validar que cada número que ingrese el usuario sea un entero positivo y, en caso de que no lo sea, solicitarlo nuevamente (hasta que se ingrese algo correcto).
# 
# Ejemplo:
# 
# Ingrese el número 'a': 4
# Ingrese el número 'b': 6
# 6
# 12
# 18
# 24
# Ejemplo con números inválidos. Notar que no se pregunta por el número b hasta que a sea válido:
# 
# Ingrese el número 'a': -7
# Ingrese el número 'a': hola
# Ingrese el número 'a': 3
# Ingrese el número 'b': 0
# Ingrese el número 'b': 8
# 8
# 16
# 24

def main():
    while True:
        a=input("Ingrese el número 'a': ")
        if a.isdigit() and float(a)%1== 0 and float(a)>0:
            break
    while True:
        b=input("Ingrese el número 'b': ")
        if b.isdigit() and float(b)%1== 0 and float(b)>0:
            break

    contador=1
    a=int(a)
    b=int(b)
    while contador<=a:
        print(b*contador)
        contador+=1
    
main()

#otra solucion:

def imprimir_a_multiplos_de_b():
    while True:
        a = input("Ingrese el número 'a': ")
        if a.isdigit() and a != '0':
            break
    while True:
        b = input("Ingrese el número 'b': ")
        if b.isdigit() and b != '0':
            break
    for numero in range(1, int(a) + 1):
        print(int(b) * numero)
    
#imprimir_a_multiplos_de_b()