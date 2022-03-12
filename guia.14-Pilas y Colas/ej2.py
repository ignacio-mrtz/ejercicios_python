# Ejercicio 14.2. Escribir las clases Impresora y Oficina que permita modelar el funcionamiento
# de un conjunto de impresoras conectadas en red.
# Una impresora:
# • Tiene un nombre, y una capacidad máxima de tinta.
# • Permite encolar un documento para imprimir (recibiendo el nombre del documento).
# • Permite imprimir el documento que está al frente de la cola.
# – Si no hay documentos encolados, se muestra un mensaje informándolo.
# – Si no hay tinta suficiente, se muestra un mensaje informándolo.
# – En caso contrario, se muestra el nombre del documento, y se gasta 1 unidad de tinta.
# • Permite cargar el cartucho de tinta
# Una oficina:
# • Permite agregar una impresora
# • Permite obtener una impresora por nombre
# • Permite quitar una impresora por nombre
# • Permite obtener la impresora que tenga menos documentos encolados.
# Ejemplo:
# >>> o = Oficina()
# >>> o.agregar_impresora(Impresora('HP1234', 1))
# >>> o.agregar_impresora(Impresora('Epson666', 5))
# >>> o.impresora('HP1234').encolar('tp1.pdf')
# >>> o.impresora('Epson666').encolar('tp2.pdf')
# >>> o.impresora('HP1234').encolar('tp3.pdf')
# >>> o.obtener_impresora_libre().encolar('tp4.pdf') # se encola en Epson666
# >>> o.impresora('HP1234').imprimir()
# tp1.pdf impreso
# >>> o.impresora('HP1234').imprimir()
# No tengo tinta :(
# >>> o.impresora('HP1234').cargar_tinta()
# >>> o.impresora('HP1234').imprimir()
# tp3.pdf impreso

class _Nodo:
    def __init__(self,dato,prox=None):
        self.dato=dato
        self.prox=prox

class Impresora:
    def __init__(self,nombre, capacidad_max_de_tinta):
        self.nombre=nombre
        self.capacidad_max_de_tinta=capacidad_max_de_tinta
        self.primero=None
        self.ultimo=None
        self.cant=0

    def encolar(self,doc):
        nuevo = _Nodo(doc)
        if self.ultimo==None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.prox = nuevo
            self.ultimo = nuevo

    def imprimir(self):
        if self.primero is None:
            print("la impresora no tiene nada que imprimir")
            return
        if self.capacidad_max_de_tinta==0:
            print("No tengo tinta :(")
            return
        archivo = self.primero.dato
        self.primero = self.primero.prox
        if not self.primero:
            self.ultimo = None
        print(f"{archivo} impreso")
        self.capacidad_max_de_tinta-=1

    def cargar_tinta(self):
        self.cargar_tinta=5

class Oficina:
    def __init__(self):
        self.impresoras=[]

    def agregar_impresora(self,impresora):
        self.impresoras.append(impresora)

    def impresora(self,nombre):
        for x in self.impresoras:
            if x.nombre==nombre:
                return x
        raise Exception("no hay impresoras con dicho nombre")

    def obtener_impresora_libre(self):
        ...


