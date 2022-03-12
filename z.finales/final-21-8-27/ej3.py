class Nodo:
    def __init__(self, dato, ant=None, prox=None):
        self.dato = dato
        self.prox = prox
        self.ant = ant

class ListaDoblementeEnlazada:
    def __init__(self):
        self.prim = None

    def eliminar(self, dato):
        # HACER: implementar la función

def pruebas():
    #  creamos "a mano" la lista: 10 <-> 20 <-> 30 <-> 40
    n0 = Nodo(10)
    n1 = Nodo(20, ant=n0)
    n2 = Nodo(30, ant=n1)
    n3 = Nodo(40, ant=n2)
    n0.prox = n1
    n1.prox = n2
    n2.prox = n3

    L = ListaDoblementeEnlazada()
    L.prim = n0

    L.eliminar(30)

    assert L.prim.dato == 10
    assert L.prim.prox.dato == 20
    assert L.prim.prox.prox.dato == 40
    assert L.prim.prox.prox.ant.dato == 20

    # OPCIONAL: Pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
