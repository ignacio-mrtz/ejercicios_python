# Ejercicio 4.6. Suponiendo que el primer día del año fue lunes, escribir una función que reciba
# un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo:
# si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'.

def dia_de_la_semana(nro):
    if 1 <= nro <= 366:
        resto = nro%7
        if resto == 1:
            return "lunes"
        if resto == 2:
            return "martes"
        if resto == 3:
            return "miercoles"
        if resto == 4:
            return "jueves"
        if resto == 5:
            return "viernes"
        if resto == 6:
            return "sabado"
        if resto == 0:
            return "domingo"
    else:
        return "el nro no es valido"

#o tmb:

def numero_a_dia(n):
    dias = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sabado']
    return dias[n % 7]

#print(numero_a_dia(7))
    



        

