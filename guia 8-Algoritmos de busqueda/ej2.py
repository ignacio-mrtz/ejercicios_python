# Ejercicio 8.2. Escribir una función que reciba una lista de números no ordenada, que:
# a) Devuelva el valor máximo.
# b) Devuelva una tupla que incluya el valor máximo y su posición.
# c) ¿Qué sucede si los elementos son cadenas de caracteres?
# Nota: no utilizar lista.sort()


def main_a(lista_de_numeros_no_ordenada):
    maximo=lista_de_numeros_no_ordenada[0]
    for i in range (1,len(lista_de_numeros_no_ordenada)):
        if lista_de_numeros_no_ordenada[i]>maximo:
            maximo=lista_de_numeros_no_ordenada[i]
    return maximo

#print(main_a([1,2,3,4,5,6,11,22,45,7785,565,976,452,12,4,5,43242,1444,1,4,6,73]))

def main_b(lista_de_numeros_no_ordenada):
    maximo=lista_de_numeros_no_ordenada[0]
    posicion=0
    for i in range (1,len(lista_de_numeros_no_ordenada)):
        if lista_de_numeros_no_ordenada[i]>maximo:
            maximo=lista_de_numeros_no_ordenada[i]
            posicion=i
    return maximo,posicion

#print(main_b([1,2,3,4,5,6,11,22,45,7785,565,976,452,12,4,5,43242,1444,1,4,6,73]))

print(main_b(["AFsf","fgadd","39adssnk","zgedg","vadaf"]))
#c)el maximo es el ultimo segun el orden lexicografico

