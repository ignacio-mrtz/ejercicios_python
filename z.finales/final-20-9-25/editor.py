class Editor:
    "Representa el estado de un editor de texto."
    def __init__(self,contenido_del_archivo=None):
        if contenido_del_archivo=="" or contenido_del_archivo==None:
            contenido_del_archivo="\n"
        if contenido_del_archivo[-1:]!="\n":
            contenido_del_archivo=contenido_del_archivo+"\n"
        self.contenido_del_archivo=contenido_del_archivo
        self.posicion_cursor=(1,1)

    def cantidad_lineas(self):
        contador=0
        for c in self.contenido_del_archivo:
            if c=="\n":
                contador+=1
        return contador

    def __str__(self):
        return self.contenido_del_archivo

    def escribir_archivo(self,ruta_archivo):
        with open(ruta_archivo,"w", encoding="utf8") as f:
            f.write(self.contenido_del_archivo)
        #self.posicion_cursor=(self.cantidad_lineas,)

    def cursor_pos(self): 
        """Devuelve una tupla con el número de línea y columna del cursor."""
        return self.posicion_cursor

    def cursor_caracter(self): 
        """Devuelve el caracter sobre el cual el cursor está posicionado."""
        lista_de_lineas=self.contenido_del_archivo.split("\n")
        return lista_de_lineas[self.posicion_cursor[0]-1][self.posicion_cursor[1]-1]

    def mover_derecha(self): 
        """Mueve el cursor un caracter hacia la derecha. Si el cursor estaba en el último caracter de la línea, se moverá al primer caracter de la línea siguiente (en caso de ser posible)."""
        lista_de_lineas=self.contenido_del_archivo.split("\n")
        if self.posicion_cursor[0]==len(lista_de_lineas) and self.posicion_cursor[1]==len(lista_de_lineas[-1]):
            return
        elif self.posicion_cursor[1]==len(lista_de_lineas[self.posicion_cursor[0]-1]):
            self.posicion_cursor=(self.posicion_cursor[0]+1,1)
        else:
            self.posicion_cursor=(self.posicion_cursor[0],self.posicion_cursor[1]+1)

    def mover_izquierda(self):
        """ Mueve el cursor un caracter hacia la izquierda. Si el cursor estaba en el primer caracter de la línea, se moverá al último caracter de la línea anterior (en caso de ser posible)."""
        lista_de_lineas=self.contenido_del_archivo.split("\n")
        if self.posicion_cursor[0]==1 and self.posicion_cursor[1]==1:
            return
        elif self.posicion_cursor[1]==1:
            self.posicion_cursor=(self.posicion_cursor[0]-1,len(lista_de_lineas[self.posicion_cursor[0]-1]))
        else:
            self.posicion_cursor=(self.posicion_cursor[0],self.posicion_cursor[1]-1)

    def mover_arriba(self):
        """ Mueve el cursor un caracter hacia arriba. Si la línea de arriba es más corta que el número de columna actual, se posiciona el cursor en el último caracter."""
        lista_de_lineas=self.contenido_del_archivo.split("\n")
        if self.posicion_cursor[0]==1:
            return
        elif len(lista_de_lineas[self.posicion_cursor[0]]-1)>len(lista_de_lineas[self.posicion_cursor[0]-2]):
            self.posicion_cursor=(self.posicion_cursor[0]-1,len(lista_de_lineas[self.posicion_cursor[0]-1]))
        else:
            self.posicion_cursor=(self.posicion_cursor[0]-1,self.posicion_cursor[1])

    def mover_abajo(self): 
        """Mueve el cursor un caracter hacia abajo. Si la línea de abajo es más corta que el número de columna actual, se posiciona el cursor en el último caracter."""
        lista_de_lineas=self.contenido_del_archivo.split("\n")
        if self.posicion_cursor[0]==len(lista_de_lineas):
            return
        elif len(lista_de_lineas[self.posicion_cursor[0]])<len(lista_de_lineas[self.posicion_cursor[0]-1]):
            self.posicion_cursor=(self.posicion_cursor[0]+1,len(lista_de_lineas[self.posicion_cursor[0]-1]))
        else:
            self.posicion_cursor=(self.posicion_cursor[0]+1,self.posicion_cursor[1])

    def mover_a(self,linea,columna):
        """Recibe un número de línea y columna y mueve el cursor a esa posición.
Si la línea y/o columna están fuera de los límites, se ajustarán para que el cursor quede
en una posición válida."""
        lista_de_lineas=self.contenido_del_archivo.split("\n")
        if linea>self.cantidad_lineas:
            linea=self.cantidad_lineas
        if columna>len(lista_de_lineas[linea-1]):
            columna=len(lista_de_lineas[linea-1])

        self.posicion_cursor=(linea,columna)


def leer_archivo(ruta_archivo):
    nuevo_editor=Editor()
    nuevo_editor.contenido_del_archivo=""
    with open(ruta_archivo, encoding="utf8") as f:
        for linea in f:
            nuevo_editor.contenido_del_archivo+=linea
    return nuevo_editor










