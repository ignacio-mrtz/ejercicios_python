import gamelib
import png
from pila import Pila

def paint_nuevo(ancho, alto):
    '''inicializa el estado del programa con una imagen vacía(en blanco) de ancho x alto pixels'''
    paint={}
    for i in range(0,alto):
        for j in range(0,ancho):
            paint[(i,j)]="#FFFFFF"
    
    return paint


def paint_mostrar(paint,color_opcional,recuadro_en_amarillo,recuadro_en_azul,recuadro_en_blanco,recuadro_en_negro, recuadro_en_rojo, recuadro_en_verde,ancho,alto,recuadro_en_balde,recuadro_en_pincel,ancho_total,alto_total):
    '''dibuja la interfaz de la aplicación en la ventana'''
    gamelib.draw_begin()

    gamelib.draw_rectangle(0,0, ancho_total,alto_total, outline='black', fill="#808080")

    #CUADRICULADO DEL PAINT:

    gamelib.draw_rectangle(20, 20, (20*ancho)+20, (20*alto)+20, outline='white', fill="white")

    coordenada_y=0
    for i in range(20,(20*ancho)+20,20):
        coordenada_x=0
        for j in range(20,(20*alto)+20,20):
            gamelib.draw_rectangle(i, j, i+20, j+20, outline='grey', fill=f"{paint[(coordenada_x,coordenada_y)]}")
            coordenada_x+=1
        coordenada_y+=1
    

    #BOTONES DE COLORES PARA SELECCIONAR EL COLOR:

    gamelib.draw_rectangle(20,(20*alto)+40, 50, (20*alto)+70, outline=recuadro_en_blanco, width="4", fill="#FFFFFF")
    gamelib.draw_rectangle(70,(20*alto)+40, 100, (20*alto)+70, outline=recuadro_en_negro, width="4", fill="#000000")
    gamelib.draw_rectangle(120,(20*alto)+40, 150, (20*alto)+70, outline=recuadro_en_rojo, width="4", fill="#FF0000")
    gamelib.draw_rectangle(170,(20*alto)+40, 200, (20*alto)+70, outline=recuadro_en_verde, width="4", fill="#00FF00")
    gamelib.draw_rectangle(220,(20*alto)+40, 250, (20*alto)+70, outline=recuadro_en_azul, width="4", fill="#0000FF")
    gamelib.draw_rectangle(270,(20*alto)+40, 300, (20*alto)+70, outline=recuadro_en_amarillo, width="4", fill="#FFFF00")
    gamelib.draw_rectangle(320,(20*alto)+40, 350, (20*alto)+70, outline='black',width=2, fill=color_opcional, dash=(3,5))
    gamelib.draw_text("* Color a elección", 390, (20*alto)+55, font=None, size=7, bold=False, italic=False, fill="black")

    #BOTONES PARA REALIZAR OTRO TIPO DE ACCIONES(BALDE DE PINTURA,REHACER Y DESHACER)

    gamelib.draw_rectangle(20, (20*alto)+100, 80, (20*alto)+130, outline=recuadro_en_pincel, width="4", fill="white")
    gamelib.draw_text("PINCEL", 50, (20*alto)+115, font=None, size=11, bold=False, italic=False, fill="black")
    gamelib.draw_rectangle(100, (20*alto)+100, 160, (20*alto)+130, outline=recuadro_en_balde, width="4", fill="white")
    gamelib.draw_text("BALDE", 130, (20*alto)+115, font=None, size=11, bold=False, italic=False, fill="black")
    gamelib.draw_rectangle(180, (20*alto)+100, 240, (20*alto)+130, outline='black', fill="white")
    gamelib.draw_text("UNDO", 210, (20*alto)+115, font=None, size=11, bold=False, italic=False, fill="black")
    gamelib.draw_rectangle(260, (20*alto)+100, 320, (20*alto)+130, outline='black', fill="white")
    gamelib.draw_text("REDO", 290, (20*alto)+115, font=None, size=11, bold=False, italic=False, fill="black")
    
    #BOTONES PARA GUARDAR O EDITAR IMAGENES:

    gamelib.draw_rectangle(20, (20*alto)+150, 120, (20*alto)+180, outline='black', fill="white")
    gamelib.draw_text("Guardar PPM", 70, (20*alto)+165, font=None, size=11, bold=False, italic=False, fill="black")
    gamelib.draw_rectangle(140, (20*alto)+150, 240,(20*alto)+180, outline='black', fill="white")
    gamelib.draw_text("Cargar PPM", 190, (20*alto)+165, font=None, size=11, bold=False, italic=False, fill="black")
    gamelib.draw_rectangle(260, (20*alto)+150, 360, (20*alto)+180, outline='black', fill="white")
    gamelib.draw_text("Guardar PNG", 310, (20*alto)+165, font=None, size=11, bold=False, italic=False, fill="black")


    gamelib.draw_end()

