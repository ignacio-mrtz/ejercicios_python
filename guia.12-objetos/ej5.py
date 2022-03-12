# Ejercicio 12.5. Crear las clases Materia y Carrera, que se comporten según el siguiente ejemplo:
# >>> analisis2 = Materia("61.03", "Análisis 2", 8)
# >>> fisica2 = Materia("62.01", "Física 2", 8)
# >>> algo1 = Materia("75.40", "Algoritmos 1", 6)
# >>> c = Carrera([analisis2, fisica2, algo1])
# >>> str(c)
# Créditos: 0 -- Promedio: N/A -- Materias aprobadas:
# >>> c.aprobar("95.14", 7)
# ValueError: La materia 75.14 no es parte del plan de estudios
# >>> c.aprobar("75.40", 10)
# >>> c.aprobar("62.01", 7)
# >>> str(c)
# Créditos: 14 -- Promedio: 8.5 -- Materias aprobadas:
# 75.40 Algoritmos 1 (10)
# 62.01 Física 2 (7)

#hecho en clase: mirar practica dia 29 desde min 45 mas o menos

class Materia:
    def __init__(self,codigo,materia,creditos):
        self.codigo=codigo
        self.nombre=materia
        self.creditos=creditos
        self.nota=None 
    
    def __str__(self):
        return f"{self.codigo} {self.nombre} ({self.nota})"

class Carrera:
    def __init__(self,lista_de_materias):
        self.creditos_obtenidos=0
        self.materiasaprobadas=" \n"
        self.lista_de_materias=lista_de_materias
        self.cantidad_de_materias_aprobadas=0
        self.promedio=0
        self.sumatoria_de_notas=0

    def __str__(self):
        return f"Creditos: {self.creditos_obtenidos} -- Promedio: {self.promedio} -- Materias aprobadas: {self.materiasaprobadas}"
    
    def aprobar(self,codigo,nota):
        for materia in self.lista_de_materias:
            if materia.codigo==codigo:
                materia.nota=nota
                self.sumatoria_de_notas+=nota
                if nota>=4:
                    self.creditos_obtenidos+=materia.creditos
                    self.materiasaprobadas+=f"{materia.codigo} {materia.nombre} ({materia.nota})\n"
                    self.cantidad_de_materias_aprobadas+=1
                    self.promedio=self.sumatoria_de_notas/self.cantidad_de_materias_aprobadas
                return
        raise ValueError (f"La materia {codigo} no es parte del plan de estudios")
        


class Materia2:
    def __init__(self,codigo,nombre,creditos):
        self.codigo=codigo
        self.nombre=nombre
        self.creditos=creditos
    def __str__(self):
        return f"{self.codigo} {self.nombre}"

class Carrera2:
    def __init__(self,lista_con_materias_plan_de_estudios):
        self.lista_con_materias_plan_de_estudios=lista_con_materias_plan_de_estudios
        self.materiasaprobadas=[]
        self.suma_notas=0
        self.promedio=0
        self.totalcreditos=0
    
    def __str__(self):
        return f"Créditos: {self.totalcreditos} -- Promedio: {self.promedio} -- Materias aprobadas: {self.materiasaprobadas}"

    def aprobar(self,codigo,nota):
        for i in range(0,len(self.lista_con_materias_plan_de_estudios)):
            if self.lista_con_materias_plan_de_estudios[i].codigo==codigo:
                self.materiasaprobadas.append(f"{self.lista_con_materias_plan_de_estudios[i]} ({nota})")
                self.totalcreditos+=self.lista_con_materias_plan_de_estudios[i].creditos
                self.suma_notas+=nota
                self.promedio=self.suma_notas/len(self.materiasaprobadas)
                return
        raise ValueError(f"La materia {codigo} no es parte del plan de estudios")





