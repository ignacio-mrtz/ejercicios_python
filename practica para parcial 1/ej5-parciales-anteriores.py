# Del segundo recuperatorio del primer parcialito, primer cuatrimestre de 2014
# 3) Escribir una funcion que reciba dos secuencias A y B como parametro, y devuelva un
# valor booleano indicando si todos los elementos de A estan en B.

def main(secuencia_A, secuencia_B):
    for x in secuencia_A:
        if x not in secuencia_B:
            return False
    return True

print(main("hola","aloha"))
