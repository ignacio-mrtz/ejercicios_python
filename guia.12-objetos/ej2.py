# Ejercicio 12.2.
# a) Crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se
# asignan en el constructor, y se imprimen como X/Y en el método __str__.
# b) Implementar el método __add__ que recibe otra fracción y devuelve una nueva fracción
# con la suma de ambas.
# c) Implementar el método __mul__ que recibe otra fracción y devuelve una nueva fracción
# con el producto de ambas.
# d) Crear un método simplificar que modifica la fracción actual de forma que los valores
# del dividendo y divisor sean los menores posibles.

import math

class Fraccion:
    def __init__(self,x,y):
        mcd=math.gcd(x,y) #con esto hago el ultimo pto de simplificar. esta funcion encuentra el maximo comun denominador entre ambos nros.
        self.dividendo=x//mcd # y aca divido ambos numeros por el mcd y simplifico la fraccion
        self.divisor=y//mcd

    def __str__(self):
        #con esta funcion yo puedo usar el print y me imprime lo que devuelvo aca
        #>>> f1=Fraccion(2,4)
        #>>> print(f1)
        #2/4
        #sino me devuelve algo como <__main__.Fraccion object at 0x0000000001E85CA0>
        #peeero si solo defino esta funcion y hago por ej:
        #>>> f1
        #<__main__.Fraccion object at 0x0000000001E85CA0>
        #me devuelve eso raro. pero a mi me gustaria que cuando escribo el nombre de mi variable me devuelva el valor. y para solcuionarlo uso la funcion __repr__. por lo que necesito ambos metodos
        return f"{self.dividendo}/{self.divisor}"

    def __repr__(self):
        return self.__str__() #tmb pude haber escrito str(self)
        #y ahora puedo hacer ambos:

        #>>> f1=Fraccion(2,5)
        #>>> f1
        #2/5
        #>>> print(f1)
        #2/5

    def __mul__(self,otra):
        return Fraccion(self.dividendo * otra.dividendo, self.divisor * otra.divisor)
        #y ahora yo puedo usar * para multiplicar:
        # >>> f1=Fraccion(2,6)
        # >>> f2=Fraccion(3,7)
        # >>> f3=f1*f2
        # >>> f3
        # 6/42
    
    def __add__(self,otra):
        if self.divisor==otra.divisor:
            return Fraccion(self.dividendo+otra.dividendo,self.divisor)
        else:
            return Fraccion(self.dividendo*otra.divisor+self.divisor*otra.dividendo,self.divisor*otra.divisor)


#entonces ahora puedo:
    # PS C:\Users\juan ignacio\Desktop\resolucion guia de ejercicios Algo1-FIUBA\guia.12-objetos> python3 -i ej2.py
        # >>> f1=Fraccion(2,5)
        # >>> f1
        # 2/5
        # >>> print(f1)
        # 2/5
        # >>> f2=Fraccion(3,4)
        # >>> f12=f1+f2
        # >>> f12
        # 23/20

#HABIENDO AGREGADO EL MCD AHORA PASA ESTO:

# PS C:\Users\juan ignacio\Desktop\resolucion guia de ejercicios Algo1-FIUBA\guia.12-objetos> python3 -i ej2.py
# >>> f1=Fraccion(2,6)
# >>> f1
# 1/3
# >>> f2=Fraccion(4,8)
# >>> f2
# 1/2
# >>> f1*f2
# 1/6






