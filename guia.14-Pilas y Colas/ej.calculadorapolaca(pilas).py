#ej pag 220 apuntes

from pila import Pila

def calculadora_polaca(elementos):
    """Dada una lista de elementos que representan las componentes de
    una expresión en notacion polaca inversa, evalúa dicha expresión.
    Si la expresion está mal formada, levanta ValueError."""
    p = Pila()
    for elemento in elementos:
        print("DEBUG:", elemento)
        # Intenta convertirlo a número
        try:
            numero = float(elemento)
            p.apilar(numero)
            print("DEBUG: apila ", numero)
        # Si no se puede convertir a número, debería ser un operando
        except ValueError:
            # Si no es un operando válido, levanta ValueError
            if elemento not in ('+', '-', '*', '/'):
                raise ValueError("Operando inválido")
            # Si es un operando válido, intenta desapilar y operar
            try:
                a1 = p.desapilar()
                print("DEBUG: desapila ", a1)
                a2 = p.desapilar()
                print("DEBUG: desapila ", a2)
            # Si hubo problemas al desapilar
            except IndexError:
                raise ValueError("Faltan operandos")

            if elemento == "+":
                resultado = a2 + a1
            elif elemento == "-":
                resultado = a2 - a1
            elif elemento == "*":
                resultado = a2 * a1
            elif elemento == "/":
                resultado = a2 / a1
            print("DEBUG: apila ", resultado)
            p.apilar(resultado)

    # Al final, el resultado debe ser lo único en la Pila
    resultado = p.desapilar()
    if not p.esta_vacia():
        raise ValueError("Sobran operandos")
    return resultado

def main():
    expresion = input("Ingrese la expresion a evaluar: ")
    elementos = expresion.split()
    print(calculadora_polaca(elementos))

main()

#ej
#PS C:\Users\juan ignacio\Desktop\resolucion guia de ejercicios Algo1-FIUBA\guia.14-Pilas y Colas> python3 -i '.\ej.calculadorapolaca(pilas).py'
#Ingrese la expresion a evaluar: 4 5 + 6 *
#DEBUG: 4
#DEBUG: apila  4.0
#DEBUG: 5
#DEBUG: apila  5.0
#DEBUG: +
#DEBUG: desapila  5.0
#DEBUG: desapila  4.0
#DEBUG: apila  9.0
#DEBUG: 6
#DEBUG: apila  6.0
#DEBUG: *
#DEBUG: desapila  6.0
#DEBUG: desapila  9.0
#DEBUG: apila  54.0
#54.0
#>>>