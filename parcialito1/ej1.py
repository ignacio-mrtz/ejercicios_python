#1. Escribir una función que, dada una lista de tuplas de la forma (valor, indice), devuelva una nueva lista generada con cada valor en su respectivo índice, donde el resto de los índices que no tienen un valor asociado se les asignará un 0.
#Por ejemplo, para la lista de tuplas [(4, 1), (9, 6), (13, 3)] debe devolverse la lista [0, 4, 0, 13, 0, 0, 9].
#Nota: El mayor índice de la lista de tuplas corresponde al último índice de la lista final. En el ejemplo el mayor índice era 6, y el resultado tiene 7 elementos.
#Nota 2: Puede asumirse que no hay índices repetidos en las tuplas.

def main(valores_e_indices):
    maximo=0
    for i in range(0,len(valores_e_indices)):
        if valores_e_indices[i][1]>maximo:
            maximo=valores_e_indices[i][1]

    nueva_lista=[]

    for i in range(0,maximo+1):
        for j in range(0,len(valores_e_indices)):
            if i==valores_e_indices[j][1]:
                nueva_lista.append(valores_e_indices[j][0])
        if len(nueva_lista)<i+1 or len(nueva_lista)==0:
            nueva_lista.append(0)

    return nueva_lista



