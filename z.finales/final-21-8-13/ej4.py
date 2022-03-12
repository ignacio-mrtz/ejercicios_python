class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.prim = None

    def lshift(self, n):
        #
        # HACER: implementar
        #

def pruebas():

    # creamos "a mano" la lista [3] -> [5] -> [8] -> [11]
    n3 = _Nodo(11, None)
    n2 = _Nodo(8, n3)
    n1 = _Nodo(5, n2)
    n0 = _Nodo(3, n1)
    lista = ListaEnlazada()
    lista.prim = n0

    lista.lshift(3)

    assert lista.prim.dato == 11
    assert lista.prim.prox.dato == 3
    assert lista.prim.prox.prox.dato == 5
    assert lista.prim.prox.prox.prox.dato == 8

    # OPCIONAL: Pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
