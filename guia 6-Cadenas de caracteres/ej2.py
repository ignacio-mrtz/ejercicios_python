# Ejercicio 6.2. Escribir funciones que dada una cadena y un caracter:
# a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
# 's,e,p,a,r,a,r'
# b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
# debería devolver 'mi_archivo_de_texto.txt'
# c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y
# 'X' debería devolver 'su clave es: XXXX'
# d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver
# '255.255.255.0'

def insertar_caracter_entre_cada_letra_de_la_cadena2(string,caracter):
    print(caracter.join(string))


#insertar_caracter_entre_cada_letra_de_la_cadena2("hola",",")

def reemplazar_los_espacios_por_el_caracter(string,caracter):
    print(string.replace(" ",caracter))

#reemplazar_los_espacios_por_el_caracter("hola como va","-")

def reempazar_todos_los_digitos_del_string_por_caracter(string,caracter):
    for c in string:
        if c.isdecimal():
            print(c.replace(c,caracter), end="")
        else:
            print(c,end="")
    
#reempazar_todos_los_digitos_del_string_por_caracter("tu nro es: 45265","X")

def insertar_caracter_cada_3_digitos_en_cadena(string,caracter):
    for i in range(0,len(string)):
        if (i+1)%3==0:
            print(string[i]+caracter, end="")
        else:
            print(string[i], end="")

#insertar_caracter_cada_3_digitos_en_cadena("1283923107", ".")




