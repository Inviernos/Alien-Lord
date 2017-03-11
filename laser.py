'''
laser class
'''

import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/laser.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = -100

    #reset the position of laser
    def reset(self):
        self.rect.x = -100
        self.rect.y = -100
