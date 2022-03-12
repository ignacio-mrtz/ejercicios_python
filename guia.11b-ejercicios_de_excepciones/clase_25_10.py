# Le pedi al usuario que ingrese un nro entero, si no ingresa algo valido lo vuelve a pedir

def pedir_entero():
    while True:
        numero = input("ingresa un nro entero campeon: ")
        try:
            return int(numero)
        except ValueError:
            print("Ingresa algo valido")

# Implementar una función que dado la ruta de un archivo de la forma <película>;<año>;<actor1,actor2,...> devuelva un diccionario donde cada actor tenga asociado una lista con todos los años en los que actuó (puede haber años repetidos). Cualquier línea con datos inválidos (cualquier campo vacío, año no es un número) debe ser ignorada. Se puede suponer que todas las líneas contienen siempre tres elementos separados por ;.

import csv

def años_por_actor(ruta):
    """..."""
    res = {}
    try:
        with open(ruta) as archivo:
            for linea in archivo:
                pelicula, año, actores = linea.rstrip("\n").split(";")#pelicula es el 1er elemento,año el 2do y actores es el 3ero con todos los actores separados por una coma. es decir es una lista de un elemento
                if not pelicula or not año or not actores:#si hay algun campo vacio salteate la linea y esto tmb chequea que todas las lineas tengan 3 elementos. si esto no chequeara lo ultimo habria que meter la linea 24 dentro de un try y meter un except
                    continue
                # if not año.isnumeric():
                #     continue
                try:#chequeo que el año es un numero que puedo pasar a int sino agarra la excepcion 
                    año = int(año)#antes de guardarlos en el diccionario paso los años de str a int
                except ValueError:
                    raise ArchivoConFormatoInvalidoError
                for actor in actores.split(","):
                    if año in res.get(actor, []): # if actor in res and año in res[actor] #para que no haya años repetidos
                        continue
                    res[actor] = res.get(actor, []) + [año]#si la clave con el nombre del actor tiene asociada un año anterior, lo devuelve y le agrega el año nuevo y si la clave no tiene ningun valor asociado, crea una lista vacia y le suma el año nuevo(tmb se puede hacer todo esto con append)
    except (FileNotFoundError, IOError) as e:
        # adadfasd
        # si el archivo no existe o hay un error de input output, atrapamos la excepcion y hacemos el siguiente rise para comunicar lo que falló
        raise ProblemaConArchivoError("")

    return res

import interaccion #acá simula importar un  modulo llamado interaccion sobre interaccion con el usuario

#modularizamos el problema. el siguiente es el modulo main, el modulo principal
def main():
    try:
        años_por_actor("pelis.csv")
    except ProblemaConArchivoError as e:#ac levantamos la excepcion que lanzaria la funcion años_por_actor.esta es una forma de informarle los errores a modulos de mas arriba y que lo puedan manejar
        # adadfasd
        interaccion.informar_error(e)
    except ArchivoConFormatoInvalidoError:
        # adfasdf
        interaccion.informar_error("El archivo tenia un formato invalido")#envio este msj al modulo interaccion

#en todo el codigo que estuvo escribiendo hasta aca usa excepciones que serian creadas por el(se ve en la proxima clase). aca las usa como si ya las hubiera creado





# de la siguiente forma es como lo hago usando el modulo csv(import csv)

# como manejar archivos facilmente en python:
# 
# los files csv son muy usados en la industria xq se adaptan facilmente a muchos otros formatos.
# 
# es el formato estandard, es el que se usa en casi todos los lenguajes.
# 
# entonces python ofrece facilidades para manejar ese tipo de files
# 
# eso se hace con el modulo csv:
# 
# import csv (csv significa: coma separated values)
# 
# este nos va a dar funciones para leer y parcear los archivos csv mas facilmente

def años_por_actor(ruta):
    """..."""
    res = {}
    with open(ruta) as archivo:
        # reader = csv.reader(archivo, delimiter=';') #Este reader funcionaria muy parecido al "archivo" que teniamos, se lo puede iterar( con for linea in reader) pero linea no es una cadena de texto sino que va a ser una lista con cada uno de los campos de mi csv(si no pusiese nada lo que separa los elementos seria la coma pero como en este caso son ; por dnd quiero separar, los separo agregando: , delimiter=';' ).
        # for linea in reader:
        #     pelicula, año, actores = linea #esto lo hacemos xq le queremos asignar a cada nombre una variable sino podemos usar los indices de la lista
        reader = csv.DictReader(archivo, delimiter=';') #el dictreader en vex de listas me va a dar diccionarios donde cadad una de las claves van a ser los valores del encabezado y los valores, los valores de cada una de las lineas. entonces cada linea va a ser un diccionario. el dictreader asume que la primer linea son los headers de cada columna.
        for linea in reader:
            if not linea["Año"] or not linea["Actores"]:#xq me interesan el año y los actores, la pelicula me da lo mismo si esta o no está.
                continue
            if not linea["Año"].isnumeric():
                continue
            año = int(linea["Año"])
            for actor in linea["Actores"].split(","):
                if año in res.get(actor, []): # if actor in res and año in res[actor]
                    continue
                res[actor] = res.get(actor, []) + [año]

    return res

#ademas de los reader, tenemos los writer y dictwriter que hace los mismo a la inversa. te escribe el header, etc,etc
