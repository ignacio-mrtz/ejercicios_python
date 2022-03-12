# Ejercicio 15.7. Escribir una función que calcule recursivamente cuántos elementos hay en una pila, suponiendo que la pila sólo tiene los métodos apilar y desapilar, y no altere el contenido de la pila

from pila import Pila

p=Pila()
p.apilar(2)
p.apilar(5)
p.apilar(8)
p.apilar(45)
p.apilar(31)

def _elementos_en_una_pila(pila,pila_extra):
    try:
        pila_extra.apilar(pila.desapilar())
    except:
        return 0
    return 1+ _elementos_en_una_pila(pila,pila_extra)

def elementos_en_una_pila(pila):
    pila_extra=Pila()
    cantidad=_elementos_en_una_pila(pila,pila_extra)
    while True:
        try:
            pila.apilar(pila_extra.desapilar())
        except:
            break
    print(str(pila_extra))
    print(str(p))
    return cantidad


print(elementos_en_una_pila(p))