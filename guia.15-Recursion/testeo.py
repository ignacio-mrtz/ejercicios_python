def es_potencia(n, b):
    if n==b:
        return True
    elif n<b:
        return False
    else:
        n=n//b
        es_potencia(n,b)

print(es_potencia(8,2))