class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.prim = None

    def eliminar_ultimo(self, dato):
        # HACER: implementar
        if self.prim.prox == None: #La lista tiene un solo elemento
            if self.prim.dato == dato: # Ese unico elemento era el que se queria eliminar
                self.prim = None 
            return
        anterior = None
        actual = self.prim
        anterior_al_elemento = None
        elemento_a_borrar = None
        proximo_al_elemento = None
        while actual:
            if actual.dato == dato:
                anterior_al_elemento = anterior
                elemento_a_borrar = actual
                proximo_al_elemento = actual.prox
            anterior = actual
            actual = actual.prox
        if self.prim == elemento_a_borrar:
            self.prim = elemento_a_borrar.prox
        else:
            elemento_a_borrar.prox = None
            anterior_al_elemento.prox = proximo_al_elemento



def pruebas():
    # armamos "a mano" la lista 1->3->7->4->3->7->2
    lista = ListaEnlazada()
    lista.prim = Nodo(1, Nodo(3, Nodo(7, Nodo(4, Nodo(3, Nodo(7, Nodo(2)))))))

    lista.eliminar_ultimo(7)

    # ahora la lista es 1->3->7->4->3->2
    assert lista.prim.prox.prox.dato == 7
    assert lista.prim.prox.prox.prox.prox.prox.dato == 2

    # OPCIONAL: escribir pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")


pruebas()
