# Ejercicio 7.7. Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Inicial_segundo_nombre) y #devuelva una lista de cadenas donde cada una contenga primero el
# nombre, luego la inicial con un punto, y luego el apellido.

def main(lista_de_nombres):
    lista_nueva=[]
    for i in range(0,len(lista_de_nombres)):
        datos=list(lista_de_nombres[i])
        lista_nueva.append(datos[1]+" "+datos[2]+" "+datos[0])
    return lista_nueva 

print(main([("martinez","pedro","I"),("perez","lucia","M"),("garcia","pablo","J")]))

