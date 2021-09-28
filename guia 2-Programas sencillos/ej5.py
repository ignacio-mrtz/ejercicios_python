# Ejercicio 2.5. a) Escribir una función que dado un número entero devuelva 1 si el mismo
# es impar y 0 si fuera par.
# b) Escribir una función que dado un número entero devuelva 0 si el mismo es impar y 1 si
# fuera par.
# c) Escribir una función que dado un número entero devuelva el dígito de las unidades. Por
# ejemplo, para 153 debe devolver 3.
# d) Escribir una función que dado un número devuelva el primer número múltiplo de 10
# inferior a él. Por ejemplo, para 153 debe devolver 150.

def par_o_impar(numero):
    if numero%2 == 0:
        return 0
    else:
        return 1

#print(par_o_impar(36))

def par_o_impar_punto_b(numero):
    if numero%2 == 0:
        return 1
    else:
        return 0

#print(par_o_impar_punto_b(45))

def digito_de_las_unidades(numero):
    digitos = str(numero)
    return digitos[-1]

#print(digito_de_las_unidades(1574232))

def punto_d(numero):
    for i in range (numero, 1, -1):
        resultado = i
        if resultado%10 == 0:
            return resultado

#print(punto_d(47))
        
