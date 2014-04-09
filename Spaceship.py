import pygame, random, math
class Spaceship(pygame.sprite.Sprite):
    
    image = None
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        if Spaceship.image is None:
                # This is the first time this class has been
                # instantiated. So, load the image for this and
                # all subsequence instances.
                Spaceship.image = pygame.image.load("spaceship.png")
                Spaceship.image2 = pygame.image.load("spaceship booster.png")
        self.image = Spaceship.image
       
        self.rect = self.image.get_rect()
        self.spaceship_x = 320
        self.spaceship_y = 240
        self.speed_x = 0
        self.speed_y = 0
        self.spaceship_direction = 0
        self.rect.center = (self.spaceship_x, self.spaceship_y)


    def move(self):
        self.spaceship_x = self.spaceship_x + self.speed_x
        self.spaceship_y = self.spaceship_y + self.speed_y
        if self.spaceship_x < -36:
            self.spaceship_x = 636
        if self.spaceship_x > 636:
            self.spaceship_x = -36
        if self.spaceship_y < -26:
            self.spaceship_y = 480
        if self.spaceship_y > 480:
            self.spaceship_y = -26
        self.rect.center = (self.spaceship_x, self.spaceship_y)

    #create a rotate function
    def rotate(self,direction):
        if direction == "left":
            self.spaceship_direction = self.spaceship_direction + 6
        else:
            self.spaceship_direction = self.spaceship_direction - 6
        
        
    def shoot(self):
        self.shooting = True
        self.shot_direction = self.spaceship_direction
        #pygame.transform.rotate(,self.spaceship_direction)
        
    def booster(self):
        loc = self.rect.center
        self.image = pygame.transform.rotate(Spaceship.image2, self.spaceship_direction)
        self.rect = self.image.get_rect()
        self.rect.center = loc
        radians = math.radians(self.spaceship_direction)
        self.speed_x = self.speed_x - math.sin(radians) * .1
        self.speed_y = self.speed_y - math.cos(radians) * .1

    def booster_off(self):
        loc = self.rect.center
        self.image = pygame.transform.rotate(Spaceship.image, self.spaceship_direction)
        self.rect = self.image.get_rect()
        self.rect.center = loc
