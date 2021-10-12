# Un bigrama es una secuencia de dos palabras contiguas dentro de un texto. Escribir una función que reciba un texto y devuelva una lista con todos sus bigramas. Los mismos deberán estar representados con una tupla (, ). Ejemplo:
# 
# >>> obtener_bigramas("Uno se alegra de resultar útil")
# [('Uno', 'se'), ('se', 'alegra'), ('alegra', 'de'), ('de', 'resultar'), ('resultar', 'util')]

def main(texto):
    lista_con_palabras = texto.split()
    lista_con_bigramas=[]
    for i in range (0,len(lista_con_palabras)-1):
        lista_con_bigramas.append(tuple([lista_con_palabras[i], lista_con_palabras[i+1]]))
    print(lista_con_bigramas)
        

main("Uno se alegra de resultar útil")

#o tmb:
def obtener_bigramas2(texto):
    texto_en_lista = texto.split(' ')
    for i in range(len(texto_en_lista) - 1):
        texto_en_lista[i] = texto_en_lista[i], texto_en_lista[i + 1]
    texto_en_lista.pop()
    return texto_en_lista