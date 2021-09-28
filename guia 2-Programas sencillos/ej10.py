# Ejercicio 2.10. Modificar el programa anterior para que pueda generar fichas de un juego que
# puede tener números de 0 a 𝑛.

def juego(n):
    for i in range(1, n):
        for j in range(i, n):
            print("{}:{}".format(i, j))

#juego(10)