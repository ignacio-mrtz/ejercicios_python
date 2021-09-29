# Ejercicio 6.9. Implementar la función pedir_entero(mensaje, min, max), que debe imprimir
# el mensaje y luego esperar a que el usuario ingrese un valor. Si el valor ingresado no es un
# número entero, o no es un número entre min y max (inclusive), se le debe avisar al usuario y
# pedir el ingreso de otro valor. Una vez que el usuario ingresa un valor válido, la función lo debe
# devolver.

# Ejemplo:
# >>> z = pedir_entero("¿Cuál es tu número favorito?", -50, 50)
# ¿Cuál es tu número favorito? [-50..50]:
# Por favor ingresa un número entre -50 y 50.
# ¿Cuál es tu número favorito? [-50..50]: hola
# Por favor ingresa un número entre -50 y 50.
# ¿Cuál es tu número favorito? [-50..50]: -60
# Por favor ingresa un número entre -50 y 50.
# ¿Cuál es tu número favorito? [-50..50]: 51
# Por favor ingresa un número entre -50 y 50.
# ¿Cuál es tu número favorito? [-50..50]: -16
# >>> z
# -16

def pedir_entero(mensaje, min, max):
    respuesta= input(f"{mensaje} [{min}..{max}]:")
    while not(respuesta.lstrip('-').isdigit() and min<=int(respuesta)<=max):
        print(f"Por favor ingresa un nro entre {min} y {max}.")
        respuesta= input(f"{mensaje} [{min}..{max}]: ")
    return respuesta

    
pedir_entero("Cual es tu nro favorito?",-50,50)

#resolucion de clase:

def pedir_entero(min, max):
    '''Le pide al usuario que ingrese un valor. Si el valor ingresado no es un número entero, o no es un número entre min y max (inclusive), le avisa al usuario y pide el ingreso de otro valor.'''
    valor = input(f'Ingrese un entero entre {min} y {max} ') #str
    while not valor.isdigit() or not min <= int(valor) <= max:
        print('el valor ingresado no es valida')
        valor = input(f'Ingrese un entero entre {min} y {max} ') 
    return int(valor)

def pedir_entero(min, max):
    while True:
        valor = input(f'Ingrese un entero entre {min} y {max} ' ) 
        if valor.isdigit() and min <= int(valor) <= max:
            return int(valor)
        print('el valor ingresado no es valida')