def separar_comunas(todos):
    # HACER: implementar la función


def pruebas():
    separar_comunas("todos.csv")

    # todos.csv contiene:
    # ---------
    # 12,345678
    # 15,456789
    # 12,123456
    # 12,234567
    # 15,123123

    # Se deberían haber creado dos archivos:
    #
    # 12.csv
    # ------
    # 345678
    # 123456
    # 234567
    #
    #
    # 15.csv
    # ------
    # 456789
    # 123123

    from os import path
    print(f"{path.basename(__file__)}: OK (verificar que se hayan creado los archivos)")

pruebas()
