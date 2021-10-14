# Del primer parcialito, segundo cuatrimestre de 2015
# 1) Escribir una funcion que imprima los numeros de 1 a 100; pero para los multiplos de 3 imprima \Miki" en lugar # del numero; y para los multiplos de 5 imprima \Moko". Para los multiplos de 3 y 5 debe imprimir \MikiMoko".

def main():
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print("MikiMoko")
        elif i%3==0:
            print("Miki")
        elif i%5==0:
            print("Moko")
        else:
            print(i)
        
main()