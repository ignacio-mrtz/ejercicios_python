#Escribir una función que recibe una expresión matemática (en forma de cadena)
#y devuelve True si los paréntesis ('()'), corchetes ('[]') y llaves ('{}') están correctamente
#balanceados, False en caso contrario. Ejemplos:
#validar('(x+y)/2') -> True
#validar('[8*4(x+y)]+{2/5}') -> True
#validar('(x+y]/2') -> False
#validar('1+)2(+3') -> False
#validar('(((1)+2)+3)') -> True
#validar('(((1)+2+3)') -> False
#Nota: Se encuentran disponibles los TDA Pila y Cola con sus métodos ya definidos en los archivos pila.py y cola.py #respectivamente.

#ej correcto(chequeado en rpl)


from pila import Pila

def validar(ecuacion):
    pila=Pila()
    for c in ecuacion:
        if c=="[" or c=="{" or c=="(":
            pila.apilar(c)
        elif c=="]":
            if pila.esta_vacia()==False and pila.ver_tope()=="[":
                pila.desapilar()
            else:
                pila.apilar(c)
        elif c=="}":
            if pila.esta_vacia()==False and pila.ver_tope()=="{":
                pila.desapilar()
            else:
                pila.apilar(c)
        elif c==")":
            if pila.esta_vacia()==False and pila.ver_tope()=="(":
                pila.desapilar()
            else:
                pila.apilar(c)
    return pila.esta_vacia()
