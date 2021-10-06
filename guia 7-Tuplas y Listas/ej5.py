# Ejercicio 7.5. Dada una lista de números enteros, escribir una función que:
# a) Devuelva una lista con todos los que sean primos.
# b) Devuelva la sumatoria y el promedio de los valores.
# c) Devuelva una lista con el factorial de cada uno de esos números.

def primos(enteros):
    primos=[]
    for x in enteros:
        if x==1 or x==0:
            continue
        p=0
        for i in range(2,x):
            if x%i==0:
                p+=1
                break
        if p==0:
            primos.append(x)
    return primos

#print(primos([1,2,3,4,56,6,7,9,0,11,63,13,17]))

#-------------------------------------------------------------------------------

def sumatoria_y_promedio(enteros):
    sumatoria=0
    for i in range(0,len(enteros)):
        sumatoria+=enteros[i]
    promedio=sumatoria/len(enteros)
    return sumatoria,promedio

x,y=sumatoria_y_promedio([1,5,7,9])
#print(x,y)

#-------------------------------------------------------------------------------


def factoriales(enteros):
    factoriales=[]
    for x in enteros:
        fact=1
        for p in range(1,x+1):
            fact*=p
        factoriales.append(fact)
    return factoriales

print(factoriales([1,2,3,4,5,6,7,8,9]))
        
        


                
        
