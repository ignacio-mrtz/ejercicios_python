class Cola:
    def __init__(self):
        self.frente = None
        self.ultimo = None

    def encolar(self, dato):
        nodo = _Nodo(dato)
        if self.ultimo is None:
            self.frente = nodo
        else:
            self.ultimo.prox = nodo
        self.ultimo = nodo

    def desencolar(self):
        "pre: la cola no está vacía"
        dato = self.frente.dato
        self.frente = self.frente.prox
        if self.frente is None:
            # la cola quedó vacía
            self.ultimo = None
        return dato

    def esta_vacia(self):
        return self.ultimo == None

    def ver_frente(self):
        return self.frente.dato

class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None

