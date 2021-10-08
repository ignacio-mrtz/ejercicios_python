# Ejercicio 9.1. Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario
# en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los
# segundos.
# Por ejemplo:
# >>> l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]
# >>> print(tuplas_a_diccionario(l))
# { 'Hola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }

def main(lista_de_tuplas):
    diccionario={}
    for x in lista_de_tuplas:
        if diccionario.get(x[0], ''):
            diccionario[x[0]].append(x[1])
        else:
            diccionario[x[0]]=[x[1]]
    return diccionario


print(main([ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días'), ("Hola", "coco") ]))