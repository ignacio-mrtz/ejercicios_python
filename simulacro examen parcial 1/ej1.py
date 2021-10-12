# 1. Escribir una función que realice lo siguiente: 
# - Le pida al usuario que ingrese una contraseña. Luego debe validar que la misma: 
#     - Tenga al menos dos numeros, pero no tenga más números que letras (a-z, A-Z, no es necesario incluir letras #       acentuadas o especiales de otros idiomas que no sea el ingles).
#     - Tenga alguno de estos caracteres ("!", "@", "~", "/", "#") pero no más de tres.
# - Si no ingresa una contraseña válida debe volver a preguntarle hasta quedarse sin intentos.
# - Cuando sea válida, se deben devolver la cantidad de intentos restante.
# Si se acaban los intentos, debe mostrar un mensaje por pantalla y devolver -1. La cantidad de intentos es recibida # por parametro.

def main(intentos):
    while True:
        contraseña = list(input("ingrese una contraseña: "))
        numeros=0
        letras=0
        simbolos=0
        for i in range(0,len(contraseña)):
            if contraseña[i] in "1234567890":
                numeros+=1
            if contraseña[i].isalpha():
                letras+=1
            if contraseña[i] in '"!", "@", "~", "/", "#"':
                simbolos+=1
    
        intentos = intentos-1
    
        if 1<numeros<=letras and 0<simbolos<4:
            return intentos
        if intentos==0:
            print("se te acabaron los intentos")
            return -1

#print(main(3))

def main2(intentos):
    while True:
        if intentos==0:
            print("se te acabaron los intentos")
            return -1 
        contraseña=input("escriba su contraseña: ")
        numeros=0
        letras=0
        simbolos=0
        for c in contraseña:
            if c in "1234567890":
                numeros+=1
            if c.isalpha():
                letras+=1
            if c in '"!", "@", "~", "/", "#"':
                simbolos+=1

        intentos = intentos-1

        if 1<numeros<=letras and 0<simbolos<4:
            return intentos
        
#print(main2(2))
