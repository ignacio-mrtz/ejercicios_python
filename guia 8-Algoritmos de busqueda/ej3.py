# Ejercicio 8.3. Agenda simplificada
# Escribir una función que reciba una cadena a buscar y una lista de tuplas (nombre_completo,
# telefono), y busque dentro de la lista, todas las entradas que contengan en el nombre completo
# la cadena recibida (puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos).
# Debe devolver una lista con todas las tuplas encontradas.

def main(cadena,lista):
    lista_coincidencias=[]
    for x in lista:
        if cadena in x[0]:
            lista_coincidencias.append(x)
    return lista_coincidencias

print(main("mart", [("martin lopez",14351),("javier garcia",23453),("martina perez",35265),("dario martinez",3564)]))


