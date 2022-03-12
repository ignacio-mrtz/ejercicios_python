import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 300
JUGADORES=["O","X"]
def juego_crear():
    """Inicializar el estado del juego"""
    matriz={(60,60):" ", (80,60):" ", (100,60):" ", (120,60):" ", (140,60):" ", (160,60):" ", (180,60):" ", (200,60):" ", (220,60):" ", (240,60):" ", (60,80):" ", (80,80):" ", (100,80):" ", (120,80):" ", (140,80):" ", (160,80):" ", (180,80):" ", (200,80):" ", (220,80):" ", (240,80):" ", (60,100):" ", (80,100):" ", (100,100):" ", (120,100):" ", (140,100):" ", (160,100):" ", (180,100):" ", (200,100):" ", (220,100):" ", (240,100):" ", (60,120):" ", (80,120):" ", (100,120):" ", (120,120):" ", (140,120):" ", (160,120):" ", (180,120):" ", (200,120):" ", (220,120):" ", (240,120):" ", (60,140):" ", (80,140):" ", (100,140):" ", (120,140):" ", (140,140):" ", (160,140):" ", (180,140):" ", (200,140):" ", (220,140):" ", (240,140):" ", (60,160):" ", (80,160):" ", (100,160):" ", (120,160):" ", (140,160):" ", (160,160):" ", (180,160):" ", (200,160):" ", (220,160):" ", (240,160):" ", (60,180):" ", (80,180):" ", (100,180):" ", (120,180):" ", (140,180):" ", (160,180):" ", (180,180):" ", (200,180):" ", (220,180):" ", (240,180):" ", (60,200):" ", (80,200):" ", (100,200):" ", (120,200):" ", (140,200):" ", (160,200):" ", (180,200):" ", (200,200):" ", (220,200):" ", (240,200):" ", (60,220):" ", (80,220):" ", (100,220):" ", (120,220):" ", (140,220):" ", (160,220):" ", (180,220):" ", (200,220):" ", (220,220):" ", (240,220):" ", (60,240):" ", (80,240):" ", (100,240):" ", (120,240):" ", (140,240):" ", (160,240):" ", (180,240):" ", (200,240):"", (220,240):" ", (240,240):" "  
    }
    return matriz


def juego_actualizar(juego, x, y, contador):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
        
    for horizontal,vertical in juego.keys():
        if horizontal-10<x<horizontal+10 and vertical-10<y<vertical+10 and juego[(horizontal, vertical)]==" ":
            juego[(horizontal, vertical)]=JUGADORES[contador%2]
            contador+=1
           
    return juego, contador

def juego_mostrar(juego,contador):
    """Actualizar la ventana"""
    gamelib.draw_text('5 en línea', 150, 20)
    
    gamelib.draw_text(f"Turno: {JUGADORES[contador%2]}", 150, 280, font='Helvetica', size=14, bold=False, italic=False, anchor="c")
    gamelib.draw_rectangle(50, 50, 250, 250, outline='white', fill=None)
    
    for x in range(70,250,20):
        gamelib.draw_line(50, x, 250, x, fill='white', width=1)
        gamelib.draw_line(x, 50, x, 250, fill='white', width=1)

    for y in range(60,260,20):
        gamelib.draw_text(f"{juego[(y,60)]}", y, 60, font='Helvetica', size=14, bold=False, italic=False, anchor="c")
        gamelib.draw_text(f"{juego[(y,80)]}", y, 80, font='Helvetica', size=14, bold=False, italic=False, anchor="c")
        gamelib.draw_text(f"{juego[(y,100)]}", y, 100, font='Helvetica', size=14, bold=False, italic=False, anchor="c")
        gamelib.draw_text(f"{juego[(y,120)]}", y, 120, font='Helvetica', size=14, bold=False, italic=False, anchor="c")
        gamelib.draw_text(f"{juego[(y,140)]}", y, 140, font='Helvetica', size=14, bold=False, italic=False, anchor="c")
        gamelib.draw_text(f"{juego[(y,160)]}", y, 160, font='Helvetica', size=14, bold=False, italic=False, anchor="c")
        gamelib.draw_text(f"{juego[(y,180)]}", y, 180, font='Helvetica', size=14, bold=False, italic=False, anchor="c")
        gamelib.draw_text(f"{juego[(y,200)]}", y, 200, font='Helvetica', size=14, bold=False, italic=False, anchor="c")
        gamelib.draw_text(f"{juego[(y,220)]}", y, 220, font='Helvetica', size=14, bold=False, italic=False, anchor="c")
        gamelib.draw_text(f"{juego[(y,240)]}", y, 240, font='Helvetica', size=14, bold=False, italic=False, anchor="c")


def main():
    juego = juego_crear()
    contador=0

    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego, contador)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego,contador = juego_actualizar(juego, x, y, contador)

gamelib.init(main)