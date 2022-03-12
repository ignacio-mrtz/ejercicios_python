# 11.4. Escribir una función, llamada grep, que reciba una cadena y un archivo e imprima
# las líneas del archivo que contienen la cadena recibida.

def grep(cadena, archivo):
    with open(archivo) as f:
        for linea in f:
            linea=linea.rstrip("\n")
            if cadena in linea:
                print(linea)

grep("tramites","tareas.txt")

#o tmb:

def grep2(cadena,archivo):
    with open(archivo) as f:
        for linea in f:
            if cadena in linea:
                print(linea.rstrip("\n"))
                
grep2("c","tareas.txt")