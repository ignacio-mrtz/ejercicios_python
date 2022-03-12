import vectores
import math

def calcular_area_triangulo(Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz):
    ABx, ABy, ABz = vectores.diferencia(Bx, By, Bz, Ax, Ay, Az)
    ACx, ACy, ACz = vectores.diferencia(Cx, Cy, Cz, Ax, Ay, Az)
    Px, Py, Pz = vectores.producto_vectorial(ABx, ABy, ABz, ACx, ACy, ACz)
    return vectores.norma(Px, Py, Pz)/2

print(calcular_area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0))

assert calcular_area_triangulo(1, -1, 3, 7, 4, 1, 7, 2, 3) == 9
assert math.trunc(calcular_area_triangulo(1, 8, 5, 8, 2, 0, 3, 4, 9))== 30
assert calcular_area_triangulo(0, 0, 0, 0, 0, 0, 0, 0, 0) == 0
