=======================
Examen final 2022-02-14
=======================
:lang: es-AR

--------------------------------------------------------
95.14/75.40 - Algoritmos y Programación I - Curso Essaya
--------------------------------------------------------

Objetivo
========

Se dispone de los archivos ``ej1.py``, ``ej2.py``, ``ej3.py``, ``ej4.py`` y
``ej5.py`` correspondientes a los 5 ejercicios del examen.

Cada uno tiene un lugar para escribir la implementación del ejercicio, y una
función de pruebas para verificar que la solución es correcta.

El examen se aprueba con al menos 3 ejercicios correctamente resueltos. Un
ejercicio se considera correctamente resuelto si:

* El programa ``ej<n>`` no tiene errores de sintaxis y puede ser ejecutado
* La implementación cumple con lo pedido en el enunciado

En algunos ejercicios se incluye un ejemplo de uno o dos casos de prueba y
queda a cargo del alumno agregar más casos de prueba, para los que se provee
sugerencias. En otros ejercicios se provee únicamente sugerencias.  La
implementación de las pruebas adicionales es **opcional**, pero se recomienda
hacerlo ya que permite incrementar la certeza de que la resolución del
ejercicio es correcta.

Pruebas
=======

Al ejecutar cada uno de los ejercicios (``python3 ej<n>.py``), se ejecutan
todas las pruebas presentes en la función ``pruebas``.

Si alguna de las verificaciones falla, se imprime un mensaje de error y el
programa termina su ejecución. Por ejemplo::

    $ python3 ej1.py
    Traceback (most recent call last):
    File "ej1.py", line 148, in pruebas
        assert p != None
    AssertionError

Cuando todas las pruebas pasan correctamente, se imprime ``OK``::

    $ python3 ej1.py
    ej1.py: OK

.. raw:: latex

    \newpage

Ejercicios
==========

.. temas:
    cadenas
    - listas
    - busqueda
    diccionarios
    - archivos
    - objetos
    - lista-enlazada
    pilas
    colas
    - recursion
    - ordenamiento

.. Temas: listas
Ejercicio 1
   Escribir la función ``patron_tablero(n, k)`` (con :math:`k < n`), que devuelve
   una matriz de :math:`n \times n` ceros y unos, formando un patrón de tablero de
   ajedrez donde cada casillero es de tamaño :math:`k \times k`.

   Ejemplo: ``patron_tablero(10, 3)``::

        0001110001
        0001110001
        0001110001
        1110001110
        1110001110
        1110001110
        0001110001
        0001110001
        0001110001
        1110001110

.. Temas: busqueda ordenamiento objetos
Ejercicio 2
   Sea la clase ``Alumno`` que representa a un alumno de FIUBA, con un ``nombre`` y un ``padrón``.

   Sea la clase ``Curso`` que contiene un ``código`` y una lista de los alumnos inscriptos
   al curso, ordenada por padrón.

   Implementar los métodos de la clase ``Curso``:

   * ``__init__``, que inicializa un curso vacío dado un código.

   * ``inscribir(alumno)``, que agrega el alumno al curso. En caso de que ya
     haya un alumno inscripto con el mismo padrón, debe lanzar una excepción.

   * ``listar(k, n)``, que devuelve la ``n``-ésima página (contando desde 0) de
     alumnos ordenados por padrón, donde cada página tiene ``k`` alumnos, en
     tiempo **lineal** (``O(k)``). En caso de que no haya alumnos en la
     ``n``-ésima página, devolver una lista vacía.

   * ``interseccion(otro_curso)`` que devuelve la lista ordenada de padrones de
     los alumnos que están inscriptos a ambos cursos, en tiempo **lineal**
     (``O(N+M)`` siendo ``N`` y ``M`` la cantidad de alumnos inscriptos en
     ambos cursos).

   Ayuda: pensar bien la implementación de ``inscribir`` para cumplir los
   requisitos de ``listar`` e ``interseccion``.

.. Temas: archivos objetos
Ejercicio 3
   Sean las clases ``Alumno`` y ``Curso`` del ejercicio 2 (modificadas).
   Implementar las funciones:

   * ``guardar_curso(curso, ruta)`` que guarda los datos del curso en un
     archivo.
   * ``cargar_curso(ruta)`` que carga los datos del archivo y devuelve una
     instancia de ``Curso``. Asumir que el formato del archivo es correcto.

   El nombre y formato del archivo queda a libre elección. Se puede implementar
   "a mano" o utilizar cualquiera de los módulos estándar ``csv``, ``json`` o
   ``struct``.

.. Temas: lista-enlazada recursion
Ejercicio 4
   Implementar en forma **recursiva** el método de ``ListaEnlazada``
   ``intercambiar_pares()`` que intercambia los datos de cada par de nodos
   adyacentes.

   Ejemplo::

        lista = a -> b -> c -> d -> e -> f -> g
        lista.intercambiar_pares()
                b -> a -> d -> c -> f -> e -> g

.. Temas: cadenas
Ejercicio 5
    Los archivos en un sistema operativo pueden o no tener permisos de lectura (`r`),
    escritura (`w`) y/o ejecución (`x`). Los permisos
    de un archivo se pueden representar con una cadena de 3 caracteres o con un
    número octal (entero entre 0 y 7):

    *   En forma de cadena, el primer caracter puede ser `r` o `-` según si el
        archivo tiene o no permisos de lectura. El segundo caracter es `w` o
        `-` según si tiene o no permisos de escritura. El tercer
        caracter es `x` o `-` según si tiene o no permisos de ejecución. Por
        ejemplo, la cadena `rwx` representa un archivo con todos los permisos.
        La cadena `r-x` representa permisos de lectura y ejecución.

    *   En forma de número octal, el permiso de lectura vale 4, el de
        escritura vale 2 y el de ejecución vale 1, y se suman los tres valores.
        Un archivo con todos los permisos (`rwx`) tiene valor 7 (4+2+1). Un
        archivo con permisos `r-x` tiene valor 5 (4+1).

    Implementar las funciones `a_octal(cadena)` y `a_cadena(octal)` que
    permiten convertir los permisos entre ambas representaciones. Ejemplos:
    `a_octal('r-x') ➡ 5`, `a_cadena(5) ➡ 'r-x'`.

    No es necesario validar los parámetros recibidos.
