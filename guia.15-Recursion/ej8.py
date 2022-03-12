# Ejercicio 15.8. Escribir una funcion recursiva que encuentre el mayor elemento de una lista.

def _buscar_maximo(lista,maximo):
    if lista[0]>maximo:
        maximo=lista[0]
    if len(lista)==1:
        return maximo
    return _buscar_maximo(lista[1:],maximo)

def buscar_maximo(lista):
    maximo=lista[0]
    maximo=_buscar_maximo(lista,maximo)
    return maximo

print(buscar_maximo([1,7,3,23,5,753,8,34,1008,0,765]))
