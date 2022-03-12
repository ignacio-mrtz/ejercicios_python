def a_octal(s):
    # HACER: implementar


def a_cadena(n):
    # HACER: implementar


def pruebas():
    assert a_octal('r-x') == 5
    assert a_cadena(5) == 'r-x'

    # OPCIONAL: escribir pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()



