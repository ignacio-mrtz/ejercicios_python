def tail(entrada, salida, n):
    # HACER: implementar la funcion

def pruebas():
    tail("entrada.txt", "salida.txt", 6)

    # salida.txt debería contener las siguientes 6 líneas:
    #
    # Pero ponga su esperanza
    # en el Dios que lo formó;
    # y aquí me despido yo
    # que he relatao a mi modo
    # MALES QUE CONOCEN TODOS,
    # PERO QUE NAIDES CONTÓ.

    from os import path
    print(f"{path.basename(__file__)}: OK (verificar el contenido de salida.txt)")

pruebas()
