# Ejercicio 15.4. Escribir una funcion recursiva que reciba como parámetros dos cadenas a y b, y
# devuelva una lista con las posiciones en donde se encuentra b dentro de a.
# Ejemplo:
# posiciones_de("Un tete a tete con Tete", "te") -> [3, 5, 10, 12, 21]


def _posiciones_de(cadena_a, cadena_b,lista,i):
    if len(cadena_a)==0:
        return lista
    elif cadena_a[:2]=="te":
        lista.append(i)
        return _posiciones_de(cadena_a[2:],cadena_b,lista,i+2)
    return _posiciones_de(cadena_a[1:],cadena_b,lista,i+1)

def posiciones_de(cadena_a,cadena_b):
    lista=[]
    return _posiciones_de(cadena_a,cadena_b,lista,0)

print(posiciones_de("Un tete a tete con Tete", "te"))