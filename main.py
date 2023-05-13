import pygame
#OS is a standard library module, so no need to install it.
import os

currentDirectory = os.getcwd()


#A file written for this project, stored in local directory I think.
#If you want to use a module from a different directory, you need to add it to the path. Support modules are in the modules folder.
import sys
sys.path.insert(0, currentDirectory+'/modules') 

#Screensize used to determine screenSize dynamically.
import screenSize
#Log used to log messages. If attempting to debug just use a logger
import log as logger

pygame.init()

# Create the window - GameSize here
screen = pygame.display.set_mode((screenSize.SCREEN_WIDTH, screenSize.SCREEN_HEIGHT))

#Log info
logger.log.info(f"Screen Size set at: {screenSize.SCREEN_WIDTH} by {screenSize.SCREEN_HEIGHT}")

# Load the sprite image
sprite_image = pygame.image.load("./assets/Bird_1.png")

# Create the spritegit 
sprite = pygame.sprite.Sprite()
sprite.image = sprite_image
sprite.rect = sprite.image.get_rect()
sprite.rect.center = screen.get_rect().center

#variables for height and width for simplification
height = int(screenSize.SCREEN_HEIGHT)
width = int(screenSize.SCREEN_WIDTH)
MidpointWidth = (screenSize.SCREEN_WIDTH / 2)
MidpointHeight = (screenSize.SCREEN_HEIGHT / 8)

#loading new images and resizing them to be the correct fit
logo = pygame.image.load(currentDirectory + "/assets/Logo.png")
logo = pygame.transform.scale(logo,(300,200))
skybg0 = pygame.image.load(currentDirectory + "/assets/Sky_Background_0.png")
skybg0 = pygame.transform.scale(skybg0, (width, height))
skybg1 = pygame.image.load(currentDirectory + "/assets/Sky_Background_1.png")
skybg1 = pygame.transform.scale(skybg1, (width, height))
skybg2 = pygame.image.load(currentDirectory + "/assets/Sky_Background_2.png")
skybg2 = pygame.transform.scale(skybg2, (width, height))

# function for the start menu
def startmenu():
    screen.blit(skybg0,(0,0))
    screen.blit(skybg1,(0,0))
    screen.blit(skybg2,(0,0))
    screen.blit(logo,(MidpointWidth - 150 ,MidpointHeight))



# Create the background image
background_image = pygame.image.load("./assets/Forest_Background_0.png")
background_image = pygame.transform.scale(background_image, (screenSize.SCREEN_WIDTH, screenSize.SCREEN_HEIGHT))

def Level1(surface, counter):
    screen.fill((0, 0, 0))
    # Move the background
    screen.blit(surface, (counter, 0))
    screen.blit(surface, (screenSize.SCREEN_WIDTH + counter, 0))

    if (counter==-screenSize.SCREEN_WIDTH):
        screen.blit(surface,(screenSize.SCREEN_WIDTH+counter,0))
        counter=0
    
    counter-=1

    return counter

# Game loop

#tracking vars
running = True
i = 0
while running:
    startmenu()
    #i = Level1(background_image, i)
    # Draw the sprite and update the display
    
    pygame.display.update()

# Clean up
pygame.quit()
