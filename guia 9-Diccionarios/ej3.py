# Ejercicio 9.3. Continuación de la agenda.
# Escribir un programa que vaya solicitando al usuario que ingrese nombres.
# a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar
# el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
# b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# El usuario puede utilizar la cadena ”*”, para salir del programa.

def main(agenda):
    while True:
        nombre=input("ingrese un nombre a buscar en la agenda(ingrese * para no buscar ningun nombre mas): ")
        if nombre=="*":
            break
        if agenda.get(nombre,""):
            print(agenda[nombre])
            modificar=input("desea modificar el numero de telefono?(si/no): ")
            if modificar=="si":
                nuevo_numero=input("escribir nuevo numero: ")
                agenda[nombre]=nuevo_numero
        else:
            ingresar=input("el nombre no se encuentra. quiere ingresar un nro para dicha persona?(si/no): ")
            if ingresar=="si":
                nuevo_numero=input("ingrese el numero de telefono: ")
                agenda[nombre]=nuevo_numero
    return agenda
                
agenda={"juan": 43643543, "carlos":3153453, "ana":36757345, "jose": 256436546}
#agenda_modificada=main(agenda)
#print(agenda_modificada)



def mainb(agenda):
    while True:
        nombre=input("ingrese un nombre('*' para salir): ")
        if nombre=="*":
            break
        elif nombre in agenda:
            print(f"su telefono es: {agenda[nombre]}")
            correccion=input("si no es correcto ingrese un nuevo numero sino escriba '*' para continuar: ")
            if correccion!="*":
                agenda[nombre]=int(correccion)
        else:
            numero=int(input("no se encuentra en la agenda, ingrese el numero de telefono: "))
            agenda[nombre]=numero
    return agenda

print(mainb(agenda))


            
        
