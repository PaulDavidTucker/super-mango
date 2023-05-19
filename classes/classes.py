from typing import Any
import pygame
import screenSize

class Sprite(pygame.sprite.Sprite):

    def __init__(self, image, start_X, start_Y):

        super().__init__()

        self.image = pygame.image.load("./assets/" + image)
        self.X = start_X
        self.Y = start_Y
        self.rect = self.image.get_rect()
        
        self.rect.center = (self.X, self.Y)

    def update(self):
        #TODO: Add update function to allow for movement
        pass

    def draw(self,screen):
        screen.blit(self.image, self.rect)
    
class Player(Sprite):

    def __init__(self, image, start_X, start_Y):
        super().__init__(image, start_X, start_Y)


class Enemy(Sprite):
    
    def __init__(self, image, start_X, start_Y):
        super().__init__(image, start_X, start_Y)

class Box(Sprite):

    def __init__(self, image, start_X, start_Y):
        super().__init__(image, start_X, start_Y)

class Background:

    #Object to modify the scrolling background

    def __init__(self, image, speed):
        self.Image = image
        self.Speed = speed
        self.counter = 0

        # Create the background image
        self.background_image = pygame.image.load("./assets/" + self.Image)
        self.background_image = pygame.transform.scale(self.background_image, (screenSize.SCREEN_WIDTH, screenSize.SCREEN_HEIGHT))

    def Move(self,screen):
        screen.fill((0, 0, 0))
        # Move the background
        screen.blit(self.background_image, (self.counter, 0))
        screen.blit(self.background_image, (screenSize.SCREEN_WIDTH + self.counter, 0))

        if (self.counter==-screenSize.SCREEN_WIDTH):
            self.background_image.blit(self.background_image,(screenSize.SCREEN_WIDTH+self.counter,0))
            self.counter=0
    
        self.counter-=1

    
