from pathlib import Path

# LAS RUTAS SE ME GUARDAN DE ESTA MANERA ['a\\x.txt'] ----> \\

def buscar(ruta, nombre):
    # HACER: implementar
    lista = []
    r = Path(ruta)
    if r.is_dir():
        for elemento in r.iterdir():
            if elemento.is_dir():
                lista.extend(buscar(elemento, nombre))
            else:
                if elemento.name == nombre:
                    lista.append((str(elemento)))
    return lista


def pruebas():
    r = buscar('a', 'x.txt')

    assert len(r) == 2
    assert 'a\\b\\c\\x.txt' in r
    assert 'a\\x.txt' in r

    # OPCIONAL: escribir pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
