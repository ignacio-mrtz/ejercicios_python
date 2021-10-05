# Ejercicio 7.3. Campaña electoral
# a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima
# el mensaje Estimado <nombre>, vote por mí.
# b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una
# cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir
# de la posición p.
# c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario,
# para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género.

def estimado(nombres):
    for x in nombres:
        print("Estimado",x,"vote por mí")

#estimado(("carlos","josé","mariano"))

def estimado2(nombres,p,n):
    for i,x in enumerate(nombres):
        if p-1<=i<p-1+n:
            print("Estimado",x,"vote por mí")

#estimado2(("carlos","josé","mariano","juan","pedro","sebastian","lucas","rodrigo","marcelo"),4,3)

#####################################################

def estimado3(nombres):
    for x in nombres:
        if x[1]=="m":
            print("Estimado",x[0],"vote por mí")
        else:
           print("Estimada",x[0],"vote por mí") 

#estimado3((("carlos","m"),("josé","m"),("lucia","f"),("mariano","m")))


def estimado4(nombres,p,n):
    for i,x in enumerate(nombres):
        if p-1<=i<p-1+n and x[1]=="m":
            print("Estimado",x[0],"vote por mí")
        elif p-1<=i<p-1+n and x[1]=="f":
            print("Estimada",x[0],"vote por mí")

estimado4((("carla","f"),("josé","m"),("mariana","f"),("juana","f"),("pedro","m"),("sebastian","m"),("luciana","f"),("rodrigo","m"),("marcelo","m")),4,3)
    

