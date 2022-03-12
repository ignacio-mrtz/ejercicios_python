class Imagen:
    "Representa una imagen digital"
    def __init__(self, valor_max, ancho, alto):
        self.valor_max=valor_max
        self.ancho=ancho
        self.alto=alto
        coordenadas={}
        for i in range(0,ancho):
            for j in range(0,alto):
                coordenadas[(i, j)]=(0, 0, 0)
        self.imagen=coordenadas

    def get_valor_max(self):
        return self.valor_max
    def get_ancho(self):
        return self.ancho
    def get_alto(self):
        return self.alto

    def get(self,x, y):
        if (x, y) in self.imagen:
            return self.imagen[(x, y)]
        else:
            return (0, 0, 0)

    def set(self,x,y,color):
        if 0<=x<self.ancho and 0<=y<self.alto:
            c1,c2,c3=color
            if c1<0:
                c1=0
            elif c1>255:
                c1=255
            if c2<0:
                c2=0
            elif c2>255:
                c2=255
            if c3<0:
                c3=0
            elif c3>255:
                c3=255
            color=(c1, c2, c3)
            self.imagen[(x,y)]=color

    def pintar(self,color):
        for key in self.imagen:
            self.imagen[key]=color

    def escribir_ppm(self, nombre_archivo):
        with open(nombre_archivo,"w") as f:
            f.write("P3\n")
            f.write(f"{self.ancho} {self.alto}\n")
            f.write(f"{self.valor_max}\n")
            for j in range(0,self.alto):
                for i in range(0,self.ancho):
                    c1,c2,c3=self.imagen[(i, j)]
                    f.write(f"{c1} {c2} {c3}  ")
                f.write(" \n")

    def histograma(self):
        histograma={}
        for key, color in self.imagen.items():
            histograma[color]=histograma.get(color,0)+1
        return histograma

    def colores_mas_frecuentes(self):
        histograma=self.histograma()
        lista=list(histograma.items())
        lista.sort(key=lambda x:x[1])
        lista=lista[::-1]
        return lista

    def promedio(self):
        red=0
        green=0
        blue=0
        for r,g,b in self.imagen.values():
            red+=int(r)
            green+=int(g)
            blue+=int(b)
        cantidad=self.ancho*self.alto
        color_promedio=(red//cantidad, green//cantidad, blue//cantidad)
        return color_promedio

    def balde_de_pintura(self,x,y,c):
        if self.imagen[(x,y)]==c:
            return
        self.imagen[(x,y)]=c
        if (x+1,y) in self.imagen and self.imagen[(x+1,y)] != c:
            self.balde_de_pintura(x+1,y,c)
        if (x-1,y) in self.imagen and self.imagen[(x-1,y)] !=c:
            self.balde_de_pintura(x-1,y,c)
        if (x,y+1) in self.imagen and self.imagen[(x,y+1)] !=c:
            self.balde_de_pintura(x,y+1,c)
        if (x,y-1) in self.imagen and self.imagen[(x,y-1)] !=c:
            self.balde_de_pintura(x,y-1,c)
        

        










def leer_ppm(nombre_archivo):
    with open(nombre_archivo) as f:
        next(f)
        tamaño=f.readline()
        tamaño=tamaño.rstrip("\n")
        ancho,alto=tamaño.split(" ")
        ancho=int(ancho)
        alto=int(alto)
        valor_max=f.readline()
        valor_max=int(valor_max.rstrip("\n"))
        print(valor_max)
        imagen_leida=Imagen(valor_max, ancho,alto)
        nro_de_linea=0
        for linea in f:
            linea=linea.rstrip("\n")
            colores_en_linea=linea.split("   ")
            for i in range(len(colores_en_linea)):
                actual=colores_en_linea.pop(0).split(" ")
                final=[]
                for x in actual:
                    if x!=" " and x!="":
                        final.append(int(x))
                imagen_leida.set(i,nro_de_linea,tuple(final))
            nro_de_linea+=1
        return imagen_leida




    







