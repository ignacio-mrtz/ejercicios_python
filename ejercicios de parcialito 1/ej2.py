# Escribir un programa que pida al usuario que ingrese líneas de texto, hasta que ingrese un *. El programa deberá  imprimir todas las líneas encerradas en un marco con *. Ejemplo:
# 
# Ingrese una linea o '*' para terminar: Hola
# Ingrese una linea o '*' para terminar: Mundo
# Ingrese una linea o '*' para terminar: en un marco
# Ingrese una linea o '*' para terminar: *
# ***************
# * Hola        *
# * Mundo       *
# * en un marco *
# ***************

def main():
    lista=[]
    maximo=0
    while True:
        cadena = input("Ingrese una linea o '*' para terminar: ")
        if cadena=="*":
            break
        lista.append(cadena)
        if len(cadena)>maximo:
            maximo=len(cadena)
    if  maximo>0:
        maximo=maximo+3
    print(("*" * (maximo))+"*")
    for i in range(0,len(lista)):
        print(f'* {lista[i]}{" "*(maximo-len(lista[i])-3)} *')
    print(("*" * (maximo))+"*")

main()