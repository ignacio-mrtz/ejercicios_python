# Escribir un programa que le pida al usuario que ingrese un número entero positivo n y una cadena, e imprima la misma cadena pero con un guión (-) cada n lugares.
# 
# Ejemplo: n = 2, cadena = Otra frase devuelta; debe imprimir Es-to- e-s -un- e-je-mp-lo-.
# 
# Ingrese una frecuencia: 2
# Ingrese una frase: Esto es un ejemplo.
# Es-to- e-s -un- e-je-mp-lo-.
# Otro ejemplo: n = 1, cadena = Otra frase devuelta; debe imprimir O-t-r-a- -f-r-a-s-e- -d-e-v-u-e-l-t-a
# 
# Ingrese una frecuencia: 1
# Ingrese una frase: Otra frase devuelta
# O-t-r-a- -f-r-a-s-e- -d-e-v-u-e-l-t-a

def main():
    n=int(input("Ingrese una frecuencia: "))
    cadena=input("Ingrese una frase: ")
    cadena_nueva=""
    for i,x in enumerate(cadena) :
        if i%n==0 and i!=0 :
            cadena_nueva+="-"+x
        else:
            cadena_nueva+=x
    print(cadena_nueva)

main()

print(main())