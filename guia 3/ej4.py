# Ejercicio 3.4. Área de polígonos
# a) Escribir una función que reciba las coordenadas de un vector en ℝ3 (x,y,z) y devuelva
# la norma del vector, dada por ‖(x, y, z)‖ = √𝑥2 + 𝑦2 + 𝑧2.
# Ejemplo: norma(3, 2, -4) → 5.3851
# b) Escribir una función que reciba las coordenadas de dos vectores en ℝ3 (x1,y1,z1,x2,
# y2,z2) y devuelva las coordenadas del vector diferencia (debe devolver 3 valores numéricos).
# Ejemplo: diferencia(8, 7, -3, 5, 3, 2) → (3, 4, -5)
# c) Escribir una función que reciba las coordenadas de dos vectores en ℝ3 y devuelva las
# coordenadas del producto vectorial, definido como:
# (x1,y1,z1)x(x2,y2,z2)=(y1*z2-z1*y2, z1*x2-x1*z2, x1*y2 - y1*x2)
# Ejemplo: producto_vec(1, 4, -2, 3, -1, 0) → (-2, -6, -13)
# d) Utilizando las funciones anteriores, escribir una función que reciba las coordenadas de
# 3 puntos en ℝ3 y devuelva el área del triángulo que conforman.
# Ayuda: Si 𝐴, 𝐵 y 𝐶 son 3 puntos en el espacio, la norma del producto vectorial AB x AC es
# igual al doble del área del triángulo 𝐴𝐵𝐶.
# Ejemplo: area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0) → 19.4551
# e) Escribir una función que reciba las coordenadas de 4 puntos en el plano ℝ2 (x1,y1,x2,
# y2,x3,y3,x4,y4) que conforman un cuadrilátero convexo, y devuelva el área del mismo.
# Ayuda: Aprovechar las funciones escritas anteriormente, asumiendo que los puntos dados
# están en ℝ3 con coordenada 𝑧 = 0.
# Ejemplo: area_cuadrilatero(4, 3, 5, 10, -2, 8, -3, -5) → 65


def norma_de_vector(x, y, z):
    return ((x**2) + (y**2) + (z**2))**(1/2)

#print(norma_de_vector(3,2,-4))

def vector_diferencia(x1, y1, z1, x2, y2, z2):
    return x1 - x2, y1 - y2, z1 - z2

def producto_vectorial(x1, y1, z1, x2, y2, z2):
    return y1 * z2 - z1 * y2, z1 * x2 - x1 * z2, x1 * y2 - y1 * x2

#print(producto_vectorial(1,4,-2,3,-1,0))

def area_traingulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    ABx, ABy, ABz = vector_diferencia(x2, y2, z2, x1, y1, z1)
    ACx, ACy, ACz = vector_diferencia(x3, y3, z3, x1, y1, z1)
    p1, p2, p3 = producto_vectorial(ABx, ABy, ABz, ACx, ACy, ACz)
    return (norma_de_vector(p1,p2,p3)/2)

#print(area_traingulo(5,8,-1,-2,3,4,-3,3,0))

def area_cuadrilatero(x1, y1, x2, y2, x3, y3, x4, y4):
    """Recibe 4 vectores en R2 y devuelve el area del cuadrilátero que conforman"""
    return (1/2) * (
        x1 * y2 
      + x2 * y3 
      + x3 * y4 
      + x4 * y1 
      - y1 * x2 
      - y2 * x3 
      - y3 * x4 
      - y4 * x1
    )

#print(area_cuadrilatero(4, 3, 5, 10, -2, 8, -3, -5))
