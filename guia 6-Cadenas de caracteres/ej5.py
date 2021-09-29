# Ejercicio 6.5. Escribir una función que dada una cadena de caracteres, devuelva:
# a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
# devolver 'USB'.
# b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
# 'república argentina' debe devolver 'República Argentina'.
# c) Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer'
# debe devolver 'Antes ayer'

def main(string):
    sum=string[0]
    for i in range (0,len(string)):
        if string[i]==" ":
            sum+= string[i+1]
    return sum

#print(main("Universal Serial Bus"))

def mainb(string):
    sum=string[0].capitalize()
    for i in range (1,len(string)):
        if string[i]==" ":
            sum+= " "+string[i+1].capitalize()
        else:
            sum+=string[i]
    return sum

#print(mainb("afsaf aegdg plkfas"))

def mainc(string):
    palabras = string.split(' ')
    sum=""
    for i in range(0,len(palabras)):
        if palabras[i][0]=="a" or palabras[i][0]=="A":
            sum+=palabras[i]+" "
    return sum

print(mainc("ave hola arca oso Ala"))