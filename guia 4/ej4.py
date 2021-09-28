# Ejercicio 4.4. Escribir funciones que permitan encontrar:
# a) El máximo o mínimo de un polinomio de segundo grado (dados los coeficientes a, b y
# c), indicando si es un máximo o un mínimo.
# b) Las raíces (reales o complejas) de un polinomio de segundo grado.
# Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por
# cero, ni calcular la raíz de un número negativo).
# c) La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta).
# Nota: validar que no sean dos rectas con la misma pendiente, antes de efectuar la operación.

import cmath

def max_o_min_de_polinomio_grado_2(a,b,c):
    pto_critico_x = (-b) / (2*a)
    pto_critico_y = (a*(pto_critico_x**2) + b*(pto_critico_x) + c)
    if a < 0:
        print("(",pto_critico_x,",",pto_critico_y,")", " es un maximo")
    else:
        print("(",pto_critico_x,",",pto_critico_y,")", " es un minimo")

def raices_de_un_polinomio(a,b,c):
    discriminante = (b**2) - 4 *a * c
    if discriminante > 0:
        raiz1 = (-b + (discriminante)**(1/2)) / (2 * a)
        raiz2 = (-b - (discriminante)**(1/2)) / (2 * a)
        print("las raices son: ",raiz1, "y", raiz2)
    elif discriminante == 0:
        raizdoble = (-b) / (2 * a)
        print("la raiz dobles es: ", raizdoble)
    else:
        raiz1real = (-b) / (2 * a)
        raiz1imag = ((-discriminante)**(1/2)) / (2*a)
        raiz2real = (-b) / (2 * a)
        raiz2imag = -((-discriminante)**(1/2)) / (2*a)
        print("las raices son complejas y son: ", complex(raiz1real,raiz1imag)," y ", complex(raiz2real,raiz2imag))

    
#raices_de_un_polinomio(1,2,81)
#max_o_min_de_polinomio_grado_2(1,2,81)

def interseccion_de_2_rectas(pendiente1, ordenada_al_origen1, pendiente2, ordenada_al_origen2):
    if pendiente1 == pendiente2 and ordenada_al_origen1 != ordenada_al_origen2:
        print("las rectas son paralelas")
    elif pendiente1 == pendiente2 and ordenada_al_origen1 == ordenada_al_origen2:
        print("ambas son rectas iguales")
    else:
        x = ((ordenada_al_origen2 - ordenada_al_origen1)/(pendiente1-pendiente2))
        y = (pendiente1 * x) + ordenada_al_origen1
        print("el pto de interseccion es: ", "(",x,",",y,")")

interseccion_de_2_rectas(4,-1,-2,5)
