#imports
import pygame
import os
import sys

'''
This project makes use of a logger to track events and errors. 
Use logger.log.info("message") to log an event.
Use logger.log.error("message") to log an error.
Use logger.log.warning("message") to log a warning.
'''


#A file written for this project, stored in local directory I think.
#If you want to use a module from a different directory, you need to add it to the path. Support modules are in the modules folder.
currentDirectory = os.getcwd()
sys.path.insert(0, currentDirectory+'/modules') 

#local imports from modules folder
import screenSize
import log as logger
from classes.classes import *

#variables for height and width for simplification
height = int(screenSize.SCREEN_HEIGHT)
width = int(screenSize.SCREEN_WIDTH)
MidpointWidth = (screenSize.SCREEN_WIDTH / 2)
MidpointHeight = (screenSize.SCREEN_HEIGHT / 8)

# Essential game objects. 
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#Log info
logger.log.info(f"Screen Size set at: {screenSize.SCREEN_WIDTH} by {screenSize.SCREEN_HEIGHT}")

# Load the sprite image
sprite_image = pygame.image.load("./assets/SplitPNGs/Files/dash_01.png")

# Create the spritegit 
sprite = pygame.sprite.Sprite()
sprite.image = sprite_image
sprite.rect = sprite.image.get_rect()
sprite.rect.center = screen.get_rect().center



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


# initialise game objects

player = Player("/SplitPNGs/Files/dash_01.png", 200, 400)

boxes = pygame.sprite.Group()

#Loop to create boxes
for bx in range(24, screenSize.SCREEN_WIDTH, 48):
    boxes.add(Box("Grass_Tileset.png", bx, screenSize.SCREEN_HEIGHT - 60))

#tracking vars
running = True

#create background object
background = Background("Sky_Background_0.png", 1)


# Game loop
while running:
    pygame.event.pump()
    player.update()
    boxes.update()

    # Draw the background
    background.Move(screen)

    # Draw the sprite
    player.draw(screen)
    boxes.draw(screen)

    # Flip the display
    pygame.display.flip()
    clock.tick(60)


    # Handle events such as exiting the game or moving the sprite
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Clean up
pygame.quit()

