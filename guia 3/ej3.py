# Ejercicio 3.3. Escribir una función que, dados cuatro números, devuelva el mayor producto de
# dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto
# más grande que se puede obtener entre ellos (8 = −2 × −4).


def main(num1, num2, num3, num4):
    max = num1 * num2
    if num1 * num3 > max:
        max = num1 * num3
    if num1 * num4 > max:
        max = num1 * num4
    if num2 * num3 > max:
        max = num2 * num3
    if num2 * num4 > max:
        max = num2 * num4
    if num3 * num4 > max:
        max = num3 * num4
    return max

print(main(1,5,-2,-4))