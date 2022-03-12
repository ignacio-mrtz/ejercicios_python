# HACER: implementar las funciones

def matriz_guardar(ruta, matriz):
    '???'

def matriz_cargar(ruta):
    '???'

def pruebas():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    # HACER:
    # - llamar a matriz_guardar
    # - llamar a matriz_cargar
    # - verificar que la matriz cargada es idéntica a la original

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
