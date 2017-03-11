'''
alien2
'''

import pygame

class Alien2(pygame.sprite.Sprite):
    #initialize alien
    def __init__(self, x , y, laser):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/alien2.gif").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.laser = laser
        self.time = 0
        self.health = 150
        self.lasertimer = 0
        self.right = True
        self.left = False

    #update the enemy
    def update(self):
        self.attack()
        self.movement()

    #laser attack of the alien 
    def attack(self):
        
        self.lasertimer += 1
        
        if self.lasertimer == 50:
            self.laser.rect.x = self.rect.x + 50
            self.laser.rect.y = self.rect.y
            
        if self.lasertimer > 50:
            self.laser.rect.y += 15
            if self.laser.rect.y > 600:
                self.lasertimer = 0
                self.laser.rect.x = -100
                self.laser.rect.y = -100
 
        
    #get the Health
    def getHealth(self):
        return self.health

    #set the health
    def setHealth(self):
        self.health = self.health - 5
    
    #movement of the enemy
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
        
   
        
          
