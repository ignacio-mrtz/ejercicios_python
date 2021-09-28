# Ejercicio 5.7. Números perfectos y números amigos
# a) Escribir una función que devuelva la suma de todos los divisores de un número 𝑛, sin
# incluirlo.
# b) Usando la función anterior, escribir una función que imprima los primeros 𝑚 números
# tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros 𝑚 números
# perfectos).
# c) Usando la primera función, escribir una función que imprima las primeras 𝑚 parejas
# de números (𝑎, 𝑏), tales que la suma de los divisores de 𝑎 es igual a 𝑏 y la suma de los
# divisores de 𝑏 es igual a 𝑎 (es decir las primeras 𝑚 parejas de números amigos).
# d) Proponer optimizaciones a las funciones anteriores para disminuir el tiempo de ejecución.

def suma_de_todos_sus_divisores(nro):
    sum=1
    for i in range(2,nro):
        if nro%i==0:
            sum+=i
    return sum

#print(suma_de_todos_sus_divisores(88))

def imprimir_primeros_m_nros_perfectos(m):
    i=1
    p=0
    while i<=m:
        if suma_de_todos_sus_divisores(p)==p:
            print(p)
            i+=1
        p+=1
    
#imprimir_primeros_m_nros_perfectos(5)#si pones mas de 5 no carga mas xq el sexto es 33 millones y algo

def imprimir_primeras_m_parejas_De_numeros_amigos(m):
    i=1
    a=1
    b=2
    while i<=m:
        if suma_de_todos_sus_divisores(a)==b and suma_de_todos_sus_divisores(b)==a:
            print("(",a,",",b,")")
            i+=1
            b+=1
        elif a<b-1:
            a+=1
        else:
            b+=1
            a=1



imprimir_primeras_m_parejas_De_numeros_amigos(1)




