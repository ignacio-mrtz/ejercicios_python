# Ejercicio 14.7. Escribir una función llamada tail que recibe un archivo y un número N e imprime
# las últimas N líneas del archivo. Durante el transcurso de la función no puede haber más de N
# líneas en memoria.


####HECHO EN CLASE###########
#Nota: Se encuentran disponibles los TDA Pila y Cola con sus métodos ya definidos en los archivos pila.py y cola.py #respectivamente.

from cola import Cola

def tail(ruta, N):
    with open(ruta) as f:
        cola = Cola()
        cont = 0
        for linea in f:
            linea = linea.rstrip("\n")
            cont += 1
            cola.encolar(linea)
            if cont > N:
                cola.desencolar()
        while not cola.esta_vacia():
            print(cola.desencolar())
            
#otra forma

def tail2(nombre_archivo, N):
    '''
    DOC: Completar
    '''
    cola=Cola()
    contador=0
    with open(nombre_archivo) as f:
        for linea in f:
            if contador>=N:
                cola.desencolar()
            linea=linea.rstrip("\n")
            contador+=1
            cola.encolar(linea)
        while not cola.esta_vacia():
            print(cola.desencolar())

def tail3(archivo,n):
    cola=Cola()
    contador=0
    with open(archivo) as f:
        for linea in f:
            linea=linea.rstrip("\n")
            if contador<n:
                contador+=1
                cola.encolar(linea)
            else:
                cola.desencolar()
                cola.encolar(linea)
    while not cola.esta_vacia():
        print(cola.desencolar())

#tail3("testeo.py",5)


##########OTRO####################
# Implementar una clase ColaConPrioridad que tiene los metodos:
    # - Encolar(dato)
    # - EncolarPrioritario(dato)
    # - Desencolar
    # - Esta vacia


class ColaConPrioridad:
    def __init__(self):
        self.comunes = Cola()
        self.prioritarios = Cola()

    def encolar(self, dato):
        self.comunes.encolar(dato)

    def encolarPrioritario(self, dato):
        self.prioritarios.encolar(dato)

    def desencolar(self):
        if not self.prioritarios.esta_vacia():
            return self.prioritarios.desencolar()
        return self.comunes.desencolar()

    def esta_vacia(self):
        return self.comunes.esta_vacia() and self.prioritarios.esta_vacia()

    def ver_primero(self):
        pass

######OTRO EJ HECHO EN CLASE#####
#NO PUSO ENUNCIADO

def invertir(self):
        if not self.prim or not self.prim.prox:
            return 
        pila = Pila()
        actual = self.prim
        while actual:
            pila.apilar(actual)
            actual = actual.prox
        
        actual = pila.desapilar()
        self.prim = actual
        while not pila.esta_vacia():
            actual.prox = pila.desapilar()
            actual = actual.prox
        actual.prox = None





