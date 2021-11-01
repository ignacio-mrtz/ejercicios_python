#2. Se busca eliminar una lista de palabras de una cadena. Asumiendo que la cadena y la lista contienen únicamente letras minúsculas y espacios, escribir una función que reciba estos parámetros y devuelva una cadena con el mismo contenido pero sin las palabras de la lista.
#Ejemplo: si la lista de palabras a eliminar es ['buen', 'muy', 'lindo', 'es', 'que'] y la cadena 'muy pero muy buen dia como estas es un buen dia', la función debe devolver 'pero dia como estas un dia'.

def main(palabras_a_eliminar, cadena):
    cadena_nueva=""
    palabras_en_cadena=cadena.split()
    for i,p in enumerate(palabras_en_cadena):
        if p not in palabras_a_eliminar and i==len(palabras_en_cadena)-1:
            cadena_nueva+=p
        elif p not in palabras_a_eliminar:
            cadena_nueva+=p +" "
    return cadena_nueva

main(['buen', 'muy', 'lindo', 'es', 'que'], 'muy pero muy buen dia como estas es un buen dia')





