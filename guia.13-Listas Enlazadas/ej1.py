#Ejercicio 13.1. Implementar el método __str__ de ListaEnlazada, para que se genere una salida legible de lo que contiene la lista, similar a las listas de python.
def es_par(nro):
    if nro%2==0:
        return True
    else:
        return False

class _Nodo:
    def __init__(self,dato, prox=None):
        self.dato=dato
        self.prox=prox


class ListaEnlazada:
    def __init__(self):
        """crea una lista enlazada vacia"""
        self.prim=None
        #cantidad de elementos de la lista
        self.len=0
    
    def append(self,dato):
        """agrega un elementos al final de la lista"""
        #creo un nuevo nodo con el dato que pasa el usuario
        nuevo=_Nodo(dato)

        if dato==None:
            raise ValueError("no ingresó ningun dato")
        
        #act appunta al elemento actual
        act=self.prim

        if act==None:
            #la lista esta vacia
            self.prim=nuevo
        else:
            #la lista no esta vacia
            while act.prox is not None:
                act=act.prox
            #aca estoy en el ultimo nodo de la lista
            act.prox=nuevo
        
        self.len+=1
        
    def __str__(self):
        L=[]
        act=self.prim
        while act is not None:
            L.append(str(act.dato))
            act=act.prox
        return "[" + ",".join(L) + "]"


    def __len__(self):
        return self.len
    

    def pop(self,i=None):
        """elimina y devuelve el elemento que está en la posicion i y si no se especifica la posicion elimina y devuelve el elemento en la ultima posicion.Por otro lado levanta una excepcion si hace referencia a una posicion no valida de la lista """

        if i==None:
            i=self.len - 1
        
        if i<0 or i>self.len-1:
            raise IndexError("Indice fuera de rango")
        
        if i==0:
            #guardo el dato para devolverlo despues
            dato=self.prim.dato
            #apunto el comienzo de la lista al segundo elemento
            self.prim=self.prim.prox
        else:
            #busca los nodos en las posiciones i-1 e i
            n_ant=self.prim
            n_act=n_ant.prox
            for pos in range(1,i):
                n_ant=n_act
                n_act=n_ant.prox
            #cuando termina el ciclo, el n_ant es el elemento i-1 de la lista y n_act es el elemento i
            #guardo el dato y elimino el nodo:
            dato=n_act.dato
            n_ant.prox=n_act.prox

        self.len-=1

        return dato

    def remove(self,x):
        """elimina la primera aparicion de x en la lista, o bien levanta una excepcion si x no esta en la lista"""
        if self.len==0:
            raise ValueError("Lista vacia")
        if self.prim.dato==x:
            self.prim=self.prim.prox
        else:
            #busca el nodo anterior al que contiene a x (n_ant)
            n_ant=self.prim
            n_act=n_ant.prox
            while n_act.dato!=x and n_act is not None:
                n_ant=n_act
                n_act=n_ant.prox
            
            if n_act==None:
                raise ValueError("el valor no esta en la lista")
            #descarto el nodo
            n_ant.prox=n_act.prox
        self.len-=1


    def insert(self,i,x):
        """agrega el elemento x en la posicion i. levanta una excepcion si la posicion i es invalida"""
        if self.len<i<0:
            raise IndexError("posicion invalida")
        nuevo=_Nodo(x)
        if i==0:
            nuevo.prox=self.prim
            self.prim=nuevo
        else:
            #itera hasta que n_ant sea el nodo i-1
            n_ant=self.prim
            for pos in range(1,i):
                n_ant=n_ant.prox
            #intercala el nuevo nodo
            nuevo.prox=n_ant.prox
            n_ant.prox=nuevo
        self.len+=1

    def extend(self,otralistaenlazada):
        """recibe una ListaEnlazada y agrega a la lista actual los elementos que se encuentran en la lista recibida."""
        act=self.prim

        if act is None:
            #la lista esta vacia
            self.prim=otralistaenlazada.prim

        while act.prox is not None:
            act=act.prox
        #aca act es el ultimo elemento
        act.prox=otralistaenlazada.prim

        self.len+=otralistaenlazada.len

    def remover_todos(self,elemento):
        """recibe un elemento y remueve de la lista todas las apariciones del mismo, devolviendo la cantidad de elementos removidos. La lista debe ser recorrida una sola vez."""

        contador=0

        if self.prim==None:
             raise ValueError("Lista vacia")

        while self.prim.dato==elemento:
            self.prim=self.prim.prox
            contador+=1
            self.len-=1

        ant=self.prim
        act=ant.prox
        
        while act is not None:
            if act.dato==elemento:
                ant.prox=act.prox
                act=act.prox
                contador+=1
                self.len-=1
                continue
            ant=act
            act=ant.prox

        return contador

    def duplicar(self,elemento):
        """recibe un elemento y duplica todas las apariciones del mismo."""
        ant=self.prim
        act=ant.prox
        
        while act is not None:
            if ant.dato==elemento:
                nuevo=_Nodo(elemento)
                ant.prox=nuevo
                nuevo.prox=act
            ant=act
            act=ant.prox
        #aca ant termina siendo el ultimo elemento y act es none

        if ant.dato==elemento:
            nuevo=_Nodo(elemento)
            ant.prox=nuevo
            nuevo.prox=None

    def duplicar2(self,x):
        ant=self.prim
        act=ant.prox
        while ant is not None:
            if ant.dato==x:
                nuevo=_nodo2(x)
                nuevo.prox=act
                ant.prox=nuevo
            ant=act
            if ant!=None:
                act=ant.prox    

    def filter(self,f):
        """recibe una función y devuelve una nueva lista enlazada con los elementos para los cuales la aplicación de f devuelve True. La nueva lista debe ser construida recorriendo los nodos una sola vez (es decir, no se puede llamar a append).
        Ejemplo:
        #L = 1 -> 5 -> 8 -> 8 -> 2 -> 8
        #L.filter(es_primo) -> L2 = 5 -> 2"""
        act=self.prim
        L_nueva=ListaEnlazada()
        act_de_lista_nueva=None
        while act is not None:
            if f(act.dato)==True:
                nuevo=_Nodo(act.dato)
                if L_nueva.prim==None:
                    L_nueva.prim=nuevo
                    act_de_lista_nueva=nuevo
                else:
                    nuevo=_Nodo(act.dato)
                    act_de_lista_nueva.prox=nuevo
                    act_de_lista_nueva=nuevo
            act=act.prox

        return L_nueva
    
    def filter2(self,f):
        nueva_lista=ListaEnlazada2()
        act_de_lista_nueva=None
        act=self.prim
        while act is not None:
            if f(act.dato)==True:
                nuevo=_nodo2(act.dato)
                if nueva_lista.prim==None:
                    nueva_lista.prim=nuevo
                    act_de_lista_nueva=nuevo
                else:
                    act_de_lista_nueva.prox=nuevo
                    act_de_lista_nueva=nuevo
            act=act.prox
        return str(nueva_lista)

    def invertir(self):
        """invierte el orden de la lista (es decir, el primer elemento queda como último y viceversa)"""
        ant = None
        act = self.prim
        while act:
            sig = act.prox
            act.prox = ant
            ant = act
            act = sig
        self.prim = ant

    def invertir2(self):
        if self.cant==1:
            return
        ant=self.prim
        act=ant.prox
        sig=act.prox

        ant.prox=None
        while sig is not None:
            act.prox=ant
            ant=act
            act=sig
            sig=sig.prox
        act.prox=ant
        self.prim=act

