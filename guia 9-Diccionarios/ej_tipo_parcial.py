# Un grupo de amigos quieren juntarse a cenar pero tienen todos calendarios muy ajustados y les es difícil ver qué días pueden juntarse todos. Se pide escribir una función que reciba un diccionario con los nombres de cada persona, y que como valor asociado tenga los días del mes en los que esa persona no puede juntarse (una lista de números, que pueden ser del 1 al 31), y que devuelva un diccionario con todos los días como claves (también del 1 al 31), y como valor qué amigos pueden asistir cada día.

entrada = {
    "Diego": [4,18,17,26,13,31,30,29],
    "Fede": [2,3,4,6,7,8,9,13,17,18,26],
    "Flor": [1,2,3,4,5,6,7,8,9,13,17,18,19,20,21,23,22,24,25,26],
    "Javi": [1,2,3,4,5,6,7,8,9,13,14,15,16,17,18,19,20,21,23,22,24,25,26,27,28,29]
}

def main(diccionario):
    nuevo_diccionario={}
    for i in range(1,32):
        nuevo_diccionario[i]=["Diego","Fede","Flor","Javi"]
    for i in range(1,32):
        for persona,dias in diccionario.items():
            if i in dias:
                nuevo_diccionario[i].remove(persona)
    return nuevo_diccionario
    
print(main(entrada))
#o tmb:
def mainb(diccionario):
    nuevo_diccionario={}
    for i in range(1,32):
        nuevo_diccionario[i]=list(diccionario.keys())
    for key,value in diccionario.items():
        for dia in value:
            nuevo_diccionario[dia].remove(key)
    return nuevo_diccionario

print(mainb(entrada))

#hecho en clase:

def amigos_por_dia(dicc):
    res = {}
    for i in range(1, 32):
        res[i] = []
    for amigo, dias in dicc.items():
        dias = set(dias)
        for i in range(1, 32):
            if i not in dias:
                res[i].append(amigo)
    return res

resultado = amigos_por_dia(entrada)

for k, v in resultado.items():
    print(k, v)


        
