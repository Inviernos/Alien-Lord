'''
Boss laser class
'''

import pygame

class BossLaser(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bosslaser.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = -500
        self.rect.y = -500

    #reset the position of laser
    def reset(self):
        self.rect.x = -500
        self.rect.y = -500
