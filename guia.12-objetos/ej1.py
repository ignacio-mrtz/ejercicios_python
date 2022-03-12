# Ejercicio 12.1.

# a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos
# instantes de tiempo (números enteros expresados en segundos), con la condición desde < hasta.

# b) Implementar el método duracion que devuelve la duración en segundos del intervalo.

# c) Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo intervalo
# resultante de la intersección entre ambos, o lanzar una excepción si la intersección es nula.

# d) Implementar el método union que recibe otro intervalo. Si los intervalos no son adyacentes
# ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo intervalo resultante de la unión entre ambos.

class Intervalo:
    def __init__(self,desde,hasta):
        if desde<hasta:
            self.desde=validacion_nro_entero(desde)
            self.hasta=validacion_nro_entero(hasta)
        else:
            raise Exception(" no se cumple la condicion desde<hasta")

    def duracion(self):
        return self.hasta-self.desde

    def interseccion(self,otro):
        if self.desde<otro.desde<self.hasta and not self.desde<otro.hasta<self.hasta:
            return Intervalo(otro.desde,self.hasta)
        elif self.desde<otro.desde<self.hasta and self.desde<otro.hasta<self.hasta:
            return Intervalo(otro.desde, otro.hasta)
        elif otro.desde<self.desde<otro.hasta and otro.desde<self.hasta<otro.hasta:
            return Intervalo(self.desde, self.hasta)
        elif otro.desde<self.desde and otro.hasta<self.hasta:
            return Intervalo(self.desde, otro.hasta)
        else:
            raise Exception("La interseccion es nula")
        
    def union(self,otro):
        if Interseccion(self, otro) or self.desde==otro.hasta or self.hasta==otro.desde:
            #acá escribiria varios ifs como en el metodo interseccion y devolveria la union en cada caso.
        else:
            raise Exception("Los intervalos no son adyacentes ni se intersectan")

def validacion_nro_entero(valor):
    if not type(valor)="int":
        raise TypeError("el valor ingresado no es un nro entero")
    return int(valor)


#COMO TESTEO ESTO EN LA TERMINAL? ASI:
# python3 -i ej1.py
# >>> i1=Intervalo(5,25)
# >>> i2=Intervalo(10,30)
# >>> print(i1.interseccion(i2))
# <__main__.Intervalo object at 0x0000000001EB17C0>
# >>> intersec12=(i1.interseccion(i2))
# >>> intersec12
# <__main__.Intervalo object at 0x0000000001E22430>
# >>> intersec12.desde
# 10
# >>> intersec12.hasta
# 25
# >>> i3=Intervalo(5,25)
# >>> i4=Intervalo(30,50)
# >>> i3.interseccion(i4)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "ej1.py", line 33, in interseccion
#     raise Exception("La interseccion es nula")
# Exception: La interseccion es nula
# >>>






