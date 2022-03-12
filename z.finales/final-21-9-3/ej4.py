def temperaturas_maximas(ruta):
    # HACER: implementar la función


def pruebas():
    # El archivo temperaturas.csv contiene:
    #
    # 2021-08-30,Buenos Aires,22
    # 021-08-29,Buenos Aires,24
    # 2021-08-27,22
    # 2021-08-31,Buenos Aires,23
    # 2021-08-30,La Plata,20
    # 2021-08-31,La Plata,19
    # 2021-08-29,La Plata,21,
    #
    # Notar que algunas líneas no cumplen con el formato y deben ser ignoradas.

    assert temperaturas_maximas("temperaturas.csv") == {
        "Buenos Aires": ("2021-08-31", 23),
        "La Plata": ("2021-08-30", 20),
    }

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()

