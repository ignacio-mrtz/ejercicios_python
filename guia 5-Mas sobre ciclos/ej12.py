# ejercicio 5.12: Escribir una función que dada la cantidad de ejercicios de un examen, y el porcentaje
# necesario de ejercicios bien resueltos necesario para aprobar dicho examen, revise un
# grupo de examenes. Para ello, en cada paso debe preguntar la cantidad de ejercicios resueltos
# por el alumno, indicando con un valor centinela que no hay más examenes a revisar. Debe mostrar
# por pantalla el porcentaje correspondiente a la cantidad de ejercicios resueltos respecto a la
# cantidad de ejercicios del examen y una leyenda que indique si aprobó o no.

def examen(cantidad_de_ejercicios, porcentaje_de_aprobacion):
    while True:
        ej_resueltos = int(input("cuantos ejercicios resolvió de manera correcta?: "))
        porcentaje = (ej_resueltos*100)/cantidad_de_ejercicios
        print("porcentaje de ejercicios correctos respecto del total: ", porcentaje,"%")
        if porcentaje>=porcentaje_de_aprobacion:
            print("aprobado")
        else:
            print("desaprobado")
        hay_mas = input("hay mas examenes para corregir?( si/no ): ")
        if hay_mas == "no":
            break

examen(20,60)






