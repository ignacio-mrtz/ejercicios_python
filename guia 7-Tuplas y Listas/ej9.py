# Ejercicio 7.9. Escribir una función empaquetar para una lista, donde epaquetar significa indicar
# la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones). Por
# ejemplo, empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3), (3, 1), (5, 1), (1, 2), (3, 2)].

def empaquetar(lista):
    nueva_lista=[]
    repeticiones=1
    for i in range(1,len(lista)):
        if lista[i]==lista[i-1]:
            repeticiones+=1
            if i==len(lista)-1:
                nueva_lista.append((lista[i-1],repeticiones))
        else:
            nueva_lista.append((lista[i-1],repeticiones))
            repeticiones=1
            if i==len(lista)-1:
                nueva_lista.append((lista[i],repeticiones))

    return nueva_lista


print(empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 2]))


def empaquetar2(lista):
    nueva_lista=[]
    contador=0
    for i in range(0,len(lista)):
        if i==len(lista)-1 or lista[i]!=lista[i+1] :
            contador+=1
            nueva_lista.append((lista[i],contador))
            contador=0
        else:
            contador+=1
    return nueva_lista

print(empaquetar2([1, 1, 1, 3, 5, 1, 1, 3, 2]))

