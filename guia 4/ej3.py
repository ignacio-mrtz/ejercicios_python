# Ejercicio 4.3. Escribir una función que reciba por parámetro una dimensión 𝑛, e imprima la
# matriz identidad correspondiente a esa dimensión

def matriz_identidad(n):
    for j in range(n):
        for i in range(n):
            if i == j:
                print(1, end= " ")
            elif i == (n-1):
                print(0)
            else:
                print(0, end=" ")

#matriz_identidad(4)

#o tmb:

def matriz_identidad2(n):
    area = n**2
    row = 1
    for col in range(1, area + 1):
        if(col % n == row or col == area):
            print(1, end=" ")
        else:
            print(0, end=" ")
        
        if (col % n == 0):
            print()
            row += 1


