"""Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido tiene el formato materia, fecha_final y devuelva un diccionario con las fechas de final para cada materia"""

def cargar_datos(ruta_archivo):
    diccionario={}
    with open(ruta_archivo) as f:
        for linea in f:
            linea=linea.rstrip("\n")
            lista=linea.split(",")
            if lista[0] in diccionario:
                diccionario[lista[0]].append(lista[1])
            else:
                diccionario[lista[0]]=[lista[1]]
    return diccionario
        

#print(cargar_datos("materias.csv"))

#como se hizo en clase:

def cargar_datos(ruta_archivo):
    diccionario = {}
    with open(ruta_archivo) as archivo:
        for linea in archivo:
            linea = linea.rstrip()
            materia, fecha = linea.split(',')
            if materia not in diccionario:
                diccionario[materia] = [fecha]
            else:
                diccionario[materia].append(fecha)

            # diccionario[materia] = diccionario.get(materia, [])
            # diccionario[materia].append(fecha)

            # diccionario[materia] = diccionario.get(materia, []) + [fecha]
        
    return diccionario

''' Escribir una función guardar_datos que reciba un diccionario y un nombre de 
    archivo, y guarde el contenido del diccionario en el archivo, con el formato 
    clave, valor.
    '''
def guardar_datos(diccionario,nuevo_archivo):
    with open(nuevo_archivo,"w") as f:
        for materia,fecha in diccionario.items():
            for i in range(0,len(fecha)):
                f.write(f"{materia},{fecha[i]}\n")


#guardar_datos(cargar_datos("materias.csv"),"archivo_nuevo_examenes.csv")

#hecho en clase:

def guardar_datos2(diccionario, ruta_archivo):
    with open(ruta_archivo, 'w') as salida:
        for materia, fechas in diccionario.items():
            for fecha in fechas:
                salida.write(f'{materia},{fecha}\n')

#guardar_datos2(cargar_datos("materias.csv"),"archivo_nuevo_examenes2.csv")