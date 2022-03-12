# HACER: implementar la clase Persona

def buscar_en_padron(dni, personas):
    # HACER: implementar la función

def pruebas():
    personas = [
        Persona(11111, "persona 1", "direccion 1"),
        Persona(22222, "persona 2", "direccion 2"),
        Persona(33333, "persona 3", "direccion 3"),
        Persona(44444, "persona 4", "direccion 4"),
    ]

    p = buscar_en_padron(33333, personas)
    assert(p is personas[2])

    # OPCIONAL: Pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
