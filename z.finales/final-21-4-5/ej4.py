
# HACER: implementar las funciones

class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def __eq__(self, otro):
        '???'

def ordenar_libros(libros):
    '???'

def buscar_libro(libros, titulo):
    '???'

def pruebas():

    libros = [
        Libro("The Sittaford Mystery", "Agatha Christie", 1931),
        Libro("The Seven Dials Mystery", "Agatha Christie", 1929),
        Libro("The Murder at the Vicarage", "Agatha Christie", 1930),
        Libro("The Mystery of the Blue Train", "Agatha Christie", 1928),
        Libro("The Floating Admiral", "Agatha Christie", 1931),
        Libro("Giant's Bread", "Agatha Christie", 1930),
    ]

    ordenar_libros(libros)

    assert libros == [
        Libro("Giant's Bread", "Agatha Christie", 1930),
        Libro("The Floating Admiral", "Agatha Christie", 1931),
        Libro("The Murder at the Vicarage", "Agatha Christie", 1930),
        Libro("The Mystery of the Blue Train", "Agatha Christie", 1928),
        Libro("The Seven Dials Mystery", "Agatha Christie", 1929),
        Libro("The Sittaford Mystery", "Agatha Christie", 1931),
    ]

    libro = buscar_libro(libros, "The Floating Admiral")
    assert libro is libros[1]

    # OPCIONAL: pruebas adicionales. Ejemplo: buscar un libro que no exista

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()
