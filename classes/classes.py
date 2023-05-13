import pygame
import screenSize

class Menu:
    #Menu class used to create a menu object Make this custom paul please
    
    def __init__(self, background, buttons):
        self.Background0 = background
        self.Background1 = background
        self.Background2 = background
        self.Buttons = buttons
    
    def Draw(self, screen):
        self.Background.Move(screen)
        


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

    
class Level:

    #Level will have a background object parsed to it to allow us to work on both seperately

    def __init__(self, background):
        self.TileMap = []
        self.Background = background