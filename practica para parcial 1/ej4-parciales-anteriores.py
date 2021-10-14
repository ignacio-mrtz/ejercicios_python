# Del primer recuperatorio del primer parcialito, primer cuatrimestre de 2014
# 2) Escribir un programa que pida al usuario que ingrese un total de 16 numeros, y luego los imprima en 4 columnas # y 4 filas.
# 3) Escribir una funcion que reciba dos secuencias y devuelva una lista con los elementos comunes a ambas, sin #repetir ninguno.
# Ejemplo: f([7, 9, 7, 1], [6, 9, 7]) ->[7, 9]

def main2():
    while True:
        numero=input("ingrese un total de 16 nros: ")
        if len(numero)==16 and numero.isdigit()==True:
            break
        else:
            print("ingrese correctamente un total de 16 digitos")
    for i in range(0,16):
        if (i+1)%4==0 and i!=0:
            print(numero[i],"\n")
        else:
            print(numero[i], end=" ")

#print(main2())

def main3(secuencia1,secuencia2):
    coincidencias=[]
    for i in range(0,len(secuencia1)):
        for j in range(0,len(secuencia2)):
            if secuencia1[i]==secuencia2[j] and (secuencia2[j] not in coincidencias) :
                coincidencias.append(secuencia2[j])
    print(coincidencias)

main3([7, 9, 7, 1], [6, 9, 7])

        

    

        



