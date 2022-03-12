# Ejercicio 15.3. Escribir una función recursiva que reciba 2 enteros n y b y devuelva True si n es
# potencia de b.
# Ejemplos:
# es_potencia(8, 2) -> True
# es_potencia(64, 4) -> True
# es_potencia(70, 10) -> False

def es_potencia(n,b):
    if b>n:
        return False
    elif b==n:
        return True
    return es_potencia(n/b,b)

print(es_potencia(8, 2))
print(es_potencia(64, 4))
print(es_potencia(70, 10))
print(es_potencia(81, 3))
print(es_potencia(70, 90))