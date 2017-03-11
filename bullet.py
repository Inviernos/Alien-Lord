'''
bullet class
'''

import pygame

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bullet.gif").convert()
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = -100

    #reset the bullet position
    def reset(self):
        self.rect.x = -100
        self.rect.y = -100
