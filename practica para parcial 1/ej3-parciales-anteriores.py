# Del segundo recuperatorio del primer parcialito, primer cuatrimestre de 2013
# 3) Escribir una funcion que reciba una palabra y devuelva una lista con todas las rotaciones
# de esa palabra. Por ejemplo, si recibe: 'rotar', debe devolver:
# ['rotar','otarr','tarro','arrot','rrota']

def main(palabra):
    lista=[]
    for i in range(len(palabra)):
        cadena_con_rotacion=palabra[i:len(palabra)] + palabra[0:i]
        lista.append(cadena_con_rotacion)
    return lista

print(main("rotar"))


