# 1. Escribir una funcion que reciba un texto y devuelva la palabra que tiene la mayor
# cantidad de letras distintas. El texto puede contener cualquier tipo de símbolo
# pero no tiene letras acentuadas.

# Por ejemplo: `"Hola, como le va al señor Papadopulus Mintkeolu, en el dia de hoy?"` -> `"Mintkeolu"`

# _Hint_: el módulo string tiene la variable ascii_lowercase que devuelve una cadena con todas las letras del alfabeto en minúscula.

import string

def palabra_mas_variada(texto):
    palabra_mas_variada = ""
    for palabra in limpiar_texto(texto).split():
        cant = len(set(palabra.lower()))
        if cant > len(set(palabra_mas_variada.lower())):
            palabra_mas_variada = palabra
    return palabra_mas_variada

def palabra_mas_variada(texto):
    return max(limpiar_texto(texto).split(), key=lambda palabra: len(set(palabra.lower())))

def limpiar_texto(texto):
    res = ""
    for c in texto:
        if c.lower() in string.ascii_lowercase or c == " ":
            res += c
    return res

# 2. Se tiene una lista de los alumnos de una materia y se desea dividirlos en 3
# grupos según resto del cociente entre el padrón del alumno y 3.

# * Si el padrón es `12345`, se deberá hacer `12345 % 3 = 2`
# * Si el padrón es `7774` se deberá hacer `7774 % 3 = 1`
# * Si el padrón es `36` se deberá hacer `36 % 3 = 0`

# La lista de los alumnos se encuentra en un archivo que tiene un número de
# padrón por línea. Se pide escribir una función que reciba por parámetro el
# nombre del archivo de alumnos y devuelva 3 archivos cuyos nombres tendrán el
# formato: `<nombre archivo alumnos>_Enunciado<número de grupo>.txt` con la lista
# de padrones correspondientes a cada grupo uno por línea.

# Nota: al finalizar la ejecución de la función (haya ocurrido un error o no),
# todos los archivos abiertos deben quedar cerrados.

def agrupar_padrones(ruta):
    salida = "{}_Enunciado".format(ruta) + "{}.txt"

    with open(ruta) as padrones, open(salida.format(1), 'w') as salida1, open(salida.format(2), 'w') as salida2, open(salida.format(3), 'w') as salida3:
        salidas = [salida1, salida2, salida3]
        for padron in padrones:
            salidas[int(padron) % 3].write(padron)

# 3. Se pide implementar una clase `CalendarioMes` con los siguientes métodos:

# - `__init__()`: toma como parámetro un entero que representa el número de
#   días del mes (entre 28 y 31). Debe levantar una excepción si no es un día válido.
# - `agregar_evento()`: toma como parámetro un día (número entero) y el nombre
#   de un evento (cadena) y lo almacena en el calendario. Debe levantar una excepción si no es un día válido.
# - `eliminar_evento()`: toma como parámetro un día y el nombre de un evento y
#   lo elimina del calendario. Debe levantar una excepción si no existe un evento con ese nombre.
# - `obtener_eventos_dia()`: toma como parámetro un día y devuelve una lista
#   con los eventos programados para ese día, o la lista vacía si no hay
#   eventos en ese día. Debe levantar una excepción si no es un día válido.


class DiaNoValidoError(Exception):
    pass

class CalendarioMes:
    def __init__(self, dia):
        if validar_en_rango(dia, 28, 31):
            self.dias_del_mes = dia
        else:
            raise Exception(f"El dia {dia} debe estar entre 28 y 31")
        self.eventos = {}

    def agregar_evento(self, dia, evento):
        if validar_en_rango(dia, 1, self.dias_del_mes):
            self.eventos[dia] = self.eventos.get(dia, []) + [evento]
        else:
            raise Exception(f"El dia {dia} debe estar entre 1 y {self.dias_del_mes}")
    
    def eliminar_evento(self, dia, evento):
        if evento not in self.eventos.get(dia, []):
            raise Exception(f"No existe el evento {evento} para el dia {dia}")
        self.eventos[dia].remove(evento)
    
    def obtener_eventos_dia(self, dia):
        if validar_en_rango(dia, 1, self.dias_del_mes):
            return self.eventos.get(dia, [])
        raise Exception(f"El dia {dia} debe estar entre 1 y {self.dias_del_mes}")

def validar_en_rango(n, min, max):
    return min <= n <= max