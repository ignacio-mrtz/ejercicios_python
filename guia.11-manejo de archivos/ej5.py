# 11.5. Escribir una función, llamada rot13, que reciba un archivo de texto de origen
# y uno de destino, de modo que para cada línea del archivo origen, se guarde una línea cifrada
# en el archivo destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter comprendido
# entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para obtener un nuevo
# caracter.

import string

def buscar_indice_en_abecedario(caracter,abecedario):
        for i,x in enumerate(abecedario):
            if x==caracter:
                return i

def rot13(archivo_de_origen,archivo_de_destino):
    abecedario=string.ascii_lowercase

    with open(archivo_de_origen) as f:
        with open(archivo_de_destino,"w") as d:
            lista_de_cadenas=[]
            for linea in f:
                nueva_linea=""
                for caracter in linea:
                    if caracter in abecedario:
                        indice_en_abecedario= buscar_indice_en_abecedario(caracter,abecedario)
                        nuevo_indice=(indice_en_abecedario+13)%26
                        nuevo_caracter=abecedario[nuevo_indice]
                        nueva_linea+=nuevo_caracter
                    else:
                        nueva_linea+=caracter
                lista_de_cadenas.append(nueva_linea)
            d.writelines(lista_de_cadenas)

rot13("tareas.txt","copiaderot13_5.txt")

#o tmb:

def rot13b(archivo_de_origen,archivo_de_destino):
    with open(archivo_de_origen) as f:
        with open(archivo_de_destino,"w") as f2:
            for linea in f:
                abecedario=string.ascii_lowercase
                linea=linea.rstrip("\n")
                for c in linea:
                    for i,x in enumerate(abecedario):
                        if x==c:
                            f2.write(abecedario[(i+13)%26])
                            break

rot13("tareas.txt","copiaderot13_b.txt")


        

