# Ejercicio 2.3. Escribir una función que convierta un valor dado en grados Fahrenheit a grados
# Celsius. Recordar que la fórmula para la conversión es: 𝐹 = (9/5)* 𝐶 + 32

def farenheit_a_celsius(farenheit):
    celsius = (farenheit - 32) * (5 / 9)
    return celsius

#farenheit_a_celsius(257)

