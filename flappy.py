import pygame
from pygame.locals import *

#const
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
SPEED = 10
GRAVITY = 1 

#pygame class for use sprites
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images =[
            pygame.image.load('images/bluebird-upflap.png').convert_alpha(),
            pygame.image.load('images/bluebird-midflap.png').convert_alpha(),
            pygame.image.load('images/bluebird-downflap.png').convert_alpha()
        ]

        self.speed = SPEED

        self.current_image = 0  

        #convert_alpha = use tranparency
        self.image = pygame.image.load('images/bluebird-upflap.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 2
        self.rect[1] = SCREEN_HEIGHT / 2
    
    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        #update height
        self.rect[1] += self.speed

        self.speed += GRAVITY
    
    def bump(self):
        self.speed = -SPEED

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = pygame.image.load('images/background-day.png')
#adjust image scale
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.bump()
    
    #image for all frames and set position
    screen.blit(BACKGROUND, (0,0))

    bird_group.update()
    #draw all elements, pass surface
    bird_group.draw(screen)

    pygame.display.update()