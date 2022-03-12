def agrupar_diccionarios(lista_de_diccionarios):
    diccionario_global={}
    for i in range(0,len(lista_de_diccionarios)):
        for clave,valor in lista_de_diccionarios[i].items():
            diccionario_global[clave]=diccionario_global.get(clave,[])
            diccionario_global[clave].append(valor)
    return diccionario_global

print(agrupar_diccionarios([{"clave_1": 1, "clave_2": 2, "clave_3": 3}, {"clave_1": 4, "clave_3": 5},{"clave_4": 6, "clave_3": 7, "clave_2": 8}]))





