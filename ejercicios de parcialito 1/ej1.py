# Escribir un programa que imprima los números de 1 a 100; pero para los múltiplos de 3 imprima "Miki" en lugar del # número; y para los múltiplos de 5 imprima "Moko". Para los múltiplos de 3 y 5 debe imprimir "MikiMoko".



def main():
    for i in range(1,101):
        if i%5==0 and i%3==0:
            print("MikiMoko")
        elif i%5==0:
            print("Moko")
        elif i%3==0:
            print("Miki")
        else:
            print(i)
    
main()