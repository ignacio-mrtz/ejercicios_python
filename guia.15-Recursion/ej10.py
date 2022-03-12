# Ejercicio 15.10. Escribir una funcion recursiva que dada una cadena determine si en la misma hay más letras A o letras E.

def _main(cadena,cont_A, cont_E):
    if len(cadena)==0:
        return cont_A>cont_E
    elif cadena[0]=="A":
        return _main(cadena[1:],cont_A+1,cont_E)
    elif cadena[0]=="E":
        return _main(cadena[1:],cont_A,cont_E+1)
    else:
        return _main(cadena[1:],cont_A,cont_E)
    
def main(cadena):
    cont_A=0
    cont_E=0
    return _main(cadena,cont_A, cont_E)

print(main(""))