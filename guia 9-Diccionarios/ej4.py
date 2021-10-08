# Ejercicio 9.4. Escribir una función que reciba un texto y para cada caracter presente en el texto
# devuelva la cadena más larga en la que se encuentra ese caracter.

def main(texto):
    dic = {}
    texto = texto.split(' ')
    for palabra in texto:
        for letra in palabra:
            if dic.get(letra, ''):
                if len(palabra) >= len(dic[letra]):
                    dic[letra] = palabra
            else: 
                dic[letra] = palabra
    return dic


texto="anafkhdfhddg kiwi tomate banana zapallo manzana"

print(main(texto))