# Se tiene un archivo CSV con el formato año,mes,dia,divisa,precio con el precio promedio
# de diferentes divisas registrado en cada día. El archivo no está ordenado bajo ningún
# criterio en particular.
# Escribir la función separar que cree un archivo <divisa>.csv por cada divisa con el formato
# año,precio, con el precio máximo de cada año de la divisa, ordenado por año.

def separar(ruta):
    # HACER: implementar la función
    diccionario_divisas={}
    with open(ruta) as f:
        for linea in f:
            linea=linea.rstrip("\n")
            año,mes,dia,divisa,precio=linea.split(",")
            precio=int(precio)
            if divisa not in diccionario_divisas:
                diccionario_divisas[divisa]={}
                diccionario_divisas[divisa][año]=precio
            elif año not in diccionario_divisas[divisa]:
                diccionario_divisas[divisa][año]=precio
            elif diccionario_divisas[divisa][año]<precio:
                diccionario_divisas[divisa][año]=precio
    print(diccionario_divisas)

    for clave,valor in diccionario_divisas.items():
        with open(f"{clave}.csv","w") as f:
            for clave,valor in valor.items():
                f.write(f"{clave},{valor}\n")
                

def pruebas():
    separar('divisas.csv')

    # El archivo divisas.csv contiene:
    #
    # 2020,09,07,USD,70
    # 2020,09,08,EUR,90
    # 2020,09,15,USD,80
    # 2021,08,19,USD,90
    # 2021,09,18,USD,100
    # 2021,09,09,EUR,110

    # Se deben haber creado los archivos:
    #
    # USD.csv:
    # 2020,80
    # 2021,100
    #
    # EUR.csv:
    # 2020,90
    # 2021,110

    from os import path
    print(f"{path.basename(__file__)}: OK (revisar USD.csv y EUR.csv)")

pruebas()

