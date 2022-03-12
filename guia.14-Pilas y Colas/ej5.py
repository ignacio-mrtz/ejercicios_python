# Ejercicio 14.5. Crear una clase PilaConMaximo que soporte las operaciones de Pila
# (apilar(elemento) y desapilar()), y además incluya el método obtener_maximo() en tiempo
# constante. 
# Ayuda: usar dos pilas, una para guardar los elementos y otra para guardar los máximos.

#resolucion de ej chequeado en rpl

from pila import Pila

class PilaConMaximo:
    def __init__(self):
        self.pila_con_elementos=Pila()
        self.pila_con_maximos=Pila()

    def ver_tope(self):
        return self.pila_con_elementos.ver_tope()

    def apilar(self,elemento):
        self.pila_con_elementos.apilar(elemento)
        if self.pila_con_maximos.esta_vacia()==True:
            self.pila_con_maximos.apilar(elemento)
        elif self.pila_con_maximos.ver_tope()<=elemento:
            self.pila_con_maximos.apilar(elemento)


    def desapilar(self):
        nro_desapilado=self.pila_con_elementos.desapilar()
        if nro_desapilado==self.pila_con_maximos.ver_tope():
            self.pila_con_maximos.desapilar()
        return nro_desapilado

    def obtener_maximo(self):
        return self.pila_con_maximos.ver_tope()

class PilaConMaximo2:
    def __init__(self):
        self.elementos=Pila()
        self.maximos=Pila()

    def apilar(self,nro):
        self.elementos.apilar(nro)
        if self.maximos.esta_vacia() or self.maximos.ver_tope()<=nro:
            self.maximos.apilar(nro)

    def desapilar(self):
        if self.elementos.ver_tope()==self.maximos.ver_tope():
            self.maximos.desapilar()
        return self.elementos.desapilar()

    def obtener_maximo(self):
        return self.maximos.ver_tope()




