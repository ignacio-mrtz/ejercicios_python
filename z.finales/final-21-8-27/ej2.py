def rot47(entrada, salida):
    # HACER: implementar la función

def pruebas():
    rot47("texto.txt", "salida.txt")

    # texto.txt contiene:
    #
    # Aquí me pongo a cantar
    # Al compás de la vigüela,
    # Que el hombre que lo desvela
    # Una pena estraordinaria
    # Como la ave solitaria
    # Con el cantar se consuela.


    # salida.txt debe contener:
    #
    # pBFí >6 A@?8@ 2 42?E2C
    # p= 4@>AáD 56 =2 G:8ü6=2[
    # "F6 6= 9@>3C6 BF6 =@ 56DG6=2
    # &?2 A6?2 6DEC2@C5:?2C:2
    # r@>@ =2 2G6 D@=:E2C:2
    # r@? 6= 42?E2C D6 4@?DF6=2]

    from os import path
    print(f"{path.basename(__file__)}: OK (verificar el contenido de salida.txt)")

pruebas()

