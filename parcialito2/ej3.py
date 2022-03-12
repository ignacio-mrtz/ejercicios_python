class Usuario:
    def __init__(self,nombre,mail):
        self.nombre=nombre
        self.mail=mail
        self.enespera=False
        self.ensesion=False

    def __str__(self):
        return f"nombre del usuario: {self.nombre}, mail del usuario: {self.mail}"

class GoogleMeet:
    def __init__(self,creador):#creador es un usuario
        self.nombre=creador.nombre
        self.mail=creador.mail
        self.usuarios_en_sesion=0
        self.usuarios_en_espera=0

    def __str__(self):
        return f"usuarios de la sesion: {self.usuarios_en_sesion}, usuarios esperando a ser conectados:{self.usuarios_en_espera}"

    def ingresar(self):
        if self.enespera==True:
            raise Exception("Usuario ya se encuentra en espera")
        elif self.ensesion==True:
            raise Exception("Usuario ya se encuentra en la sesión")
        elif self.enespera==False:
            self.enespera==True

    def aceptar(self,mail):

        if self.enespera==False:
            raise Exception("Usuario no se encuentra en espera")
        elif self.enespera==True:

    def eliminar(self,mail):
        #no pude terminar




        

