#Sea la clase Impresion que tiene un método obtener_impresora() (que devuelve el nombre
#de una impresora). Escribir una función que recibe una Cola de impresiones, y distribuya
#las mismas en un diccionario de colas, en el que las claves sean los nombres de las impresoras,
#y cada impresora tenga su propia Cola con las impresiones recibidas. La cola original debe
#quedar vacía al finalizar la ejecución.

from cola import Cola

def distribuir(cola):
    # HACER: implementar la función
    diccionario={}
    while cola.esta_vacia()==False:
        impresion=cola.desencolar()
        if impresion.obtener_impresora() in diccionario:
            diccionario[impresion.obtener_impresora()].encolar(impresion)
        else:
            diccionario[impresion.obtener_impresora()]=Cola()
            diccionario[impresion.obtener_impresora()].encolar(impresion)
    return diccionario


class Impresion:
    def __init__(self, doc, impresora):
        self.doc = doc
        self.impresora = impresora

    def obtener_impresora(self):
        return self.impresora

    def obtener_doc(self):
        return self.doc

    def __repr__(self):
        return f'Impresion({self.doc}, {self.impresora})'

def pruebas():
    cola = Cola()
    cola.encolar(Impresion("1.doc", "impresora A"))
    cola.encolar(Impresion("2.doc", "impresora B"))
    cola.encolar(Impresion("3.doc", "impresora A"))

    r = distribuir(cola)

    assert cola.esta_vacia()

    assert len(r) == 2

    assert r["impresora A"].desencolar().obtener_doc() == "1.doc"
    assert r["impresora A"].desencolar().obtener_doc() == "3.doc"
    assert r["impresora A"].esta_vacia()

    assert r["impresora B"].desencolar().obtener_doc() == "2.doc"
    assert r["impresora A"].esta_vacia()

    # OPCIONAL: Pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()

