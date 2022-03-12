#11.1. Escribir una función, llamada head que reciba un archivo y un número N e imprima
#las primeras N líneas del archivo.

def head(archivo,N):
    with open (archivo) as f:
        linea=f.readline()
        print(linea.rstrip("\n"))
        for i in range(1,N):
            linea=f.readline()
            print(linea.rstrip("\n"))



head("tareas.txt",2)

#otra forma:

def head2(archivo, N):
    with open(archivo) as f:
        for i, linea in enumerate(f):
            if i == N:
                return
            linea = linea.rstrip('\n')
            print(linea, i)
