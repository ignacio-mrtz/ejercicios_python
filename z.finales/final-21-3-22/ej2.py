#
# HACER: implementar la clase y las funciones
#
class Producto:

def guardar(productos, ruta):

def cargar(ruta):

def verificar_ids(productos):

def pruebas():

    productos = [
        # HACER: llenar la lista con al menos 3 productos diferentes
    ]

    # HACER: llamar a la función guardar()
    guardar()

    # HACER: llamar a la función cargar()
    productos_cargado = cargar()

    # HACER: verificar que productos_cargado y productos son equivalentes

    assert verificar_ids(productos)

    # OPCIONAL: probar verificar_ids() con una lista que contiene repeticiones

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
