from cmu_graphics import *
import random
app.fondo = 'negro'

Rótulo('By: Joel Valencia', 330, 370, relleno='blanco', tamaño=14)
sol = Estrella(200, 200, 35, 400, relleno=gradiente('naranja', 'amarillo', 'rojoNaranja'))
mercurio = Grupo(
    Círculo(200, 200, 50, relleno=None, borde='grisOscuro'),
    Círculo(200, 150, 10, relleno=gradiente('gris', 'gainsboro', inicio='izquierda-superior'))
    )
venus = Grupo(
    Círculo(200, 200, 70, relleno=None, borde='grisOscuro'),
    Círculo(200, 130, 10, relleno=gradiente('caqui', 'caquiOscuro', inicio='izquierda-superior'))
    )
tierraPlaneta = Círculo(200, 110, 10, relleno=gradiente('verde', 'azulReal', inicio='izquierda-superior'))
orbitaDeLuna = Grupo(
    Círculo(tierraPlaneta.centroX, tierraPlaneta.centroY, 13, relleno=None, borde='grisOscuro', anchuraDeBorde=1, opacidad=30),
    Círculo(tierraPlaneta.centroX-13, tierraPlaneta.centroY, 3, relleno=gradiente('gris', 'blanco', inicio='izquierda-superior'))
    )
tierra = Grupo(
    Círculo(200, 200, 90, relleno=None, borde='grisOscuro'),
    orbitaDeLuna,
    tierraPlaneta
    )
marte = Grupo(
    Círculo(200, 200, 110, relleno=None, borde='grisOscuro'),
    Círculo(200, 90, 10, relleno=gradiente('rojo', 'ladrillo', inicio='izquierda-superior'))
    )
jupiter = Grupo(
    Círculo(200, 200, 130, relleno=None, borde='grisOscuro'),
    Círculo(200, 70, 10, relleno=gradiente('naranja', 'oro', 'caqui', inicio='izquierda-superior'))
    )
saturno = Grupo(
    Círculo(200, 200, 150, relleno=None, borde='grisOscuro'),
    Círculo(200, 50, 10, relleno=gradiente('caqui', 'salmonClaro', inicio='izquierda-superior')),
    Ovalo(200,50,30,28, relleno=None, borde=gradiente('granate','caquiOscuro', 'salmonOscuro'), anchuraDeBorde=2)
    )
urano = Grupo(
    Círculo(200, 200, 170, relleno=None, borde='grisOscuro'),
    Círculo(200, 30, 10, relleno=gradiente('azul', 'azulCielo', inicio='izquierda-superior'))
    )
neptuno = Grupo(
    Círculo(200, 200, 190, relleno=None, borde='grisOscuro'),
    Círculo(200, 10, 10, relleno=gradiente('azulGandul', 'azulCieloProfundo', inicio='izquierda-superior'))
    )
posición_x = 0
posición_y = 0

def crearEstrella(posición_x, posición_y):
    Estrella(posición_x, posición_y, 2, 5, relleno='blanco', borde='nieve', opacidad=15)

def enPaso():
    # Si la dirección de la tierra es en sentido horario, agregue 3 al rotarÁngulo.
    # Si no, reste 3.
    ### Pon tu código aquí ###
    mercurio.rotarAngulo -= 2.3
    venus.rotarAngulo -= 2
    tierra.rotarAngulo -= 1.7
    orbitaDeLuna.rotarAngulo += 1.3
    marte.rotarAngulo -= 1.5
    jupiter.rotarAngulo -= 1.3
    saturno.rotarAngulo -= 1
    urano.rotarAngulo -= 0.7
    neptuno.rotarAngulo -= 0.5
    sol.puntos += 1
    # Satelites y cometas
    posición_x = random.randint(-1600,1600)
    posición_y = random.randint(-1600,1600)
    crearEstrella(posición_x, posición_y)
    
cmu_graphics.run()