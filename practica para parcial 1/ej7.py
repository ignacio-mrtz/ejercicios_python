# Escribir una función que reciba una cadena que contiene únicamente palabras separadas por espacios, y que devuelva # una nueva cadena con las letras de cada una de las palabras invertidas.
# 
# Ejemplo: invertir_palabras("Qué día tan bonito") --> "éuQ aíd nat otinob"

def invertir_palabras(frase):
    lista=frase.split()
    lista_nueva=[]
    for i,x in enumerate(lista):
        palabra= lista[i]
        palabra_invertida=""
        for i in range(len(palabra)-1,-1,-1):
            palabra_invertida+=palabra[i]
        lista_nueva.append(palabra_invertida)
    return " ".join(lista_nueva)

#print(invertir_palabras("Qué día tan bonito"))

#otra

def invertir_palabras2(frase):
    '''Dada una cadena con palabras separadas por espacios,
    devuelve la cadena con cada palabra invertida'''
    lista_de_palabras = frase.split(' ')
    for i in range(len(lista_de_palabras)):
        caracteres = list(reversed(list(lista_de_palabras[i])))
        lista_de_palabras[i] = ''.join(caracteres)
    return ' '.join(lista_de_palabras)