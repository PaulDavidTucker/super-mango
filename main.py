import pygame
#OS is a standard library module, so no need to install it.
import os

from classes.classes import Level, Player

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

# Create the sprite
sprite = pygame.sprite.Sprite()
sprite.image = sprite_image
sprite.rect = sprite.image.get_rect()
sprite.rect.center = screen.get_rect().center

# Create the background image
background_image = pygame.image.load("./assets/Forest_Background_0.png")
background_image = pygame.transform.scale(background_image, (screenSize.SCREEN_WIDTH, screenSize.SCREEN_HEIGHT))

# Game loop

player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 30  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10  # how fast to move

#generic enemy spawn location for now
enemy_list = Level.bad(1, [300, 0])

#tracking vars
running = True
i = 0
while running:

    #handle player movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)

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
