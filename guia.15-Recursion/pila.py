class _Nodo:
    def __init__(self,dato,prox=None):
        self.dato=dato
        self.prox=prox

class Pila:
    def __init__(self):
        self.tope=None

    def apilar(self,dato):
        self.tope=_Nodo(dato,self.tope)
    
    def desapilar(self):
        dato=self.tope.dato
        self.tope=self.tope.prox
        return dato

    def ver_tope(self):
        return self.tope.dato

    def esta_vacia(self):
        return self.tope is None

    def __str__(self):
        L=[]
        act=self.tope
        while act is not None:
            L.append(str(act.dato))
            act=act.prox
        return "[" + ",".join(L) + "]"