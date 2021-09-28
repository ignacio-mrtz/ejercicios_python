# Ejercicio 5.8. Escribir un programa que le pida al usuario que ingrese una sucesión de números
# naturales (primero uno, luego otro, y así hasta que el usuario ingrese ’-1’ como condición de
# salida). Al final, el programa debe imprimir cuántos números fueron ingresados, la suma total
# de los valores y el promedio.

def main():
    i=0
    suma=0
    while True:
        nro= input("ingrese un nro natural(ingrese -1 para terminar la secuencia): ")
        if nro=="-1":
            prom=suma/i
            print("nros ingresados: ",i,"\nla suma es: ", suma,"\nel promedio es: ", prom)
            break
        i+=1
        suma+=int(nro)

main()