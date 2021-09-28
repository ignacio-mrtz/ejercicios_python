# Ejercicio 4.5. Escribir funciones que resuelvan los siguientes problemas:
# a) Dado un año indicar si es bisiesto.
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100,
# excepto que también sea divisible por 400.
# b) Dado un mes y un año, devolver la cantidad de días correspondientes.
# c) Dada una fecha (día, mes, año), indicar si es válida o no.
# d) Dada una fecha, indicar los días que faltan hasta fin de mes.
# e) Dada una fecha, indicar los días que faltan hasta fin de año.
# f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
# g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido
# entre ambas, en años, meses y días.
# Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.


def es_bisiesto(año):
    if ((año%4 == 0) and (año%100 == 0) and (año%400 == 0)) or ((año%4 == 0) and not(año%100 == 0)):
        return True
    else:
        return False

#es_bisiesto(2005)

def mesyaño_a_dias(mes,año):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    elif mes == 2 and es_bisiesto(año):
        return 29
    elif mes == 2 and not(es_bisiesto(año)):
        return 28
    else:
        print("ingrese correctamente el mes(ej: para febrero ingrese 2, para diciembre ingrese 12) y el año(ej 2004")

        
#print(mesyaño_a_dias(4,2005))

def fecha_valida(dia,mes,año):
    if dia > mesyaño_a_dias(mes,año):
        return False
    else:
        return True

#print(fecha_valida(29,2,2005))

def dias_que_faltan_para_fin_de_mes(dia,mes,año):
    return mesyaño_a_dias(mes,año) - dia

#print(dias_que_faltan_para_fin_de_mes(20,9,2007))

def dias_que_faltan_para_fin_de_año(dia,mes,año):
    if not(fecha_valida(dia,mes,año)):
        print("ingrese una fecha valida")
        return 
    dias_transcurridos_en_meses_anteriores = 0
    for i in range (1,mes):
        dias_transcurridos_en_meses_anteriores += mesyaño_a_dias(i,año)
    dias_transcurridos_en_el_mes_Actual = dia
    if es_bisiesto(año):
        return 366 - (dias_transcurridos_en_meses_anteriores + dias_transcurridos_en_el_mes_Actual)
    elif not(es_bisiesto(año)):
        return 365 - (dias_transcurridos_en_meses_anteriores + dias_transcurridos_en_el_mes_Actual)

#print(dias_que_faltan_para_fin_de_año(25,4,2009))

def dias_transcurridos_en_el_año_hasta_la_fecha(dia,mes,año):
    if not(fecha_valida(dia,mes,año)):
        print("ingrese una fecha valida")
        return 
    dias_transcurridos_en_meses_anteriores = 0
    for i in range (1,mes):
        dias_transcurridos_en_meses_anteriores += mesyaño_a_dias(i,año)
    dias_transcurridos_en_el_mes_Actual = dia
    return dias_transcurridos_en_meses_anteriores + dias_transcurridos_en_el_mes_Actual

#print(dias_transcurridos_en_el_año_hasta_la_fecha(3,3,2004))



    

