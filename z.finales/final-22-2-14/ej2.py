

class Alumno:
    def __init__(self, nombre, padron):
        self.nombre = nombre
        self.padron = padron

class Curso:
    def __init__(self, codigo):
        self.codigo = codigo
        self.inscriptos=[] #lista de los alumnos inscriptos al curso, ordenada por padrón.

    def inscribir(self, alumno):
        # HACER: implementar
        if len(self.inscriptos)==0:
            self.inscriptos.append(alumno)
            print(alumno.padron,alumno.nombre)
            return
        for i in range(0,len(self.inscriptos)):
            if self.inscriptos[i].padron>alumno.padron:
                self.inscriptos.insert(i,alumno)
                print(alumno.padron,alumno.nombre)
            elif self.inscriptos[i].padron==alumno.padron:
                raise Exception("ese padron ya esta inscripto")
            elif i==len(self.inscriptos)-1:
            
        
    def listar(self, k, n):#(2, 1)
        # HACER: implementar en tiempo LINEAL ( O(k) )
#• listar(k, n), que devuelve la n-ésima página (contando desde 0) de alumnos ordenados
#por padrón, donde cada página tiene k alumnos, en tiempo lineal (O(k)). En caso de que
#no haya alumnos en la n-ésima página, devolver una lista vacía.
        if k*n>=len(self.inscriptos):
            return []
        else:
            cant=0
            lista=[]
            while cant<k and k*n+cant<len(self.inscriptos):
                lista.append(self.inscriptos[k*n+cant])
                print(self.inscriptos[k*n+cant].padron)
                cant+=1
            return lista

    def interseccion(self, otro_curso):
        # HACER: implementar en tiempo LINEAL ( O(N + M) )
        #• interseccion(otro_curso) que devuelve la lista ordenada de padrones de los alumnos
#que están inscriptos a ambos cursos, en tiempo lineal (O(N+M) siendo N y M la cantidad de
#alumnos inscriptos en ambos cursos).
        i,j=0,0
        R=[]
        L1=self.inscriptos
        L2=otro_curso.inscriptos
        while i<len(L1) and j>len(L2):
            if L1[i].padron<L2[j].padron:
                R.append(L1[i])
                i+=1
            else:
                R.append(L2[j])
                j+=1
        R+=L1[i:]
        R+=L2[j:]
        return R







def pruebas():
    c = Curso('95.14')

    c.inscribir(Alumno('Fede', 123459))
    c.inscribir(Alumno('Javi', 123460))
    c.inscribir(Alumno('Juani', 123456))
    c.inscribir(Alumno('Lucho', 123458))
    c.inscribir(Alumno('Agus', 123457))

    # Hay 5 alumnos. Ordenados en páginas de 2 alumnos, quedan 3 páginas.

    # Primera página
    pagina0 = c.listar(2, 0)
    assert len(pagina0) == 2
    assert pagina0[0].padron == 123456
    assert pagina0[1].padron == 123457

    # segunda página
    pagina1 = c.listar(2, 1)
    assert len(pagina1) == 2
    assert pagina1[0].padron == 123458
    assert pagina1[1].padron == 123459

    # tercera (y última) página
    pagina2 = c.listar(2, 2)
    assert len(pagina2) == 1
    assert pagina2[0].padron == 123460

    # a partir de n == 3 las páginas están vacías
    assert len(c.listar(2, 3)) == 0

    # otro curso
    c2 = Curso('75.40')
    c2.inscribir(Alumno('Fran', 123432))
    c2.inscribir(Alumno('Javi', 123460))
    c2.inscribir(Alumno('Lucho', 123458))
    c2.inscribir(Alumno('Marga', 123433))

    assert c.interseccion(c2) == [123458, 123460]

    # OPCIONAL: escribir pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()

