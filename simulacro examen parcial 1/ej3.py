#3.  Escribir una función que recibe una cadena y devuelve la cadena eliminando los caracteres repetidos consecutivos.
#Ejemplo:
#sin_repetir('aaabbaac') → 'abac'

    
def main(string):
    cadena_nueva=""
    for i,c in enumerate(string):
        if i!=0 and c==string[i-1]:
            continue
        else:
            cadena_nueva+=c
    return cadena_nueva

print(main('aaabbaac'))

