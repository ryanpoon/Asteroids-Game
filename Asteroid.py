import pygame, random, math
class Asteroid(pygame.sprite.Sprite):
    image = None
    
    def __init__(self,size,start_x,start_y):
        pygame.sprite.Sprite.__init__(self)
        
        if Asteroid.image is None:
                # This is the first time this class has been
                # instantiated. So, load the image for this and
                # all subsequence instances.
                Asteroid.image = pygame.image.load("asteroid.png")

        self.size = size
        if size == 1:
            self.image = Asteroid.image
            self.rect = self.image.get_rect()
            corner = random.randint(1,4)
            if corner == 1:
                self.x = 50 
                self.y = 50
            if corner == 2:
                self.x = 590
                self.y = 50
            if corner == 3:
                self.x = 50
                self.y = 430
            if corner == 4:
                self.x = 590
                self.y = 430
                
        if size == 2:
            self.image = pygame.transform.scale(Asteroid.image,(45,37))
            self.rect = self.image.get_rect()
            self.x = start_x
            self.y = start_y

        if size == 3:
            self.image = pygame.transform.scale(Asteroid.image,(23,19))
            self.rect = self.image.get_rect()
            self.x = start_x
            self.y = start_y

        
        self.speed_x = random.random() *3-1.5
        self.speed_y = random.random() *3-1.5
        self.rect.center = (self.x, self.y)  

    def move_asteroid(self):
        
        self.x = self.x + self.speed_x
        
        self.y = self.y + self.speed_y
        self.rect.center = (self.x, self.y)
        if self.x < -72:
            self.x = 712
        if self.x > 712:
            self.x = -72
        if self.y < -54:
            self.y = 534
        if self.y > 534:
            self.y = -54
        
