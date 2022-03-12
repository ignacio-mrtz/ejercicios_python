class RegistroDeDesplazamiento:
    # HACER: implementar los metodos

def pruebas():
    r = RegistroDeDesplazamiento(4)

    assert str(r) == '0000'
    assert r.rshift(0) == 0
    assert str(r) == '0000'
    assert r.rshift(1) == 0
    assert str(r) == '1000'
    assert r.rshift(0) == 0
    assert str(r) == '0100'
    assert r.rshift(0) == 0
    assert str(r) == '0010'
    assert r.rshift(0) == 0
    assert str(r) == '0001'
    assert r.rshift(0) == 1
    assert str(r) == '0000'
    assert r.rshift(0) == 0
    assert str(r) == '0000'

    # OPCIONAL: pruebas adicionales (ej: probar lshift)


    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
