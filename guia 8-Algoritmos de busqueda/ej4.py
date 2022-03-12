# Ejercicio 8.4. Sistema de facturación simplificado
# Se cuenta con una lista ordenada de productos, en la que uno consiste en una tupla de (identificador,
# descripción, precio), y una lista de los productos a facturar, en la que cada uno consiste
# en una tupla de (identificador, cantidad).
# Se desea generar una factura que incluya la cantidad, la descripción, el precio unitario y el precio
# total de cada producto comprado, y al final imprima el total general.
# Escribir una función que reciba ambas listas e imprima por pantalla la factura solicitada.

lista_ordenada_de_productos=[(1,"zapatillas",11500),(12,"cordones",570),(34,"botas",15700),(124,"ojotas",1300)]
lista_de_productos_a_facturar=[(1,8),(34,5)]


def main(lista_ordenada_de_productos, lista_de_productos_a_facturar):
    for x in lista_de_productos_a_facturar:
        der=len(lista_ordenada_de_productos)-1
        izq=0
        while der>=izq:
            medio=(der+izq)//2
            if lista_ordenada_de_productos[medio][0]==x[0]:
                print(f'cantidad: {x[1]}\t | descripcion: {lista_ordenada_de_productos[medio][1]:15s}\t | precio unidad:{lista_ordenada_de_productos[medio][2]}\t | precio total: {lista_ordenada_de_productos[medio][2]*x[1]}')
                print("-----------------------------------------------------------------------------------------------------")
                break
            if lista_ordenada_de_productos[medio][0]>x[0]:
                der=medio-1
            else:
                izq=medio+1
            

main(lista_ordenada_de_productos, lista_de_productos_a_facturar)


def main2(lista_de_productos,productos_comprados):
    total=0
    for x in productos_comprados:
        for c in lista_de_productos:
            if x[0]==c[0]:
                print(f"{c[1]} cantidad:{x[1]} precio unitario: {c[2]} precio total: {c[2]*x[1]}")
                total+=c[2]*x[1]
                break
    print(f"total general: {total}")
        
main2(lista_ordenada_de_productos, lista_de_productos_a_facturar)

