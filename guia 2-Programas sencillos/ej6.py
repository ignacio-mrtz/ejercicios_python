# Ejercicio 2.6. Escribir un programa que imprima todos los números pares entre dos números
# que se le pidan al usuario.

def imprimir_pares():
    numero_inicial = int(input("escriba el numero inicial: "))
    numero_final = int(input("escriba el numero final: "))
    for i in range (numero_inicial, numero_final + 1):
        if i%2 == 0:
            print (i,end= " ")#pongo este end para que aparezcan uno al lado del otro y no uno abajo del otro

#imprimir_pares()
