def loteria(ruta,lista_ganadora):
    with open("premios.csv","w") as r:
        with open(ruta) as f:
            for linea in f:
                linea=linea.rstrip("\n")
                lista=linea.split(",")
                numeros=lista[1].split("-")
                contador=0
                for numero in numeros:
                    numero=int(numero)
                    if numero in lista_ganadora:
                        contador+=1
                if contador>=2:
                    cadena=f"{lista[0]}, {contador}\n"
                    r.write(cadena)

loteria("tickets.csv",[10, 15, 4, 156, 69])

