class _Nodo:
    def __init__(self,dato,prox=None):
        self.dato=dato
        self.prox=prox

class Cola:
    """Representa a una cola, con operaciones de encolar y
    desencolar. El primero en ser encolado es también el primero
    en ser desencolado. """
    def __init__(self):
        """Crea una cola vacía."""
        #invariante(se cumple siempre):
        #si la cola esta vacia, entonces primero=ultimo=None
        #si la cola no esta vacia, entonces primero!=None y ultimo!=None
        self.primero = None
        self.ultimo = None

    def encolar(self, x):
        """Encola el elemento x."""
        nuevo = _Nodo(x)
        if self.ultimo==None:
            #caso borde:recordar que si uno es none el otro tmb
            #cola vacia
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            #que el ultimo apunte al nuevo
            self.ultimo.prox = nuevo
            #y que ahora el ultimo sea el nuevo
            self.ultimo = nuevo

    def desencolar(self):
        """Desencola el primer elemento y devuelve su
        valor. Si la cola está vacía, levanta ValueError.
        PRE: la cola no puede estar vacia"""
        if self.primero is None:
            raise ValueError("La cola está vacía")
        valor = self.primero.dato
        self.primero = self.primero.prox
        #y ahora, si una vez que desencolé(saqué) el elemento, queda vacia, pongo los dos en None
        if not self.primero:
            self.ultimo = None
        return valor

    def esta_vacia(self):
        """Devuelve True si la cola esta vacía, False si no."""
        return self.primero is None

    def ver_frente(self):
        """PRE:la cola no es vacia"""
        return self.primero.dato