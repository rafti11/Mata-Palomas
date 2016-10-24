import sys, pygame
from pygame.locals import *
import time
import random

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

    contador = 0
    cursorjuego = Cursorjuego()
    borra = pygame.sprite.Group()
    raton = pygame.mouse.get_pos()
    pajaro = Pajaro()
    borra.add(pajaro)
    pajaro.rect.centerx = random.randrange(WIDTH)
    pajaro.rect.centery = random.randrange(400)

    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

            if eventos.type == pygame.MOUSEBUTTONDOWN and pajaro.rect.collidepoint(pygame.mouse.get_pos()):

                for elimina in borra:

                    borra.remove(elimina)
                    contador+=100
                    borra.add(pajaro)
                    pajaro.rect.centerx = random.randrange(WIDTH)
                    pajaro.rect.centery = random.randrange(400)


        screen.blit(background_image, (0, 0))
        borra.draw(screen)
        x,y = pygame.mouse.get_pos()
        x -= cursorjuego.image.get_width() / 2
        y -= cursorjuego.image.get_height() / 2
        screen.blit(cursorjuego.image,(x, y))
        font = pygame.font.SysFont(None, 25)
        text = font.render("Puntuacion: "+str(contador), 1, (255,255,0))
        screen.blit(text,(10,10))
        pygame.display.flip()

    return 0

if __name__ == '__main__':
    pygame.init()
    main()