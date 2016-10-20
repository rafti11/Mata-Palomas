import sys, pygame
from pygame.locals import *
 
WIDTH = 750
HEIGHT = 500

class Pajaro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/pajaro.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.5]


def load_image(filename, transparent=False):
    image = pygame.image.load(filename)
    return image
 

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mata pajaros")
 
    background_image = load_image('images/fondo.jpg')
    pajaro = Pajaro()
 
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
 
        screen.blit(background_image, (0, 0))
        screen.blit(pajaro.image, pajaro.rect)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()