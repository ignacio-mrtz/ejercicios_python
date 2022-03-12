# La moda de una secuencia es el valor que se repite con mayor frecuencia. Dada la clase
# ListaEnlazada implementada únicamente con una referencia al primer nodo, implementar un
# método que devuelve la moda de la lista. Por ejemplo, si la LE contiene los valores [1, 5, 3,
# 8, 3, 5, 3, 3], el método debe devolver el valor 3.

class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.prim = None

    def moda(self):
        # HACER: implementar la función
        diccionario={}
        act=self.prim
        while act is not None:
            diccionario[act.dato]=diccionario.get(act.dato,0)+1
            act=act.prox
        cantidad_moda=None
        moda=None
        print(diccionario)
        for clave,valor in diccionario.items():
            if cantidad_moda is None or cantidad_moda<valor:
                cantidad_moda=valor
                moda=clave
        print(moda)
        return moda



def pruebas():
    #  creamos "a mano" la lista: [1, 5, 3, 8, 3, 5, 3, 3]
    L = ListaEnlazada()
    ult = None
    for x in [1, 5, 3, 8, 3, 5, 3, 3]:
        n = Nodo(x)
        if not L.prim:
            L.prim = n
        if ult:
            ult.prox = n
        ult = n

    assert L.moda() == 3

    # OPCIONAL: Pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
