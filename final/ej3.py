# Ejercicio 3 En cierta materia de la FIUBA, los exámenes se gradúan con un puntaje entre 0 y 100.
# Como todos sabemos, según el reglamento la nota de la materia debe ser entre 0 y 10, pero
# en esta materia la correlación entre ambas numeraciones no es lineal.
# Se dispone de un archivo CSV con la estrategia de conversión entre ambas numeraciones, con
# formato nota,puntaje_min,puntaje_max. Por ejemplo:
# 2,0,39
# 3,40,49
# 4,50,59
# 5,60,69
# 6,70,79
# 7,80,89
# 8,90,94
# 9,95,99
# 10,100,100
# Por otro lado se tiene un archivo CSV con formato: padron,nombre,puntaje con el puntaje de
# cada alumno:
# 123457,Hermione Jean Granger,98
# 123458,Ronald Bilius Weasley,66
# 123456,Harry James Potter,75
# Implementar la función calcular_notas(ruta_conversion, ruta_puntajes, ruta_notas) que
# recibe las rutas de ambos archivos CSV de entrada y la ruta de un archivo de salida, que debe
# tener el formato padron,nombre,nota, con la nota calculada mediante la tabla de conversión,
# ordenado en forma decreciente según la nota. En base a los ejemplos de arriba, el archivo
# producido debe quedar:
# 123457,Hermione Jean Granger,9
# 123456,Harry James Potter,6
# 123458,Ronald Bilius Weasley,5
# Asumir que el formato de los archivos de entrada es correcto, y que la tabla de conversión está
# ordenada y completa.

def calcular_notas(ruta_conversion, ruta_puntajes, ruta_notas):
    # HACER: implementar
    lista_conversion=[]
    with open(ruta_conversion) as f:
        for linea in f:
            nota,desde,hasta=(linea.rstrip("\n")).split(",")
            nota=int(nota)
            desde=int(desde)
            hasta=int(hasta)
            lista_conversion.append([nota,desde,hasta])
    lista_con_notas_correctas=[]
    with open(ruta_puntajes) as f:
        for linea in f:
            padron,nombre,puntaje=linea.rstrip("\n").split(",")
            puntaje=int(puntaje)
            for e in lista_conversion:
                if e[1]<puntaje<e[2]:
                    puntaje=e[0]
                    break
            lista_con_notas_correctas.append([padron,nombre,puntaje])
        lista_con_notas_correctas.sort(reverse= True, key=lambda x: x[2])
    with open(ruta_notas,"w") as f:
        for x in lista_con_notas_correctas:
            f.write(f"{x[0]},{x[1]},{x[2]}\n")





def pruebas():
    calcular_notas('conversion.csv', 'puntajes.csv', 'notas.csv')

    from os import path
    assert path.exists('notas.csv')
    print(f"{path.basename(__file__)}: OK (verificar el contenido de notas.csv)")

    # OPCIONAL: escribir pruebas adicionales

pruebas()
