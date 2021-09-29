# Ejercicio 6.7. Escribir funciones que dadas dos cadenas de caracteres:
# a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena'
# es una subcadena de 'subcadena'.
# b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome'
# debe devolver 'gnome'.

def main_a(string1, string2):
    return string2 in string1

#print(main_a("subcadena","cadena"))

def main_b(string1, string2):
    if string2>string1:
        return string1
    else:
        return string2

#print(main_b("kde","gnome"))







