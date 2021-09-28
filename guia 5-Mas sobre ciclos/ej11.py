# Ejercicio 5.11. Escribir una función que reciba un dígito y un número natural, y decida numéricamente
# si el dígito se encuentra en la notación decimal del segundo.

import math

def se_encuentra_el_digito_en_dicha_notacion_decimal(digito,natural):
    for c in str(natural - math.trunc(natural)):
        if c==str(digito):
            return True
    return False

print(se_encuentra_el_digito_en_dicha_notacion_decimal(9,22.29))