def chequear_rgb(codigo):
    """recibe el texto ingresado por el usuario y si es un codigo rgb devuelve True"""
    for x in codigo[1:7]:
        if x not in "0123456789abcdefABCDEF":
            return False
    return True

def pintar_con_balde(cuadrado_seleccionado, color_actual, color_del_balde, paint):
    x,y=cuadrado_seleccionado

    if paint[(x,y)]==color_actual:
        paint[(x,y)]=color_del_balde 
        
    if ((x+1,y) in paint)==True and paint[(x+1,y)]==color_actual:
        pintar_con_balde((x+1,y), color_actual, color_del_balde,paint)

    if ((x,y+1) in paint)==True and paint[(x,y+1)]==color_actual:
        pintar_con_balde((x,y+1), color_actual, color_del_balde,paint)

    if ((x-1,y) in paint)==True and paint[(x-1,y)]==color_actual:
        pintar_con_balde((x-1,y), color_actual, color_del_balde,paint)

    if ((x,y-1) in paint)==True and paint[(x,y-1)]==color_actual:
        pintar_con_balde((x,y-1), color_actual, color_del_balde,paint)

    return None

def main():
    gamelib.title("AlgoPaint")
    ancho=15
    alto=15
    ancho_total=ancho*20+350
    alto_total=alto*20+200
    gamelib.resize(ancho_total, alto_total)
    paint = paint_nuevo(ancho, alto)
    color_opcional="#FFFFFF"
    color_seleccionado="#FFFFFF"
    recuadro_en_blanco=""
    recuadro_en_negro=""
    recuadro_en_rojo=""
    recuadro_en_verde=""
    recuadro_en_azul=""
    recuadro_en_amarillo=""
    recuadro_en_pincel="black"
    recuadro_en_balde=""
    boton_presionado=False
    balde=False
    pila_deshacer=Pila()
    pila_rehacer=Pila()
    copia_inicial=paint.copy()
    while gamelib.is_alive():

        paint_mostrar(paint,color_opcional,recuadro_en_amarillo,recuadro_en_azul,recuadro_en_blanco,recuadro_en_negro, recuadro_en_rojo, recuadro_en_verde,ancho,alto,recuadro_en_balde,recuadro_en_pincel,ancho_total,alto_total)

        ev = gamelib.wait()
        if not ev:
            break

        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:


            #SELECCIONAR COLOR CON UN CLICK Y GENERAR BORDE BLANCO EN COLOR SELECCIONADO:

            if 20<ev.x<50 and (20*alto)+40<ev.y<(20*alto)+70:
                color_seleccionado="#FFFFFF"
                recuadro_en_blanco="white"
                recuadro_en_negro=""
                recuadro_en_rojo=""
                recuadro_en_verde=""
                recuadro_en_azul=""
                recuadro_en_amarillo=""
            elif 70<ev.x<100 and (20*alto)+40<ev.y<(20*alto)+70:
                color_seleccionado="#000000"
                recuadro_en_negro="white"
                recuadro_en_blanco=""
                recuadro_en_rojo=""
                recuadro_en_verde=""
                recuadro_en_azul=""
                recuadro_en_amarillo=""
            elif 120<ev.x<150 and (20*alto)+40<ev.y<(20*alto)+70:
                color_seleccionado="#FF0000"
                recuadro_en_rojo="white"
                recuadro_en_blanco=""
                recuadro_en_negro=""
                recuadro_en_verde=""
                recuadro_en_azul=""
                recuadro_en_amarillo=""
            elif 170<ev.x<200 and (20*alto)+40<ev.y<(20*alto)+70:
                color_seleccionado="#00FF00"
                recuadro_en_verde="white"
                recuadro_en_blanco=""
                recuadro_en_negro=""
                recuadro_en_rojo=""
                recuadro_en_azul=""
                recuadro_en_amarillo=""
            elif 220<ev.x<250 and (20*alto)+40<ev.y<(20*alto)+70:
                color_seleccionado="#0000FF"
                recuadro_en_azul="white"
                recuadro_en_blanco=""
                recuadro_en_negro=""
                recuadro_en_rojo=""
                recuadro_en_verde=""
                recuadro_en_amarillo=""
            elif 270<ev.x<300 and (20*alto)+40<ev.y<(20*alto)+70:
                color_seleccionado="#FFFF00"
                recuadro_en_amarillo="white"
                recuadro_en_blanco=""
                recuadro_en_negro=""
                recuadro_en_rojo=""
                recuadro_en_verde=""
                recuadro_en_azul=""
            elif 320<ev.x<350 and (20*alto)+40<ev.y<(20*alto)+70:
                color_elegido=gamelib.input("Escriba el código rgb del color que desea usar(Ej: Para el color rosa escriba: #FF00FF):")
                if color_elegido!=None:
                    if color_elegido[0]=="#" and len(color_elegido)==7 and chequear_rgb(color_elegido)==True:
                        color_opcional=color_elegido
                        color_seleccionado=color_opcional
                    else:
                        gamelib.say("Ingrese un codigo rgb correcto")
                recuadro_en_negro=""
                recuadro_en_blanco=""
                recuadro_en_rojo=""
                recuadro_en_verde=""
                recuadro_en_azul=""
                recuadro_en_amarillo=""

            elif 20<ev.x<(20*ancho)+20 and 20<ev.y<(20*alto)+20:
                #DIBUJAR CON PINCEL O BALDE EN CUADRICULADO CON UN CLICK:
                if balde==True:
                    pintar_con_balde(((ev.y//20)-1,(ev.x//20)-1), paint[(ev.y//20)-1,(ev.x//20)-1], color_seleccionado,paint)
                else:
                    boton_presionado=True
                    paint[(ev.y//20)-1,(ev.x//20)-1]=color_seleccionado

                #copia=paint.copy()
                copia={}
                for clave,valor in paint.items():
                    copia[clave]=valor

                pila_deshacer.apilar(copia)

                while not pila_rehacer.esta_vacia():
                    pila_rehacer.desapilar()

            elif 20<ev.x<80 and (20*alto)+100<ev.y<(20*alto)+130:
                #PINCEL
                balde=False
                recuadro_en_pincel="black"
                recuadro_en_balde=""

            elif 100<ev.x<160 and (20*alto)+100<ev.y<(20*alto)+130:
                #BALDE
                balde=True
                recuadro_en_balde="black"
                recuadro_en_pincel=""

            elif 180<ev.x<240 and (20*alto)+100<ev.y<(20*alto)+130:
                #UNDO
                if not pila_deshacer.esta_vacia():
                    pila_rehacer.apilar(pila_deshacer.desapilar())
                    if not pila_deshacer.esta_vacia():
                        copia=pila_deshacer.ver_tope()
                        for clave,valor in copia.items():
                            paint[clave]=valor
                    else:
                        for clave,valor in copia_inicial.items():
                            paint[clave]=valor
                        continue
                else:
                    for clave,valor in copia_inicial.items():
                        paint[clave]=valor
                    continue
                
            elif 260<ev.x<320 and (20*alto)+100<ev.y<(20*alto)+130:
                #REDO
                if not pila_rehacer.esta_vacia():
                    pila_deshacer.apilar(pila_rehacer.desapilar())
                    paint=pila_deshacer.ver_tope()

            elif 20<ev.x<120 and (20*alto)+150<ev.y<(20*alto)+180:
                #GUARDAR PPM
                nombre_archivo=gamelib.input("Ingrese el nombre que desea ponerle al archivo(Ej: imagen.ppm):")
                if nombre_archivo!=None:
                    with open(nombre_archivo,"w") as f:
                        f.write("P3\n")
                        f.write(f"{alto} {ancho}\n")
                        f.write("255\n")
                        for i in range(0,alto):
                            for j in range(0,ancho):
                                f.write(f"{int(paint[(i,j)][1:3], 16)} {int(paint[(i,j)][3:5], 16)} {int(paint[(i,j)][5:7], 16)}\n")
                    gamelib.say(f"{nombre_archivo} fue guardado exitosamente")

            elif 140<ev.x<240 and (20*alto)+150<ev.y<(20*alto)+180:
                #CARGAR PPM
                ruta_de_archivo_cargado=gamelib.input("Ingrese la ruta del archivo que desea cargar:")
                if ruta_de_archivo_cargado!=None:
                    try:
                        with open(ruta_de_archivo_cargado) as f:
                            next(f)
                            tamaño=f.readline()
                            tamaño=tamaño.rstrip("\n")
                            pixeles_de_ancho,pixeles_de_alto=tamaño.split(" ")
                            next(f)
                            for i in range(0,int(pixeles_de_ancho)):
                                for j in range(0,int(pixeles_de_alto)):
                                    linea=f.readline()
                                    linea=linea.rstrip("\n")
                                    primera_componente,segunda_componente,tercera_componente=linea.split(" ")
                                    paint[i,j]=f"#{int(primera_componente):02x}{int(segunda_componente):02x}{int    (tercera_componente):02x}"
                    except:
                        gamelib.say("El nombre del archivo no existe. Vuelva a intentar")

            elif 260<ev.x<360 and (20*alto)+150<ev.y<(20*alto)+180:
                #GUARDAR PNG
                nombre_png=gamelib.input("Ingrese el nombre del archivo que desea guardar(Ej: imagen.png):")

                if nombre_png!=None and nombre_png[-3:len(nombre_png)]=="png":

                    def pasar_de_hexa_a_dec(hexa):
                        return (int(hexa[1:3],16),int(hexa[3:5],16),int(hexa[5:7],16))

                    paleta=[]

                    imagen=[]

                    for i in range(0,alto):
                        imagen.append([])
                        for j in range(0,ancho):

                            if pasar_de_hexa_a_dec(paint[(i,j)]) not in paleta:
                                paleta.append(pasar_de_hexa_a_dec(paint[(i,j)]))
                                imagen[i].append(len(paleta)-1)
                            else:
                                for p,color in enumerate(paleta):
                                    if pasar_de_hexa_a_dec(paint[(i,j)])==color:
                                        imagen[i].append(p)


                    png.escribir(f"{nombre_png}", paleta, imagen)
                    gamelib.say(f"Imagen {nombre_png} fue guardado exitosamente")


        elif boton_presionado==True and ev.type == gamelib.EventType.Motion and 20<ev.x<(20*ancho)+20 and 20<ev.y<(20*alto)+20:
            #PINTAR CON EL HACIENDO CLICK Y ARRASTRANDO EL CURSOR AL MISMO TIEMPO:
            paint[(ev.y//20)-1,(ev.x//20)-1]=color_seleccionado

        elif ev.type == gamelib.EventType.ButtonRelease and ev.mouse_button == 1:

            boton_presionado=False


gamelib.init(main)

