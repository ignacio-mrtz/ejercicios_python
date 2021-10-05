# Ejercicio 7.2. Dominó.
# a) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
# recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)
# b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
# recibidas en una cadena, por ejemplo: 3-4 2-5. Nota: utilizar la función split de las
# cadenas.

def fichas_de_domino_encajan(tupla1, tupla2):
    if tupla1[0]==tupla2[0] or tupla1[0]==tupla2[1] or tupla1[1]==tupla2[1] or tupla1[1]==tupla2[0] :
        return True
    else:
        return False

#print(fichas_de_domino_encajan((1,2),(3,4)))

def fichas_de_domino_encajan2(string1,strin2):
    lista1 = string1.split("-")
    lista2 = strin2.split("-")
    if lista1[0]==lista2[0] or lista1[0]==lista2[1] or lista1[1]==lista2[1] or lista1[1]==lista2[0] :
        return True
    else:
        return False

print(fichas_de_domino_encajan2("1-4","4-5"))



