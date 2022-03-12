# Ejercicio 14.6. Escribir una función que recibe una expresión matemática (en forma de cadena)
# y devuelve True si los paréntesis ('()'), corchetes ('[]') y llaves ('{}') están correctamente
# balanceados, False en caso contrario. Ejemplos:
# validar('(x+y)/2') -> True
# validar('[8*4(x+y)]+{2/5}') -> True
# validar('(x+y]/2') -> False
# validar('1+)2(+3') -> False

from pila import Pila

CORRESP = { "(" : ")",
            "[" : "]",
            "{" : "}"
} 

def validar(expresion):
    llaves = Pila()
    for carac in expresion:
        if carac in CORRESP.keys():
            llaves.apilar(carac)
        elif carac in CORRESP.values():
            if llaves.esta_vacia() or carac != CORRESP[llaves.desapilar()]:
                return False
    return llaves.esta_vacia()


# Ejemplos:
assert validar('(') == False
assert validar('(x+y)/2') == True
assert validar('[8*4(x+y)]+{2/5}') == True
assert validar('(x+y]/2') == False
assert validar('([x + y)]') == False
assert validar('1+)2(+3') == False

#otra forma

def main(cadena):
    pila=Pila()
    for c in cadena:
        if c in ("(","[","{"):
            pila.apilar(c)
        elif c in ( ")","]","}"):
            if pila.esta_vacia():
                return False
            if c==")" and pila.ver_tope()=="(" or c=="]" and pila.ver_tope()=="[" or c=="}" and pila.ver_tope()=="{":
                pila.desapilar() 
    return pila.esta_vacia()

assert main('(') == False
assert main('(x+y)/2') == True
assert main('[8*4(x+y)]+{2/5}') == True
assert main('(x+y]/2') == False
assert main('([x + y)]') == False
assert main('1+)2(+3') == False