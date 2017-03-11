'''
main function 
'''
import pygame
from alien import *
from alien2 import *
from boss import *
from bosslaser import *
from bullet import *
from Label import *
from laser import *
from player import *

def main():
    
    #initalize pygame
    pygame.init()


    #make variables
    keepgoing = True
    levelone = True
    leveltwo = False
    levelthree = False
    finallevel = False
    death = [[False],[False,False,False],[False,False,False],[False]]
    win = False
    
    
    #set the screen
    screen = pygame.display.set_mode((1000,600))

    pygame.display.set_caption ("ALIEN LORD")

    #load the images
    gameover = pygame.image.load("images/gameover.png").convert()
    road = pygame.image.load("images/background.png").convert()
    winning = pygame.image.load("images/win.png").convert()

    #load the music files
    pygame.mixer.music.load("music/background.ogg")
 
    # set the background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.blit(road,(0,0))

    #set up a sprite group
    allsprites = pygame.sprite.Group()

    
    
    #set up your Label objects
    health = Label()
    nextLevel = Label()
    health.center = (80,20)


    #set up your laser objects
    laser2 = BossLaser()
    laser = Laser()


    #set up bullet object
    bullets = Bullet()
    
    #set up player
    player = Player(bullets,screen)
    
    #set up enemy objects
    enemy = Alien1(50,50,laser)
    enemy2 = Alien1(-100,-100,laser)
    enemy3 = Alien1(-100,-100,laser)
    enemy4 = Alien1(-100,-100,laser)
    enemy5 = Alien2(-100,-100,laser)
    enemy6 = Alien2(-100,-100,laser)
    enemy7 = Alien2(-100,-100,laser)
    boss = Boss(laser2)
    
    
    #add the objects to the sprite group
    allsprites.add(enemy,player,bullets,laser,health,nextLevel,laser2)

    

    #add the background to the screen
    screen.blit(background,(0,0))

    #update the whole screen
    pygame.display.flip()

    #make a variable for framerate
    clock = pygame.time.Clock()
    
    #keep the game going 
    while keepgoing:
        
        #framerate
        clock.tick(30)

    
        
        #the music is not playing right now
        if not pygame.mixer.music.get_busy():
            #play the music 
            pygame.mixer.music.play()
            
        #You are at level 1
        if levelone:
            
            #if the creature is not dead, they will have collision
            if not death[0][0]:

                 #bullet hits the enemy
                 if bullets.rect.colliderect(enemy):
                     bullets.reset()
                     enemy.setHealth()
                     
                 #enemy hits the player
                 if enemy.rect.colliderect(player):
                     player.checkDamage()
                 else:
                     player.setHealth()

                 #laser hits the player
                 if laser.rect.colliderect(player):
                    laser.reset()
                    player.checkDamage()
                    player.setHealth()
    

                

            #creature died
            if enemy.getHealth() == 0:
               
                enemy.kill()
                death[0][0] = True
                laser.reset()
                nextLevel.text = "Next Level -->"
                
                #go to the right side of the screen to go to next level
                if player.rect.x > 880:
                    player.rect.x = 0
                    enemy2.rect.x = 60
                    enemy2.rect.y = 79
                    enemy3.rect.x = 330
                    enemy3.rect.y = 79
                    enemy4.rect.x = 774
                    enemy4.rect.y = 79
                    player.resetHealth()
                    allsprites.add(enemy2,enemy3,enemy4)
                    levelone = False
                    leveltwo = True
                    nextLevel.text = ""
                    
        #you are playing the second level
        if leveltwo:
            
            #enemy is alive
            if not death[1][0]:

                #bullet hits the 1st enemy in level
                if bullets.rect.colliderect(enemy2):
                    enemy2.setHealth()
                    bullets.reset()
                    
                #enemy dies
                if enemy2.getHealth() == 0:
                    enemy2.kill()
                    laser.reset()
                    death[1][0] = True
                
        
            #second enemy is alive
            if not death[1][1]:

                #bullet hits the second enemy in level
                if bullets.rect.colliderect(enemy3):
                    enemy3.setHealth()

                    bullets.reset()
                
                #second enemy dies
                if enemy3.getHealth() == 0:
                    enemy3.kill()
                    laser.reset()
                    death[1][1] = True
             

            #third enemy is alive
            if not death[1][2]:

                #bullet hits the third enemy
                if bullets.rect.colliderect(enemy4):
                    enemy4.setHealth()
                    bullets.reset()

               
                #the third enemy in level is dead
                if enemy4.getHealth() == 0:
                    enemy4.kill()
                    laser.reset()
                    death[1][2] = True

            #Check to see if any enemy hits player
            if enemy2.rect.colliderect(player):
                if not death[1][0]:
                    player.checkDamage()
            elif enemy3.rect.colliderect(player):
                if not death[1][1]:
                    player.checkDamage()
            elif enemy4.rect.colliderect(player):
                if not death[1][2]:
                    player.checkDamage()
            else:
                player.setHealth()
                
            #laser hits the player
            if laser.rect.colliderect(player):
                laser.reset()
                player.checkDamage()
                player.setHealth()
            
    
            #all the creatures are dead at this level
            if death[1][0] and death[1][1] and death[1][2]:
                nextLevel.text = "Next Level -->"

                #when player reaches right side of the screen
                if player.rect.x > 880:
                    player.rect.x = 0
                    enemy5.rect.x = 60
                    enemy5.rect.y = 0
                    enemy6.rect.x = 330
                    enemy6.rect.y = 120
                    enemy7.rect.x = 774
                    enemy7.rect.y = 250
                    player.resetHealth()
                    allsprites.add(enemy5,enemy6,enemy7)
                    leveltwo = False
                    levelthree = True
                    nextLevel.text = ""

        if levelthree:

            #enemy 5 is alive
            if not death[2][0]:

                #the bullet hits enemy 5
                if bullets.rect.colliderect(enemy5):
                    bullets.reset()
                    enemy5.setHealth()

                #the enemy is dead
                if enemy5.getHealth() == 0:
                    laser.reset()
                    enemy5.kill()
                    death[2][0] = True

            #enemy 6 is alive
            if not death[2][1]:

                #the bullet hits enemy 6
                if bullets.rect.colliderect(enemy6):
                    bullets.reset()
                    enemy6.setHealth()

                #the enemy is dead
                if enemy6.getHealth() == 0:
                    laser.reset()
                    enemy6.kill()
                    death[2][1] = True

            #enemy 7 is alive
            if not death[2][2]:

                #the bullet hits enemy 6
                if bullets.rect.colliderect(enemy7):
                    bullets.reset()
                    enemy7.setHealth()

                #the enemy is dead
                if enemy7.getHealth() == 0:
                    laser.reset()
                    enemy7.kill()
                    death[2][2] = True

            #laser hits the player
            if laser.rect.colliderect(player):
                laser.reset()
                player.checkDamage()
                player.setHealth()
            
    
            #all the creatures are dead at this level
            if death[2][0] and death[2][1] and death[2][2]:
                nextLevel.text = "Next Level -->"

                #when player reaches right side of the screen
                if player.rect.x > 880:
                    player.rect.x = 0
                    player.resetHealth()
                    allsprites.add(boss)
                    levelthree = False
                    finallevel = True
                    nextLevel.text = ""
                    
        #You are playing the final level
        if finallevel:

            #boss is alive
            if not death[3][0]:

              
                #the bullet hits the boss
                if bullets.rect.colliderect(boss):
                    bullets.reset()
                    boss.setHealth()

                #the boss is dead
                if boss.getHealth() == 0:
                    win = True
                    laser2.reset()
                    boss.kill()
                    finallevel = False
                    death[3][0] = True
            #the bosses laser hits the player 
            if laser2.rect.colliderect(player):
                laser2.reset()
                player.checkDamage(True)
                player.setHealth()

                    
            
        
        #clear the screen of the sprite
        allsprites.clear(screen,background)

        #update every sprite
        allsprites.update()
            
        
        #draw all the sprites on the screen
        allsprites.draw(screen)
        health.text = "Health: {} / 100".format(player.getHealth())
        
        #player quits the game
        if player.quits():
            keepgoing = False
            time = 0
            
        #the player is dead
        if player.getHealth() == 0:
            screen.blit(gameover,(0,0))
            keepgoing = False
            time = 1000
            

        #The player wins the game
        if win:
            screen.blit(winning,(0,0))
            keepgoing = False
            time = 1000

            
        #update the whole screen
        pygame.display.flip() 
            
    
    #pause the screen
    pygame.time.delay(time)
    
    #quit the game
    pygame.quit()


if __name__ == "__main__":
    main()
