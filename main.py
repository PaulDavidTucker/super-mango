import pygame

#A file written for this project, stored in local directory I think.
import sys
sys.path.insert(1, r'C:/Users/adamt/OneDrive/Documents/programming/super-mango/modules') 

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

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the sprite and update the display
    screen.fill((255, 255, 255))
    screen.blit(sprite.image, sprite.rect)
    pygame.display.update()

# Clean up
pygame.quit()
