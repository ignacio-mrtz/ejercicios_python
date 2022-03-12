# Ejercicio 12.4. Escribir una clase Caja para representar cuánto dinero hay en una caja de un
# negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la esquina hay 6 billetes
# de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos). Las denominaciones permitidas son 1, 2,
# 5, 10, 20, 50, 100, 200, 500 y 1000 pesos. Debe comportarse según el siguiente ejemplo:
# >>> c = Caja({500: 6, 300: 7, 2: 4})
# ValueError: Denominación "300" no permitida
# >>> c = Caja({500: 6, 100: 7, 2: 4})
# >>> str(c)
# 'Caja {500: 6, 100: 7, 2: 4} total: 3708 pesos'
# >>> c.agregar({250: 2})
# ValueError: Denominación "250" no permitida
# >>> c.agregar({50: 2, 2: 1})
# >>> str(c)
# 'Caja {500: 6, 100: 7, 50: 2, 2: 5} total: 3810 pesos'
# >>> c.quitar({50: 3, 100: 1})
# ValueError: No hay suficientes billetes de denominación "50"
# >>> c.quitar({50: 2, 100: 1})
# 200
# >>> str(c)
# 'Caja {500: 6, 100: 6, 2: 5} total: 3610 pesos'

class Caja:
    def __init__(self, diccionario):
        self.denominaciones_permitidas=[ 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
        self.billetes_en_negocio={}
        self.total_plata_en_negocio=0

        for clave in diccionario:
            if clave not in self.denominaciones_permitidas:
                raise ValueError(f"Denominación {clave} no permitida")

        for clave,valor in diccionario.items():
            if clave in self.denominaciones_permitidas:
                self.billetes_en_negocio[clave]=valor
                self.total_plata_en_negocio+=(valor*clave)

    def __str__(self):
        return f"Caja {self.billetes_en_negocio} total: {self.total_plata_en_negocio} pesos"

    def agregar(self,plata_a_agregar):#chequear
        for clave in plata_a_agregar:
            if clave not in self.denominaciones_permitidas:
                raise ValueError(f"Denominación {clave} no permitida")

        for clave,valor in plata_a_agregar.items():
            if clave in self.denominaciones_permitidas:
                self.billetes_en_negocio[clave]=self.billetes_en_negocio.get(clave,0)+valor
                self.total_plata_en_negocio+=(valor*clave)

    def quitar(self, plata_a_quitar):
        for clave in plata_a_quitar:
            if clave not in self.denominaciones_permitidas:
                raise ValueError(f"Denominación {clave} no permitida")
        
        for clave,valor in plata_a_quitar.items():
            if self.billetes_en_negocio[clave] < valor:
                raise ValueError(f"No hay suficientes billetes de denominación {clave}")

        for clave,valor in plata_a_quitar.items():
            self.billetes_en_negocio[clave]=self.billetes_en_negocio[clave]-valor
            self.total_plata_en_negocio-=(valor*clave)
            if self.billetes_en_negocio[clave]==0:
                self.billetes_en_negocio.pop(clave)
        


# Ejercicio 12.4. Escribir una clase Caja para representar cuánto dinero hay en una caja de un
# negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la esquina hay 6 billetes
# de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos). Las denominaciones permitidas son 1, 2,
# 5, 10, 20, 50, 100, 200, 500 y 1000 pesos. Debe comportarse según el siguiente ejemplo:
# >>> c = Caja({500: 6, 300: 7, 2: 4})
# ValueError: Denominación "300" no permitida
# >>> c = Caja({500: 6, 100: 7, 2: 4})
# >>> str(c)
# 'Caja {500: 6, 100: 7, 2: 4} total: 3708 pesos'
# >>> c.agregar({250: 2})
# ValueError: Denominación "250" no permitida
# >>> c.agregar({50: 2, 2: 1})
# >>> str(c)
# 'Caja {500: 6, 100: 7, 50: 2, 2: 5} total: 3810 pesos'
# >>> c.quitar({50: 3, 100: 1})
# ValueError: No hay suficientes billetes de denominación "50"
# >>> c.quitar({50: 2, 100: 1})
# 200
# >>> str(c)
# 'Caja {500: 6, 100: 6, 2: 5} total: 3610 pesos'

class Caja2:
    def __init__(self, billetes):
        self.billetes=validar_billetes(billetes)

    def __str__(self):
        total=0
        for key,valor in self.billetes.items():
            total+=key*valor
        return f"Caja {self.billetes} total: {total} pesos"

    def agregar(self,plata):
        plata=validar_billetes(plata)
        for key,value in plata.items():
            if key in self.billetes:
                self.billetes[key]=self.billetes[key] +value
            else:
                self.billetes[key]=value
    
    def quitar(self,plata):

            
            


def validar_billetes(billetes):
    for clave in billetes:
        if clave not in (1,2,5,10,20,50,100,200,500,1000):
            raise ValueError(f"Denominacion '{clave}' no permitida")
    return billetes








    

