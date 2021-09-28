# Ejercicio 5.9. Escribir una función que reciba dos números como parámetros, y devuelva cuántos
# múltiplos del primero hay, que sean menores que el segundo.
# a) Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
# b) Implementarla utilizando un ciclo while, que multiplique el primer número hasta que
# sea mayor que el segundo.
# c) Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operaciones?

def cuantos_multiplos_del_primero_menores_que_el_segundo(nro1,nro2):
    multiplos=0
    for i in range(nro1,nro2):
        if i%nro1==0:
            multiplos+=1
    return multiplos

#print(cuantos_multiplos_del_primero_menores_que_el_segundo(2,7))
        
def cuantos_multiplos_del_primero_menores_que_el_segundo_b(nro1,nro2):
    i=1
    while nro1*i<nro2:
        i+=1
    return i-1
print(cuantos_multiplos_del_primero_menores_que_el_segundo_b(2,11))

#el while realiza menos operaciones.