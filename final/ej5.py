# Ejercicio 5
# a. Implementar una clase Libro que representa la información de un libro en una biblioteca.
# Un libro tiene un título (str), un autor (str) y un código único identificatorio llamado ISBN
# (int).
# b. Escribir la función buscar(isbn, libros) que recibe una lista de instancias de Libro ordenada
# por ISBN, y un código a buscar, y devuelve el libro correspondiente (o None en caso
# de no encontrarlo) en tiempo mejor que lineal.

# HACER: implementar la clase Libro

class Libro:
    def __init__(self,titulo,autor,codigo_ISBN):
        self.titulo=titulo
        self.autor=autor
        self.codigo=codigo_ISBN

def buscar(isbn, libros):
    # HACER: implementar
    izq=0
    der=len(libros)-1
    while izq<=der:
        medio=(izq+der)//2
        if libros[medio].codigo==isbn:
            return libros[medio]
        if libros[medio].codigo>isbn:
            der=medio-1
        else:
            izq=medio+1



def pruebas():
    libros = [
        Libro(
            'Cien años de soledad',
            'Gabriel García Márquez',
            9780060929794,
        ),
        Libro(
            'La casa de los espíritus',
            'Isabel Allende',
            9780525433477,
        ),
        Libro(
            'Veinte poemas de amor y una canción desesperada',
            'Pablo Neruda',
            9788497933056,
        ),
    ]

    libro = buscar(9780525433477, libros)
    assert libro.titulo == 'La casa de los espíritus'

    # OPCIONAL: escribir pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()

