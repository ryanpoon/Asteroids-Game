
import pygame, random, math
from Spaceship import *
pygame.init()
pygame.key.set_repeat(20, 20)
screen = pygame.display.set_mode([640,480])
black = [0, 0, 0]
shot_x = 0
shot_y = 0
do_it = True
from Asteroid import *      
spaceship = Spaceship()
        
running = True
while running: #game loop
    for event in pygame.event.get(): #event loop
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                spaceship.rotate("left")
            if event.key == pygame.K_RIGHT:
                spaceship.rotate("right")
            if event.key == pygame.K_SPACE:
                shoot()
                do_it == False
         
            if event.key == pygame.K_UP:
                 spaceship.booster()
            #if event.key == pygame.K_DOWN:
    
        
    pygame.time.delay(20)
    screen.fill(black)
    
    #if shooting == True:
        
        


    spaceship.move()
    if do_it == True:
        shot_x = spaceship.spaceship_x
        shot_y = spaceship.spaceship_y
    pygame.draw.rect(screen, (255,0,0), [shot_x, shot_y, 5, 5])
    screen.blit(spaceship.image, spaceship.rect,)
    pygame.display.update()

pygame.quit()
