# Ejercicio 7.8. Inversión de listas
# a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea
# igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'],
# deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].
# b) Realizar otra función que invierta la lista, pero en lugar de devolver una nueva, modifique
# la lista dada para invertirla, sin usar listas auxiliares.

def main_a(lista):
    """devuelve una copia invertida de la lista"""
    return lista[::-1]


def main_b(lista):
    """devuelve la lista original invertida"""
    lista.reverse()
    return lista


print(main_b(['Di', 'buen', 'día', 'a', 'papa']))

