from cmu_graphics import *

app.fondo = rgb(60, 60, 60)

# anillo
norte_rotulo = Rótulo('N', 200, 75, relleno='blancoFantasma', tamaño=30)
anillo_fondo = Grupo(Círculo(200, 200, 110, relleno=None, borde='blancoFantasma', anchuraDeBorde=3, guión=(40, 1)),
                Rótulo('S', 200, 325, relleno='blancoFantasma', tamaño=30),
                Rótulo('W', 75, 200, relleno='blancoFantasma', tamaño=30),
                Rótulo('E', 325, 200, relleno='blancoFantasma', tamaño=30),
                norte_rotulo,
                Círculo(200, 200, 145, relleno=None, borde='blancoFantasma', anchuraDeBorde=3, guión=(80, 1)),
                Estrella(200, 200, 100, 12, relleno='blancoFantasma', redondez=20),
                Estrella(200, 200, 100, 12, relleno=app.fondo, redondez=10),
                Estrella(200, 200, 100, 12, relleno='blancoFantasma', redondez=5))

aguja = Linea(200,200,200,120, relleno='carmesi', anchuraDeLinea=8, finalDeFlecha=True)

def enRatónMovido(ratónX, ratónY):
    # Buscar ángulo
    ángulo = anguloA(200,200,ratónX, ratónY)
    # Rotación de aguja
    nuevoX2, nuevoY2 = obtenerPuntoEnDir(200,200,ángulo,80)
    aguja.x2 = nuevoX2
    aguja.y2 = nuevoY2
    anillo_fondo.rotarAngulo = anguloA(200,200,ratónX, ratónY)
cmu_graphics.run()