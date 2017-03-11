import pygame

'''
A label class
'''
class Label(pygame.sprite.Sprite):
   
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", 30)
        self.text = ""
        self.center = (500, 300)
                
    def update(self):
        self.image = self.font.render(self.text, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

