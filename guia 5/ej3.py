# Ejercicio 5.3. Manejo de contraseñas
# a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario
# la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
# b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
# c) Modificar el programa anterior para que después de cada intento agregue una pausa
# cada vez mayor, utilizando la función sleep del módulo time.
# d) Modificar el programa anterior para que sea una función que devuelva si el usuario
# ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).

# def es_la_contraseña_correcta():
#     contraseña=5833
#     contraseña_ingresada=int(input("escriba su contraseña: "))
#     while contraseña != contraseña_ingresada:
#         contraseña_ingresada=int(input("contraseña erronea,ingresela nuevamente:"))

from time import sleep

def es_la_contraseña_correcta():
    contraseña=5833
    contraseña_ingresada=int(input("escriba su contraseña: "))
    for i in range (3):
        #le da 2 intentos mas
        sleep(2)
        if contraseña != contraseña_ingresada:
            if i==2:
                print("clave bloqueada")
                return False
            contraseña_ingresada=int(input("contraseña erronea,ingresela nuevamente:"))
        else:
            return True
        
es_la_contraseña_correcta()

