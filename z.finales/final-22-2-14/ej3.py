Sean las clases Alumno y Curso del ejercicio 2 (modificadas). Implementar las funciones:
• guardar_curso(curso, ruta) que guarda los datos del curso en un archivo.
• cargar_curso(ruta) que carga los datos del archivo y devuelve una instancia de Curso.
Asumir que el formato del archivo es correcto.
El nombre y formato del archivo queda a libre elección. Se puede implementar ”a mano” o
utilizar cualquiera de los módulos estándar csv, json o struct.

class Alumno:
    def __init__(self, nombre, padron):
        self.nombre = nombre
        self.padron = padron

class Curso:
    def __init__(self, codigo, alumnos):
        self.codigo = codigo
        self.alumnos = alumnos

def guardar_curso(c, ruta):
    # HACER: implementar
    

def cargar_curso(ruta):
    # HACER: implementar

def pruebas():
    c = Curso('95.14', [
        Alumno('Juani', 123456),
        Alumno('Agus', 123457),
        Alumno('Lucho', 123458),
        Alumno('Fede', 123459),
        Alumno('Javi', 123460),
    ])

    # HACER: elegir un nombre apropiado para el archivo
    ruta = ''
    guardar_curso(c, ruta)

    c2 = cargar_curso(ruta)

    assert c.codigo == c2.codigo
    assert len(c.alumnos) == len(c2.alumnos)
    for i in range(len(c.alumnos)):
        assert c.alumnos[i].nombre == c2.alumnos[i].nombre
        assert c.alumnos[i].padron == c2.alumnos[i].padron

    # OPCIONAL: escribir pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")


pruebas()
