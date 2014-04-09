import pygame, random, math
class Laser(pygame.sprite.Sprite):
    image = None
    
    def __init__(self,direction,x,y):
        pygame.sprite.Sprite.__init__(self)
        
        if Laser.image is None:
                # This is the first time this class has been
                # instantiated. So, load the image for this and
                # all subsequence instances.
                Laser.image = pygame.image.load("laser-sword.png")
        self.y = y
        self.x = x
        self.direction = direction
        self.steps = 0
        self.speed = 9
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        loc = self.rect.center
        self.image = pygame.transform.rotate(Laser.image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = loc


    def move(self):  
        radians = math.radians(self.direction)
        self.x = self.x - math.sin(radians) * self.speed
        self.y = self.y - math.cos(radians) * self.speed
        self.rect.center = (self.x, self.y)  
        #self.rect = self.image.get_rect()

        
