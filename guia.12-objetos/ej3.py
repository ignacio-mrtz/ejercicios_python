# Ejercicio 12.3.
# a) Crear una clase Vector, que en su constructor reciba una lista de elementos que serán
# sus coordenadas. En el método __str__ se imprime su contenido con el formato [x,y,z]
# b) Implementar el método __add__ que reciba otro vector, verifique si tienen la misma
# cantidad de elementos y devuelva un nuevo vector con la suma de ambos. Si no tienen la
# misma cantidad de elementos debe levantar una excepción.
# c) Implementar el método __mul__ que reciba un número y devuelva un nuevo vector, con los elementos multiplicados por ese número.
 
class Vector:
    def __init__(self,lista_de_coordenadas):
         self.vector=lista_de_coordenadas

    def __str__(self):
        return f"{self.vector}"
    
    def __repr__(self):
        return self.__str__()

    def __add__(self,otro):
        suma=[]
        if len(self.vector)==len(otro.vector):
            for i in range(0,len(otro.vector)):
                suma.append(self.vector[i]+otro.vector[i])
            return Vector(suma)
        else:
            raise Exception("los vectores no tienen las misma cantidad de elementos entonces no se pueden sumar")

    def __mul__(self,nro):
        multiplicado=[]
        for i in range(0,len(self.vector)):
            multiplicado.append(self.vector[i]*nro)
        # y con esto ahora puedo:
        # >>> v3=Vector([2,5,6])
        # >>> v4=v3*3
        # >>> v4
        # [6, 15, 18]
        return Vector(multiplicado)



    


