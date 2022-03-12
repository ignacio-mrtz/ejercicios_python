# Ejercicio 14.5. Crear una clase PilaConMinimo que soporte las operaciones de Pila
# (apilar(elemento) y desapilar()), y además incluya el método obtener_minimo() en tiempo
# constante.
# Ayuda: usar dos pilas, una para guardar los elementos y otra para guardar los minimos.

from pila import Pila

class PilaConMinimo:
    def __init__(self):
        self.pila_con_elementos=Pila()
        self.pila_con_minimos=Pila()

    def ver_tope(self):
        return self.pila_con_elementos.ver_tope()

    def apilar(self,elemento):
        self.pila_con_elementos.apilar(elemento)
        if self.pila_con_minimos.esta_vacia():
            self.pila_con_minimos.apilar(elemento)
        elif self.pila_con_minimos.ver_tope()>=elemento:
            self.pila_con_minimos.apilar(elemento)

    def desapilar(self):
        nro_desapilado=self.pila_con_elementos.desapilar()
        if nro_desapilado==self.pila_con_minimos.ver_tope():
            self.pila_con_minimos.desapilar()
        return nro_desapilado

    def obtener_minimo(self):
        return self.pila_con_minimos.ver_tope()

from pila import Pila

class PilaConMaximo:
    def __init__(self):
        self.pila_elementos=Pila()
        self.pila_maximos=Pila()

    def apilar(self,elemento):
        self.pila_elementos.apilar(elemento)
        if self.pila_maximos.esta_vacia():
            self.pila_maximos.apilar(elemento)
        elif self.pila_maximos.ver_tope()<=elemento:
            self.pila_maximos.apilar(elemento)

    def desapilar(self):
        if self.pila_elementos.esta_vacia():
            raise exception("la pila esta vacia")
        nro_desapilado=self.pila_elementos.desapilar()
        if self.pila_maximos.ver_tope()==nro_desapilado:
            self.pila_maximos.desapilar()

        return nro_desapilado

    def ver_tope(self):
        if self.pila_elementos.esta_vacia():
            raise exception("la pila esta vacia")
        else:
            return self.pila_elementos.ver_tope()

    def obtener_maximo(self):
        return self.pila_maximos.ver_tope()

        