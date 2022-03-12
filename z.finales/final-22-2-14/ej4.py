
# Implementar en forma recursiva el método de ListaEnlazada intercambiar_pares()
# que intercambia los datos de cada par de nodos adyacentes.
# Ejemplo:
# lista = a -> b -> c -> d -> e -> f -> g
# lista.intercambiar_pares()
# b -> a -> d -> c -> f -> e -> g

class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.prim = None

    def intercambiar_pares(self):
        # HACER: implementar en forma RECURSIVA
        if self.prim.prox==None:
            return self
        ant=self.prim
        act=self.prim.prox
        ant.prox=act.prox
        act.prox=ant
        self.prim=act
        if ant.prox==None:
            return self
        lista_siguiente=ListaEnlazada()
        lista_siguiente.prim=ant.prox
        ant.prox=lista_siguiente.intercambiar_pares().prim
        return self


def pruebas():
    # armamos "a mano" la lista a -> b -> c -> d -> e -> f -> g
    L = ListaEnlazada()
    L.prim = Nodo('a', Nodo('b', Nodo('c', Nodo('d', Nodo('e', Nodo('f', Nodo('g')))))))

    L.intercambiar_pares()

    assert L.prim.dato == 'b'
    assert L.prim.prox.dato == 'a'
    assert L.prim.prox.prox.dato == 'd'
    assert L.prim.prox.prox.prox.dato == 'c'
    assert L.prim.prox.prox.prox.prox.dato == 'f'
    assert L.prim.prox.prox.prox.prox.prox.dato == 'e'
    assert L.prim.prox.prox.prox.prox.prox.prox.dato == 'g'

    assert L.prim.prox.prox.prox.prox.prox.prox.prox is None
    # OPCIONAL: escribir pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()

