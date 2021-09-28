# Ejercicio 5.1. Escribir un programa que permita al usuario ingresar un conjunto de notas, preguntando
# a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.

def notas():
    i=0
    suma=0
    while True:
        centinela = input("ingrese una nota (escriba '*' para terminar):")
        if centinela == '*':
            prom=suma/i
            print("el promedio es: ",prom)
            break
        nota = int(centinela)
        suma+=nota
        i+=1
    
#notas()
        
#resolucion de clase: 

def main():
    suma = 0
    cant_notas = 0

    while True:
        nota = float(input("Ingrese una nota: "))
        if nota < 0 or nota > 10:
            print("Por favor ingrese un numero entre 0 y 10")
            continue

        suma += nota
        cant_notas += 1
        opc = input("Quiere ingresar otra nota? [Y/n]: ")
        if opc != 'Y':
            break

    print("El promedio de notas es de: ", suma / cant_notas)


#main()
