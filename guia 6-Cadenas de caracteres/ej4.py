# Ejercicio 6.4. Escribir una función que reciba una cadena que contiene un largo número entero
# y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe
# '1234567890', debe devolver '1.234.567.890'.

def main(string):
    numero=int(string)
    print('{0:,}'.format(numero))

main("5134624123214156")

#la siguiente es la que resuelve correctamente el problema. las otras dos son variaciones
def main2(string):
    numero=int(string)
    return format(numero,',d').replace(",",".")

print(main2("3156463574573564363"))

def main3(string):
    nro=int(string)
    return "{:0,.2f}".format(nro)

print(main3("315135643675475475"))