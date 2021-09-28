# Ejercicio 1.7. Escribir un programa que le pida una palabra al usuario, para luego imprimirla
# 1000 veces, en una única línea, con espacios intermedios.
# Ayuda: Investigar acerca del parámetro end de la función print.

def imprimir_palabra_1000veces():
    palabra = input("ingrese una palabra: ")
    for i in range(1000):
        print(palabra, end= " ") #probar tmb "\t" y "\n" en vez de end

imprimir_palabra_1000veces()


