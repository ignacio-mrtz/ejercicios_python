# Ejercicio 15.13. Escribir una función recursiva que reciba un conjunto de caracteres únicos, y
# un número 𝑘, e imprima todas las posibles cadenas de longitud 𝑘 formadas con los caracteres
# dados (permitiendo caracteres repetidos).
# Ejemplo: combinaciones(['a', 'b', 'c'], 2) debe imprimir aa ab ac ba bb bc ca cb cc

def main(conjunto,k):
    subconjunto=[]
    _main(conjunto,k,subconjunto)

def _main(conjunto,k,subconjunto):
    if len(subconjunto)==k:
        print(subconjunto)
        return
    for n in conjunto:
        _main(conjunto,k,subconjunto + [n])

main("abc",3)
