# Ejercicio 14.4. Juego de Cartas
# a) Crear una clase Carta que contenga un palo y un valor.
# b) Crear una clase Solitario que permita apilar las cartas una arriba de otra, pero sólo
# permita apilar una carta si es de un número inmediatamente inferior y de distinto palo
# a la carta que está en el tope. Si se intenta apilar una carta incorrecta, debe lanzar una
# excepción.

#el siguiente ej esta correcto(chequeado en rpl)

from pila import Pila

class Carta:
    def __init__(self,palo,valor):
        self.palo=palo
        self.valor=valor

class Solitario:
    def __init__(self):
        self.pila=Pila()
    
    def apilar(self,carta):
        pila=self.pila
        if pila.esta_vacia():
            pila.apilar(carta)
        else:
            carta_tope = pila.desapilar()
            palo = carta_tope.palo
            valor = carta_tope.valor
            if carta.valor + 1 == valor and carta.palo != palo:
                pila.apilar(carta_tope)
                pila.apilar(carta)
            else:
                raise Exception('Carta inválida')

#otra forma:

class Carta2:
    def __init__(self,palo,valor):
        self.palo=palo
        self.valor=valor
        self.prox=None
        

class Solitario2:
    def __init__(self):
        self.tope=None

    def apilar(self,carta):
        if self.tope==None:
            self.tope=carta
        elif self.tope.palo != carta.palo and (self.tope.valor - 1 == carta.valor):
            carta.prox=self.tope
            self.tope=carta
        else:
            raise Exception("carta invalida")




