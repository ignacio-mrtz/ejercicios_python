# Ejercicio 1 Implementar el método de ListaEnlazada ordenar(), que ordena los elementos de la
# lista cumpliendo que sea a lo sumo:
# • O(N²) en tiempo
# • O(log N) en memoria
# Se permite utilizar cualquiera de los algoritmos de ordenamiento vistos en clase (siempre
# y cuando se pueda aplicar a una lista enlazada cumpliendo los requisitos indicados). No se
# permite pasar los elementos a una lista de Python.

class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.prim = None

    def ordenar(self):
        # HACER: implementar

def pruebas():
    # armamos "a mano" la lista 3->1->7->4->3->7->2
    lista = ListaEnlazada()
    lista.prim = Nodo(3, Nodo(1, Nodo(7, Nodo(4, Nodo(3, Nodo(7, Nodo(2)))))))

    lista.ordenar()

    # ahora la lista es 1->2->3->3->4->7->7
    assert lista.prim.dato == 1
    assert lista.prim.prox.dato == 2
    assert lista.prim.prox.prox.dato == 3
    assert lista.prim.prox.prox.prox.dato == 3
    assert lista.prim.prox.prox.prox.prox.dato == 4
    assert lista.prim.prox.prox.prox.prox.prox.dato == 7
    assert lista.prim.prox.prox.prox.prox.prox.prox.dato == 7
    assert lista.prim.prox.prox.prox.prox.prox.prox.prox is None

    # OPCIONAL: escribir pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
