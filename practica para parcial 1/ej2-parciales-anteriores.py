# Del primer recuperatorio del primer parcialito, primer cuatrimestre de 2013
# 3) Escribir una funcion que pida cadenas al usuario hasta que ingrese una cadena vacia.
# Debe devolver una lista de las palabras ingresadas. Por ejemplo:
# Cadena: hola co
# Cadena: mo
# Cadena: estas ?
# Cadena:
# Debe devolver: ['hola', 'como', 'estas', ' ?']

def main():
    cadenas_unidas=""
    while True:
        cadena=input("cadena: ")
        if cadena=="":
            break
        cadenas_unidas+=cadena
    return cadenas_unidas.split()

print(main())



        

