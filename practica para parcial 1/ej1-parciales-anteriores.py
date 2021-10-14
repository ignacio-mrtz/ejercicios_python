# Del primer parcialito del primer cuatrimestre de 2013
# 1) Escribir una funcion que reciba por parametro una lista de numeros y devuelva otra lista
# con los numeros de la ingresada que terminan en cero. Por ejemplo, si se recibe la lista: [4, 23,
# 40, -7, 0, 14, 1000, -760] debe devolver [40, 0, 1000, -760].

def main(lista_de_numeros):
    lista_nueva=[]
    for x in lista_de_numeros:
        if abs(x%10)==0:
            lista_nueva.append(x)
    return lista_nueva
            
print(main([4, 23, 40, -7, 0, 14, 1000, -760]))

