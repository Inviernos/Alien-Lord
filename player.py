'''
player class
'''
import pygame

class Player(pygame.sprite.Sprite):
    #initialize character
    def __init__(self , bullet, screen):
        #sprite properties
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/player.gif").convert()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 410

        #variables
        self.screen = screen
        self.bullet = bullet
        self.Masterimage = self.bullet.image
        self.moveX = 0
        self.moveY = 0
        self.bulletx = 0
        self.bullety = 0
        self.dir = 0
        self.health = 100
        self.damage = False
        self.bossdamage = False
        self.timer = 60

        self.moveright = False
        self.moveleft = False
        
        self.north = False
        self.east = False
        self.west = False
        self.quit = False
        
    #update the character
    def update(self):
        
        self.checkKeys()
        self.checkBorders()
        self.bulletMovement()
        self.animation()
            
    #did you get hit by enemy
    def checkDamage(self,bosslevel = False):
        if not bosslevel:
            self.damage = True
        else:
            self.bossdamage = True

    def quits(self):
        return self.quit
           
    #get the health of the player
    def getHealth(self):
        return self.health

    #set the health of the player
    def setHealth(self):
        if self.damage:
            self.health -= 10
            self.damage = False

        if self.bossdamage:
            self.health -= 20
            self.bossdamage = False

    #reset the health 
    def resetHealth(self):
        self.health = 100
            
        
    #have the bullet move
    def bulletMovement(self):

        if self.north:
            self.bullet.rect.y -= 20
        elif self.west:
            self.bullet.rect.x -= 20
        elif self.east:
            self.bullet.rect.x += 20
            
    #check the borders
    def checkBorders(self):
        x = self.rect.x
        
        if x > 890:
            self.rect.x = 890
        elif x < 0:
            self.rect.x = 0

    #change image of the character when he turns
    def turn(self, num):
        if num == 1:
            self.image = pygame.image.load("images/playerleft.gif").convert()
            self.rect.y = 410
        elif num == 2:
            self.image = pygame.image.load("images/player.gif").convert()
            self.rect.y = 410
        elif num == 3:
            self.image = pygame.image.load("images/playerup.gif").convert()
        
    #change the rotation of the bullet
    def rotation(self):
        if self.dir == 90:
            self.bullet.image = pygame.transform.rotate(self.Masterimage, 90)
            self.north = True
        if self.dir == 180:
            self.bullet.image = pygame.transform.rotate(self.Masterimage, 180)
            self.west = True
        if self.dir == 0:
            self.bullet.image = pygame.transform.rotate(self.Masterimage, 0)
            self.east = True
             
    #check the user's input
    def checkKeys(self):
        #get the input of the user
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.quit = True
                      
                #user presses down on the key
                if event.type==pygame.KEYDOWN:

                    
                    if event.key==pygame.K_a:

                        self.moveX -= 10
                        self.turn(1)
                        self.dir = 180
                        self.moveleft = True
                       
                      

                    if event.key==pygame.K_d:

                        self.moveX += 10
                        self.turn(2)
                        self.dir = 0
                        self.timer = 0
                        self.moveright = True
                        

                    if event.key==pygame.K_w:
                        self.turn(3)
                        self.dir = 90
                        self.moveright = False
                        self.moveleft = False
                        
                    if event.key == pygame.K_SPACE:
                        if self.reset():
                            self.bullet.rect.x = self.rect.x +  30
                            self.bullet.rect.y = self.rect.y  + 20
                            self.rotation()
                        
      
                        
                    #user lets go of the key
                if event.type==pygame.KEYUP:

                    if event.key==pygame.K_a:

                        self.moveX += 10
                        self.moveleft = False
                
        
                        
                    if event.key==pygame.K_d:

                        self.moveX -= 10
                        self.moveright = False

                  
            #change the position of the player           
            self.rect.x += self.moveX
            self.rect.y += self.moveY
        
    #reset position of bullet
    def reset(self):
        if self.bullet.rect.x > 1000:
            self.north = False
            self.west = False
            self.east = False
            return True
        elif self.bullet.rect.x < 0:
            self.north = False
            self.west = False
            self.east = False
            return True
        elif self.bullet.rect.y < 0:
            self.north = False
            self.west = False
            self.east = False
            return True
        else:
            return False
        
    #animation of the player
    def animation(self):
        
        self.timer += 1

        #player is moving right
        if self.moveright:
            if self.timer == 10:
                self.image = pygame.image.load("images/playerwalk.gif").convert()

            if self.timer == 20:
                self.image = pygame.image.load("images/player.gif").convert()
                self.timer = 0

        #player is moving left
        elif self.moveleft:
            if self.timer == 10:
                self.image = pygame.image.load("images/playerleftwalk2.gif").convert()

            if self.timer == 20:
                self.image = pygame.image.load("images/playerleft.gif").convert()
                self.timer = 0
        else:
            self.timer = 0
         
