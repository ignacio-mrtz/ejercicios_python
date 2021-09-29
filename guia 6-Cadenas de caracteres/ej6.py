# Ejercicio 6.6. Escribir funciones que dada una cadena de caracteres:
# a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o
# 'logaritmos' debe devolver 'lgrtms'.
# b) Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe
# devolver 'i ooae'.
# c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe
# devolver 'vistaerou'.
# d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un palíndromo
# (se lee igual de izquierda a derecha que de derecha a izquierda).

def main_a(string):
    sum=""
    for c in string:
        if not(c in "aeiou"):
            sum+=c
    return sum

#print(main_a("logaritmos"))

def main_b(string):
    sum=""
    for c in string:
        if c in "aeiou":
            sum+=c
        elif c==" ":
            sum+=" "
    return sum

#print(main_b("sin consonantes"))

def main_c(string):
    sum=""
    for c in string:
        if c=="a":
            sum+="e"
        elif c=="e":
            sum+="i"
        elif c=="i":
            sum+="o"
        elif c=="o":
            sum+="u"
        elif c=="u":
            sum+="a"
        else:
            sum+=c
    return sum
 
#print(main_c("vestuario"))

def main_c2(string):
    remplazo = string.replace("a","e").replace("e","i").replace("i","o").replace("o","u").replace("u","a")
    return remplazo

#print(main_c("vestuario"))

def main_d(string):
    sin_espacios=string.replace(" ","")
    if sin_espacios==sin_espacios[::-1]:
        return True
    else:
        return False

#print(main_d("anita lava la tina"))

