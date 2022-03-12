# Ejercicio 14.3. En la parada del colectivo 130 pueden ocurrir dos eventos diferentes:
# • Llega una persona
# • Llega un colectivo con 𝑛 asientos libres, y se suben al mismo todas las personas que están
# esperando, en orden de llegada, hasta que no quedan asientos libres.
# Cada evento se representa con una tupla que incluye:
# • El instante de tiempo (cantidad de segundos desde el inicio del día)
# • El tipo de evento, que puede ser 'p' (persona) o 'c' (colectivo).
# • En el caso de un evento de tipo 'c' hay un tercer elemento que es la cantidad de asientos
# libres.
# Escribir una función que recibe una lista de eventos, ordenados cronológicamente, y devuelva
# el promedio de tiempo de espera de los pasajeros en la parada.
# Ejemplo:
# promedio_espera([(35,'p'), (43,'p'), (80,'c',1), (98,'p'), (142,'c',2)])
# -> 62.6667 (calculado como (45+99+44) / 3)

###el siguiente está correcto(chequeado en rpl)

from cola import Cola

def promedio_espera(eventos):
    cola=Cola()
    pasajeros=0
    tiempo_total=0
    for evento in eventos:
        if evento[1]=="p":
            cola.encolar(evento)
            pasajeros+=1
        if evento[1]=="c":
            asientos_libres=evento[2]
            tiempo_llegada_colectivo=evento[0]
            while asientos_libres>0 and cola.esta_vacia() == False:
                tiempo_llegada_pasajero,_=cola.desencolar()
                tiempo_espera_del_pasajero=tiempo_llegada_colectivo-tiempo_llegada_pasajero
                tiempo_total+=tiempo_espera_del_pasajero
                asientos_libres-=1
    return tiempo_total/pasajeros


#otra resolucion que verifiqué en rpl(me gusta mas)

from cola import Cola
def promedio_espera_2(eventos):
    tiempo_espera_total=0
    subidos=0
    cola=Cola()
    for i,evento in enumerate(eventos):
        if evento[1]=="p":
            cola.encolar(evento[0])
        elif evento[1]=="c":
            asientos_libres=evento[2]
            for i in range(0,asientos_libres):
                if cola.esta_vacia():
                    continue
                segundos_pasajero=cola.desencolar()
                tiempo_espera_total+=(evento[0]-segundos_pasajero)
                subidos+=1
    return tiempo_espera_total/subidos

#otra forma:

def promedio_espera_3(lista_de_eventos):
    cola_pasajeros=Cola()
    tiempo=0
    pasajeros=0
    for x in lista_de_eventos:
        if x[1]=="p":
            cola_pasajeros.encolar(x)
        elif x[1]=="c":
            for i in range(0,x[2]):
                if cola_pasajeros.esta_vacia():
                    break
                pasajero=cola_pasajeros.desencolar()
                tiempo+=(x[0]-pasajero[0])
                pasajeros+=1
    return tiempo/pasajeros


print(promedio_espera_3([(35,'p'), (43,'p'), (80,'c',1), (98,'p'), (142,'c',2)]))