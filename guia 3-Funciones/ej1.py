# Ejercicio 3.1. Escribir dos funciones que permitan calcular:
# a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
# b) La duración en horas, minutos y segundos de un intervalo dado en segundos

def duracion_en_segundos(hora, minutos, segundos):
    resultado = segundos + 60 * minutos + 60 * 60 * hora
    return resultado

#print(duracion_en_segundos(1,24,3))

def duracion_en_hs_min_seg(segundos):
    horas = segundos//(60*60)
    minutos = (segundos%(60*60))//60
    seg = ((segundos%(60*60))%60 )
    return horas,minutos,seg