##############Hechos en clase#############################
    def eliminar_duplicados_consecutivos(self):
        if not self.prim:
            return
        actual = self.prim
        while actual.prox:
            if actual.dato == actual.prox.dato:
                actual.prox = actual.prox.prox
            else:
                actual = actual.prox

    def map(self, f):
        res = ListaEnlazada()
        actual = self.prim
        nuevo_anterior = None
        while actual:
            nuevo = Nodo(f(actual.dato))
            if not nuevo_anterior:
                nuevo_anterior = nuevo
                res.prim = nuevo
            else:
                nuevo_anterior.prox = nuevo
                nuevo_anterior = nuevo_anterior.prox
            actual = actual.prox
        return res
#############################################################
#PS C:\Users\juan ignacio\Desktop\resolucion guia de ejercicios Algo1-FIUBA\guia.13-Listas Enlazadas> python3 -i  ej1.py
#>>> L=ListaEnlazada()
#>>> L.append(35)
#>>> L.append(42)
#>>> str(L)
#'[35,42]'
#>>> len(L)
#2
#>>> L.remove(42)
#>>> str(L)
#'[35]'
#>>> L.pop()
#35
#>>> str(L)
#'[]'
#>>> L.insert(0,55)
#>>> str(L)
#'[55]'
#>>>

###################################################################################







            

        






            

            






        















