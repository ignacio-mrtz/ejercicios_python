class Tuiter:
    "Modela el funcionamiento de una plataforma sospechosamente similar a Twitter"
    def __init__(self):
        self.autores={}
        self.tuits={}
        self.autores_ID=0
        self.tuits_ID=0
    
    def crear_autor(self, autor):
        self.autores_ID+=1
        self.autores[self.autores_ID]=[autor,[]]
        return self.autores_ID

    def publicar(self, id_del_autor, msj):
        self.tuits_ID+=1
        self.tuits[self.tuits_ID]=[id_del_autor, self.autores[id_del_autor][0], msj,[]]
        self.autores[id_del_autor][1].append(self.tuits[self.tuits_ID])
        return self.tuits_ID

    def compartir(self, id_de_tuit, id_de_autor_que_comparte):
        #{1:[juan,[lista de listas de tuits]], 2:[pedro,[]]}
        #{1:[id autor, nombre_autor, "msj tuit"]}
        if self.tuits[id_de_tuit][0]==id_de_autor_que_comparte:
            return False
        else:
            self.autores[id_de_autor_que_comparte][1].append(self.tuits[id_de_tuit])
            return True

    def tuit_id_autor(self, id_de_un_tuit):
        for id_autor in self.autores:
            if self.tuits[id_de_un_tuit] in self.autores[id_autor][1]:
                return id_autor

    def tuit_mensaje(self, id_de_un_tuit):
        return self.tuits[id_de_un_tuit][2]

    def muro_cantidad(self,id_de_un_autor):
        return len(self.autores[id_de_un_autor][1])

    def muro_id_tuit(self,id_de_un_autor,posicion_p):
        for clave in self.tuits:
            if self.tuits[clave]==self.autores[id_de_un_autor][1][posicion_p]:
                return clave

    def muro_escribir_csv(self, id_de_un_autor, archivo):
        with open(archivo,"w") as f:
            f.write("autor|mensaje\n")
            for x in self.autores[id_de_un_autor][1]:
                f.write(f"{x[1]}|{x[2]}\n")

    def tuits_mas_compartidos(self):
        diccionario={}
        for i in range(1,(self.tuits_ID)+1):
            for key,value in self.autores.items():
                for x in value[1]:
                    if self.tuits[i]==x:
                        diccionario[i]=diccionario.get(i,-1)+1 #-1 xq descuento de entrada los tuits originales que no los tomo como compartidos
        lista=list(diccionario.items())
        return sorted(lista, key=lambda data:data[1], reverse=True)

    def tuit_dar_like(self, id_tuit, id_autor):
        if self.tuits[id_tuit][0]==id_autor:
            return False
        elif id_autor in self.tuits[id_tuit][3]:
            return False
        else:
            self.tuits[id_tuit][3].append(id_autor)
            return True

    def tuit_fue_likeado_por(self, id_tuit, id_autor):
        if id_autor in self.tuits[id_tuit][3]:
            return True
        else:
            return False
            

#{1:[juan,[lista de listas de tuits]], 2:[pedro,[]]}
#{1:[id autor, nombre_autor, "msj tuit", [ids de los autores que dieron like]]}

#Un autor tiene, como mínimo:
#• Un número identificatorio único (el ID del autor)
#• Un nombre
#• Un muro (explicado abajo)
#Un tuit tiene, como mínimo:
#• Un número identificatorio único (el ID del tuit)
#• El ID del autor del tuit
#• Un mensaje