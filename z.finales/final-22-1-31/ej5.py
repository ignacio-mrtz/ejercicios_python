# El algoritmo de compresión RLE (Run Length Encoding) funciona reemplazando secuencias
# del mismo símbolo consecutivo por el símbolo y la cantidad de ocurrencias. Por ejemplo,
# al comprimir la cadena "aaaabcccaaa" queda "4a1b3c3a".
# Implementar la función comprimir que reciba una cadena s y la comprima mediante el algoritmo
# RLE.

def comprimir(s):
    # HACER: implementar la funcion
    nueva_cadena=""
    caracter=None
    cantidad=0
    for i in range(len(s)):
        if caracter==None:
            caracter=s[i]
            cantidad+=1
        elif s[i]==caracter:
            cantidad+=1
        if s[i]!=caracter or s[i]==caracter and i==len(s)-1:
            nueva_cadena+=f"{cantidad}{caracter}"
            caracter=s[i]
            cantidad=1
    print(nueva_cadena)
    return nueva_cadena


def pruebas():
    assert comprimir("aaaabcccaaa") == "4a1b3c3a"

    # OPCIONAL: pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()

