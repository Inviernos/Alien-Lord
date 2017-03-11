'''
boss class
'''

import pygame

class Boss(pygame.sprite.Sprite):
    
    def __init__(self,laser):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/Boss.gif").convert()
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 0
        self.health = 200
        self.laser = laser
        self.lasertimer = 0
        self.left = False
        self.right = True

    #update the boss
    def update(self):
        self.movement()
        self.attack()

    #get the health
    def getHealth(self):
        return self.health
    
    #set the health
    def setHealth(self):
        self.health = self.health - 10
        
    #laser attack of the boss
    def attack(self):
        
        self.lasertimer += 1
        
        if self.lasertimer == 20:
            self.laser.rect.x = self.rect.x + 50
            self.laser.rect.y = self.rect.y
            
        if self.lasertimer > 20:
            self.laser.rect.y += 15
            if self.laser.rect.y > 600:
                self.lasertimer = 0
                self.laser.rect.x = -500
                self.laser.rect.y = -500

    #set up movement for boss
    def movement(self):
        if self.rect.x > 900:
            self.right = False
            self.left = True

        if self.rect.x < 50:
            self.left = False
            self.right = True

        if self.left:
            self.rect.x -= 10
        if self.right:
            self.rect.x += 10
      
