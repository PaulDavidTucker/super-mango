import pygame

#A file written for this project, stored in local directory I think.
#If you want to use a module from a different directory, you need to add it to the path. I NEED TO MAKE THIS DYNAMICALLY FIND THE PATH
import sys
sys.path.insert(0, '/home/paul/Documents/Projects/super-mango/modules') 

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

# Create the sprite
sprite = pygame.sprite.Sprite()
sprite.image = sprite_image
sprite.rect = sprite.image.get_rect()
sprite.rect.center = screen.get_rect().center

# Create the background image
background_image = pygame.image.load("./assets/Forest_Background_0.png")
background_image = pygame.transform.scale(background_image, (screenSize.SCREEN_WIDTH, screenSize.SCREEN_HEIGHT))

# Game loop

#tracking vars
running = True
i = 0
while running:

    screen.fill((0, 0, 0))
    # Move the background
    screen.blit(background_image, (i, 0))
    screen.blit(background_image, (screenSize.SCREEN_WIDTH + i, 0))

    if (i==-screenSize.SCREEN_WIDTH):
        screen.blit(background_image,(screenSize.SCREEN_WIDTH+i,0))
        i=0
    i-=1

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.update()

# Clean up
pygame.quit()
