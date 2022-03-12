class Materia:
    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.nota = None

    def poner_nota(self, nota):
        self.nota = nota
    
    def __str__(self):
        return f"{self.codigo} {self.nombre} ({self.nota})"

class Carrera:
    def __init__(self, materias):
        self.materias = materias
        self.aprobadas = []

    def __str__(self):
        creditos = 0
        suma_notas = 0
        representacion_materias = ""
        for materia in self.aprobadas:
            creditos += materia.creditos
            suma_notas += materia.nota
            representacion_materias += str(materia) + "\n"

        if len(self.aprobadas) == 0:
            promedio = 'N/A'
        else:
            promedio = str(suma_notas/len(self.aprobadas))
        return f"Créditos: {creditos} -- Promedio: {promedio} -- Materias aprobadas:\n{representacion_materias}"

    def aprobar(self, codigo, nota):
        for materia in self.materias:
            if codigo == materia.codigo:
                materia.poner_nota(nota)
                self.aprobadas.append(materia)
                return
        raise ValueError(f"La materia {codigo} no es parte del plan de estudios")