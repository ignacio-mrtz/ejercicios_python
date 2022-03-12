# Ejercicio 14.1. Escribir una clase TorreDeControl que modele el trabajo de una torre de control de
# un aeropuerto con una pista de aterrizaje. Los aviones que están esperando para aterrizar tienen
# prioridad sobre los que están esperando para despegar. La clase debe funcionar conforme al
# siguiente ejemplo:
# >>> torre = TorreDeControl()
# >>> torre.nuevo_arribo('AR156')
# >>> torre.nueva_partida('KLM1267')
# >>> torre.nuevo_arribo('AR32')
# >>> torre.ver_estado()
# Vuelos esperando para aterrizar: AR156, AR32
# Vuelos esperando para despegar: KLM1267
# >>> torre.asignar_pista()
# El vuelo AR156 aterrizó con éxito.
# >>> torre.asignar_pista()
# El vuelo AR32 aterrizó con éxito.
# >>> torre.asignar_pista()
# El vuelo KLM1267 despegó con éxito.
# >>> torre.asignar_pista()
# No hay vuelos en espera.

from cola import Cola

class TorreDeControl:
    def __init__(self):
        self.esperando_para_aterrizar=Cola()
        self.esperando_para_despegar=Cola()

    def nuevo_arribo(self,dato):
        self.esperando_para_aterrizar.encolar(dato)

    def nueva_partida(self,dato):
        self.esperando_para_despegar.encolar(dato)

    def ver_estado(self):
        print("Vuelos esperando para aterrizar: ", end="")

        cola_auxiliar=Cola()

        while not self.esperando_para_aterrizar.esta_vacia():
            vuelo=self.esperando_para_aterrizar.desencolar()
            cola_auxiliar.encolar(vuelo)
            print(vuelo+",",end=" ")
        
        print("\n")
        
        while not cola_auxiliar.esta_vacia():
            self.esperando_para_aterrizar.encolar(cola_auxiliar.desencolar())

        print("Vuelos esperando para despegar: ", end="")

        while not self.esperando_para_despegar.esta_vacia():
            vuelo=self.esperando_para_despegar.desencolar()
            cola_auxiliar.encolar(vuelo)
            print(vuelo+",",end=" ")

        print("\n")
        
        while not cola_auxiliar.esta_vacia():
            self.esperando_para_despegar.encolar(cola_auxiliar.desencolar())


    def asignar_pista(self):
        if self.esperando_para_despegar.esta_vacia() and self.esperando_para_aterrizar.esta_vacia():
            print("No hay vuelos en espera.")
        elif not self.esperando_para_aterrizar.esta_vacia():
            dato=self.esperando_para_aterrizar.desencolar()
            print(f"El vuelo {dato} aterrizo con exito.")
        else:
            dato=self.esperando_para_despegar.desencolar()
            print(f"El vuelo {dato} despegó con exito.")

        


    







