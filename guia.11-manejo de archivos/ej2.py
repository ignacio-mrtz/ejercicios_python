# 11.2. Escribir una función, llamada cp, que copie todo el contenido de un archivo (sea
# de texto o binario) a otro, de modo que quede exactamente igual.
# Nota: utilizar archivo.read(bytes) para leer como máximo una cantidad de bytes.

def cp(archivo,copia,bytes):
    with open(archivo) as f:
        texto_copiado=f.read(bytes)#Acá proceso y guardo el archivo hasta un determinado byte
    with open(copia,"w") as c:
        c.write(texto_copiado) #acá escribo el texto copiado en un nuevo file. (si el file ya existiera se reemplaza lo q habia, sino lo crea y escribe el texto)

print(cp("tareas.txt","copia.txt",20))

#o tmb:

def cp2(archivo,archivo_nuevo):
    with open(archivo) as f:
        with open(archivo_nuevo,"w") as f2:
            for linea in f:
                linea=linea.rstrip('\n')
                f2.write(f"{linea}\n")

print(cp2("tareas.txt","copia2.txt"))
