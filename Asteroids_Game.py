import pygame, random, math
from Spaceship import *
from Laser import *
from Asteroid import *
pygame.init()
#pygame.key.set_repeat(20, 20)
screen = pygame.display.set_mode([640,480])
black = [0, 0, 0]

print pygame.font.get_default_font()

myfont = pygame.font.SysFont("Arial", 30)
titlefont = pygame.font.SysFont("Baskerville", 100)
pygame.display.set_caption('Asteroids')

mode = 'menu'
explosion_sound = pygame.mixer.Sound('explosion.wav')
laser_sound = pygame.mixer.Sound('laser2.wav')
rocket_sound = pygame.mixer.Sound('Rocket_sound.wav')

Big_shot = pygame.image.load('Blue_Burst.png')

def new_level():
    for x in range(0,2 + level):
        asteroid = Asteroid(1,0,0)
        asteroid_list.append(asteroid)
def bullet_spray():
    for x in range(0,36):
        laser = Laser(spaceship.spaceship_direction + x * 10,spaceship.spaceship_x,spaceship.spaceship_y)
        lasers.append(laser)
    

pygame.mixer.music.load('DST-AngryRobotIII.mp3')
pygame.mixer.music.play(-1)
running = True
while running: #game loop
    for event in pygame.event.get(): #event loop
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and mode == 'menu':
            mode = 'play'
            spaceship = Spaceship()
            asteroid_list = []
            shot_counter = 0
            level = 1
            score = 0
            special = 5
            lasers = []
            new_level()

    pygame.time.delay(20)
    screen.fill(black)

    if mode == 'menu':
        message = myfont.render("Click to Start the Game" , 1, pygame.color.THECOLORS['white'])
        screen.blit(message, (220, 240))
        title = titlefont.render("ASTEROIDS" , 1, pygame.color.THECOLORS['white'])
        screen.blit(title, (130, 100))
        pygame.display.update()
    if mode == 'play':
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            spaceship.rotate("left")
        if keys[pygame.K_RIGHT]:
            spaceship.rotate("right")
        if keys[pygame.K_SPACE] and shot_counter > 9:
            laser = Laser(spaceship.spaceship_direction,spaceship.spaceship_x,spaceship.spaceship_y)
            lasers.append(laser)
            shot_counter = 0
            laser_sound.play()
        if keys[pygame.K_UP]:
             spaceship.booster()
             rocket_sound.play()
        if keys[pygame.K_SLASH] and special > .5 and shot_counter > 9:
            special = special - 1
            shot_counter = 0
            bullet_spray()    
       
        shot_counter = shot_counter + 1
            
        #doing / movement / collisions
        for asteroid in asteroid_list:
            asteroid.move_asteroid()
        spaceship.move()
        
        for laser in lasers:
            laser.move()
            if laser.x > 660 or laser.y > 500 or laser.x < -20 or laser.y < -20:
                lasers.remove(laser)
        
        
        for asteroid in asteroid_list:
            for laser in lasers:
                if laser.rect.colliderect(asteroid.rect):
                    score = score + 1
                    asteroid_list.remove(asteroid)
                    if asteroid.size == 1:
                        asteroid_list.append(Asteroid(2,asteroid.x,asteroid.y))
                        asteroid_list.append(Asteroid(2,asteroid.x,asteroid.y))
                    elif asteroid.size == 2:
                        asteroid_list.append(Asteroid(3,asteroid.x,asteroid.y))
                        asteroid_list.append(Asteroid(3,asteroid.x,asteroid.y))
                    
                  
                    lasers.remove(laser)
                    explosion_sound.play()
                    break
       
        #check if you beat the level
        if len(asteroid_list) == 0:
            level = level + 1
            special = special + .5
            new_level()

        #check if you lost the game  
        for asteroid in asteroid_list:
            if spaceship.rect.colliderect(asteroid.rect):
                explosion_sound.play()
                mode = 'menu'
                
        #draw everything
        for asteroid in asteroid_list:
            screen.blit(asteroid.image, asteroid.rect)
        for laser in lasers:
            screen.blit(laser.image, laser.rect)
            laser.move()
        if running == True:
            screen.blit(spaceship.image, spaceship.rect) 
        label = myfont.render("Score:"+ " " + str(score) , 1, pygame.color.THECOLORS['white'])
        screen.blit(label, (0, 0))
        for x in range(0,int(special)):
            screen.blit(Big_shot, [0 + x * 30, 450])
        pygame.display.update()
        spaceship.booster_off()
        
#pygame.time.delay(1000)
pygame.quit()
