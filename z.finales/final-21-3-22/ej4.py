import math

def buscar_cero(f, n_min, n_max):
    #
    # HACER: implementar la función
    #

def pruebas():

    def f(n):
        return math.factorial(n) - 40320

    assert buscar_cero(f, 0, 20) == 8   # porque f(8) == 0

    # OPCIONAL: agregar más casos de prueba.

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
