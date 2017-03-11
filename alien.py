'''
Alien1 class
'''

import pygame

class Alien1(pygame.sprite.Sprite):
    #initialize alien
    def __init__(self, x , y, laser):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/alien1.gif").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.laser = laser
        self.track = 0
        self.time = 0
        self.health = 100
        self.lasertimer = 0

    #update the enemy
    def update(self):
        self.animation()
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
            
    #animation of the creature
    def animation(self):
        self.track += 1
        
        if self.track == 5:
            self.image = pygame.image.load("images/alien1down.gif").convert()
      
            
        elif self.track == 10:
            self.image = pygame.image.load("images/alien1up.gif").convert()
            self.track = 0

        
    #get the Health
    def getHealth(self):
        return self.health

    #set the health
    def setHealth(self):
        self.health = self.health - 5
    
    #movement of the enemy
    def movement(self):
        
        move = True
        
        if self.rect.y > 390:
            self.rect.x += 10
            move = False
        if self.rect.x > 500 and self.rect.y > 50:
            self.rect.x += 10
            self.rect.y -= 10
            move = False
        if self.rect.y <= 50:
            self.rect.y = 50
            self.rect.x -= 10
            move = False
        if self.rect.x < 50:
            self.rect.y = 51
            self.rect.x += 5
            self.rect.y += 5
            move = False

        if move:
            self.rect.x += 10
            self.rect.y += 10
    
        
