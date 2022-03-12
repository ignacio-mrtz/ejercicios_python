class AeroDB:
    "AeroDB es una base de datos de aeropuertos y rutas"
    def __init__(self):
        self.aeropuertos={}
        self.rutas=[]

    def aeropuerto_agregar(self,designacion,nombre,ciudad,pais,latitud,longitud):
        for clave in self.aeropuertos:
            if clave==designacion:
                return
        self.aeropuertos[designacion]=[nombre,ciudad,pais,latitud,longitud]

    def cantidad_aeropuertos(self):
        return len(self.aeropuertos)

    def aeropuerto_get_nombre(self,designacion):
        return self.aeropuertos[designacion][0]

    def aeropuerto_get_ciudad(self,designacion):
        return self.aeropuertos[designacion][1]

    def aeropuerto_get_pais(self,designacion):
        return self.aeropuertos[designacion][2]

    def aeropuerto_get_coords(self,designacion):
        return (self.aeropuertos[designacion][3],self.aeropuertos[designacion][4])

    def ruta_agregar(self,codigo_de_vuelo,designacion_origen,designacion_destino):
        terna=(codigo_de_vuelo,designacion_origen,designacion_destino)
        for r in self.rutas:
            if r==terna:
                return
        self.rutas.append(terna)

    def cantidad_rutas(self):
        return len(self.rutas)

    def rutas_desde_ciudad(self,ciudad):
        lista=[]
        for r in self.rutas:
            if self.aeropuertos[r[1]][1]==ciudad:
                lista.append(r)
        return lista
    
    def rutas_hacia_ciudad(self,ciudad):
        lista=[]
        for r in self.rutas:
            if self.aeropuertos[r[2]][1]==ciudad:
                lista.append(r)
        return lista
    
    def aeropuerto_con_mas_rutas(self):
        diccionario={}
        for x in self.rutas:
            diccionario[x[1]]=diccionario.get(x[1],0)+1
            diccionario[x[2]]=diccionario.get(x[2],0)+1
        cantidad_mas_rutas=0
        designacion=""
        for key,value in diccionario.items():
            if value>cantidad_mas_rutas:
                cantidad_mas_rutas=value
                designacion=key
        return (designacion,cantidad_mas_rutas)

    def aeropuertos_ordenados_por_distancia(self,latitud,longitud):
        lista=[]
        for designacion,value in self.aeropuertos.items():
            distancia=((value[3]-latitud)**2+(value[4]-longitud)**2)**1/2
            lista.append((distancia,designacion))
        lista.sort()
        print(lista)
        lista_definitiva=[]
        for x in lista:
            lista_definitiva.append(x[1])
        return lista_definitiva 

    def armar_itinerario(self,ciudad_origen,ciudad_destino):
        R=[]# lista R de rutas que conforman un itinerario posible a partir de la ciudad origen
        V=[]
        return self._armar_itinerario(ciudad_origen,ciudad_destino,R,V)


    def _armar_itinerario(self,ciudad_origen,ciudad_destino,R,V):
        C=""
        if R==[]:
            C=ciudad_origen
        else:
            C=self.aeropuertos[R[-1][-1]][1]#C ES LA CIUDAD EN LA QUE ESTAMOS PARADOS ACTUALMENTE
        V.append(C)# V ES LA LISTA DE CIUDADES VISITADAS
        if C==ciudad_destino:
            return R
        else:
            for r in self.rutas:
                if self.aeropuertos[r[1]][1]==C and self.aeropuertos[r[2]][1] not in V:
                    R=R+[r]
                    _armar_itinerario(self.aeropuertos[r[2]],ciudad_destino,R,V)


#aeropuertos[designacion]=[nombre,ciudad,pais,latitud,longitud]
#ruta=(codigo_de_vuelo,designacion_origen,designacion_destino)

# devuelve[(código_0, origen, destino_0), ..., (código_n, origen_n, destino)].
# Devuelve None si no hay ningún itinerario posible entre ambas ciudades.
# Si hay más de un itinerario posible, es indistinto cuál de ellos es devuelto.

def cargar(ruta_archivo_aeropuertos,ruta_archivo_rutas):
    instancia=AeroDB()
    with open(ruta_archivo_aeropuertos, encoding="utf8") as f:
        for linea in f:
            linea=linea.rstrip("\n")
            linea=linea.split("|")
            instancia.aeropuerto_agregar(linea[0],linea[1],linea[2],linea[3],linea[4],linea[5])
    with open(ruta_archivo_rutas, encoding="utf8") as f:
        for linea in f:
            linea=linea.rstrip("\n")
            linea=linea.split("|")
            instancia.ruta_agregar(linea[0],linea[1],linea[2])
    return instancia


