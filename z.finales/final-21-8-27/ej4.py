class Deque:
    def __init__(self, k):
        # HACER: implementar
        #
        # Ayuda: crear un arreglo de tamaño k, y dos índices para marcar las
        # posiciones de "atrás" y "adelante". ¡Pensar bien las invariantes!

    def esta_vacia(self):
        # HACER: implementar

    def agregar_adelante(self, dato):
        # HACER: implementar

    def quitar_adelante(self):
        # HACER: implementar

    def ver_adelante(self):
        # HACER: implementar

    def agregar_atras(self, dato):
        # HACER: implementar

    def quitar_atras(self):
        # HACER: implementar

    def ver_atras(self):
        # HACER: implementar


def pruebas():
    d = Deque(10)

    assert d.esta_vacia()

    d.agregar_atras(1)

    # [ - - - - 1 - - - - - ]
    #           |
    #           adelante
    #       atras

    assert d.ver_adelante() == 1
    assert d.ver_atras() == 1

    d.agregar_adelante(2)

    # [ - - - - 1 2 - - - - ]
    #           | |
    #       atras adelante

    assert d.ver_adelante() == 2
    assert d.ver_atras() == 1

    d.agregar_atras(3)
    d.agregar_adelante(4)
    d.agregar_adelante(5)

    # [ - - - 3 1 2 4 5 - - ]
    #         |       |
    #     atras       adelante

    assert d.ver_adelante() == 5
    assert d.ver_atras() == 3

    dato = d.quitar_adelante()
    assert dato == 5

    # [ - - - 3 1 2 4 - - - ]
    #         |     |
    #     atras     adelante

    assert d.ver_adelante() == 4
    assert d.ver_atras() == 3

    dato = d.quitar_atras()
    assert dato == 3

    # [ - - - - 1 2 4 - - - ]
    #           |   |
    #       atras   adelante

    assert d.ver_adelante() == 4
    assert d.ver_atras() == 1

    d.quitar_atras()
    d.quitar_atras()
    d.quitar_atras()

    assert d.esta_vacia()

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()

