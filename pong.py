import pygame

ALTO = 600
ALTO_PALA = 100
ANCHO = 800
ANCHO_PALA = 20
MARGEN = 30

COLOR_FONDO = (0,0,0) #RGB (red, green, blue)
COLOR_OBJETOS = (200, 200, 200)


class Pong:

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pass

    def jugar(self):
        salir = False
        cont = 0

        while not salir:
            #bucle principal (main loop)
            cont = cont+1
            print(cont)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    #print('Se ha cerrado la ventana')
                    salir = True
                
                #print('Se ha producido un evento del tipo:', evento)

            # renderizar mis objetos

            # 1. borrar la pantalla (pìntar un cuadrado del mismo color de fondo del mismo tamaño de la pantalla)
            pygame.draw.rect(self.pantalla, COLOR_FONDO, ((0,0), (ANCHO, ALTO)))

            # 2. pintar jugador 1 (izquierda)
            # pygame.rect(izq, arriba, ancho, alto)
            arriba = (ALTO-ALTO_PALA) / 2   #ALTO/2 - ALTO_PALA/2
            jugador1 = pygame.Rect(MARGEN, arriba, ANCHO_PALA, ALTO_PALA)
            pygame.draw.rect(self.pantalla, COLOR_OBJETOS, jugador1)

            # 3. pintar jugador 2 (derecha)
            izquierda = ANCHO - MARGEN - ANCHO_PALA
            jugador2 = pygame.Rect(izquierda, arriba, ANCHO_PALA, ALTO_PALA)
            pygame.draw.rect(self.pantalla, COLOR_OBJETOS, jugador2)

            # 4. pintar la red
            self.pintar_red()

            # mostrar los cambios en la pantalla 
            pygame.display.flip()

        pygame.quit()

    def pintar_red(self):
        pos_x = ANCHO / 2

        tramo_pintado = 20
        tramo_vacio = 15
        ancho_red = 6

        for y in range(0, ALTO, tramo_pintado + tramo_vacio):
            pygame.draw.line(
                self.pantalla, 
                COLOR_OBJETOS, 
                (pos_x, y), 
                (pos_x, y + tramo_pintado), 
                width = ancho_red)
            

if __name__ == '__main__':
    juego = Pong()
    juego.jugar()





