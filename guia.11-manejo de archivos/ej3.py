# 11.3. Escribir una función, llamada wc, que dado un archivo de texto, lo procese e
# imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.

def wc(archivo):
    with open(archivo) as f:
        lineas=0
        palabras=0
        caracteres=0
        for linea in f:
            linea=linea.rstrip("\n")
            lineas+=1
            palabras_en_linea=linea.split(" ")
            palabras+=len(palabras_en_linea)
            caracteres_en_linea=len("".join(palabras_en_linea))
            caracteres+=caracteres_en_linea
        print("cantidad de lineas:", lineas, "palabras: ", palabras, "caracteres: ", caracteres)

wc("tareas.txt")

#otra forma:

def wc2(arch):
    with open(arch) as f:
        lineas = [linea.rstrip('\n') for linea in f]
        palabras_suma = 0
        letras_suma = 0
        for linea in lineas:
            palabras = linea.split(' ')
            palabras_suma += len(palabras)
            for palabra in palabras:
                letras_suma += len(palabra)
        print(
            f'lineas: {len(lineas)}, palabras: {palabras_suma}, caracteres: {letras_suma}')


wc2('tareas.txt')

# 11.3. Escribir una función, llamada wc, que dado un archivo de texto, lo procese e
# imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.

def wc3(archivo):
    lineas=0
    palabras=0
    caracteres=0
    with open(archivo) as f:
        for linea in f:
            linea=linea.rstrip("\n")
            lineas+=1
            for c in linea:
                caracteres+=1
                #tomo en cuenta los espacios
            palabras+=len(linea.split(" "))
    print(lineas,palabras,caracteres)
            
wc3('tareas.txt')
