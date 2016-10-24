import sys, pygame
from pygame.locals import *
import time
import random
from pygame.mixer import music

WIDTH = 750
HEIGHT = 500

class Cursorjuego(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/mira.png", True)
        self.rect = self.image.get_rect()

class Pajaro(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/pajaro.png", True)
        self.rect = self.image.get_rect()


def load_image(filename, transparent=False):
    image = pygame.image.load(filename)
    return image

def imagen_cursor(x,y):
     self.image = load_image("images/mira.png", True)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mata pajaros")
    background_image = load_image('images/fondo.jpg')
    gameover = load_image('images/game.png')
    contador = 0
    cursorjuego = Cursorjuego()
    borra = pygame.sprite.Group()
    raton = pygame.mouse.get_pos()
    pajaro = Pajaro()
    borra.add(pajaro)
    pajaro.rect.centerx = random.randrange(WIDTH)
    pajaro.rect.centery = random.randrange(400)

    time = 10
    pygame.time.set_timer(USEREVENT+1, 1000)

    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

            if eventos.type == USEREVENT+1:
                
                if time > 0:
                    time -= 1

            
            if eventos.type == pygame.MOUSEBUTTONDOWN and pajaro.rect.collidepoint(pygame.mouse.get_pos()):

                for elimina in borra:

                    borra.remove(elimina)
                    contador+=100
                    borra.add(pajaro)
                    pajaro.rect.centerx = random.randrange(WIDTH)
                    pajaro.rect.centery = random.randrange(400)
                    pygame.mixer.music.load('musica/pa.mp3')
                    pygame.mixer.music.play(0)       
            

        while time==0:
            if time == 0:
            
                borra.remove(pajaro)
                screen.blit(gameover, (0, 0))
                font2 = pygame.font.SysFont(None, 40)
                text2 = font2.render("Tu puntuacion es: "+str(contador), 1, (255,255,0))
                screen.blit(text2,(100,50))
                text3 = font2.render("Pulsa cualquier tecla para volver a jugar", 1, (255,255,0))
                screen.blit(text3,(100,415))
                pygame.display.update()
                
            for eventos in pygame.event.get():
                if eventos.type == pygame.KEYDOWN:
                    main()
                if eventos.type == QUIT:
                    sys.exit(0)

                



        screen.blit(background_image, (0, 0))
        borra.draw(screen)
        
      
        x,y = pygame.mouse.get_pos()
        x -= cursorjuego.image.get_width() / 2
        y -= cursorjuego.image.get_height() / 2
        screen.blit(cursorjuego.image,(x, y))
        font = pygame.font.SysFont(None, 25)
        text = font.render("Puntuacion: "+str(contador), 1, (255,255,0))
        screen.blit(text,(10,10))
        text4 = font.render("Tiempo restante: " + str(time) + " s", 1, (255,255,0))
        screen.blit(text4,(550,10))
        pygame.display.flip()

    return 0

if __name__ == '__main__':
    pygame.init()
    main()