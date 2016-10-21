import sys, pygame
from pygame.locals import *
 
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
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.5]

    def actualizar(self, time):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time


def load_image(filename, transparent=False):
    image = pygame.image.load(filename)
    return image

def imagen_cursor(x,y):
     self.image = load_image("images/mira.png", True)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    

    
    pygame.display.set_caption("Mata pajaros")
 
    background_image = load_image('images/fondo.jpg')
    pajaro = Pajaro()
    cursorjuego = Cursorjuego()
    clock = pygame.time.Clock()
 
    while True:
        time = clock.tick(60)
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        pajaro.actualizar(time)
        screen.blit(background_image, (0, 0))
        screen.blit(pajaro.image, pajaro.rect)
        x,y = pygame.mouse.get_pos()
        x -= cursorjuego.image.get_width() / 2
        y -= cursorjuego.image.get_height() / 2
        screen.blit(cursorjuego.image,(x, y))
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()