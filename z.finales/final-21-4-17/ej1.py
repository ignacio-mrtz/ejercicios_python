class Nodo:
    def __init__(self, dato, izq=None, der=None):
        self.dato = dato
        self.izq = izq
        self.der = der

    def recorrer(self, camino):
        # HACER: implementar la funcion

def pruebas():
    # el árbol ejemplo del enunciado
    raiz = Nodo(2,
        izq = Nodo(7,
            izq = Nodo(2),
            der = Nodo(6,
                izq = Nodo(5),
                der = Nodo(11),
            ),
        ),
        der = Nodo(5,
            der = Nodo(9,
                izq = Nodo(4),
            ),
        ),
    )

    assert raiz.recorrer("010") == 5

    # OPCIONAL: pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
