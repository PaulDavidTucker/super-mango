import pygame

#A file written for this project, stored in local directory I think.
import sys
pygame.init()

screen = pygame.display.set_mode((1000,800))
# Load the sprite image
sprite_image = pygame.image.load("./assets/Bird_1.png")

# Create the sprite
sprite = pygame.sprite.Sprite()
sprite.image = sprite_image
sprite.rect = sprite.image.get_rect()
sprite.rect.center = screen.get_rect().center

def startmenu()
    logo = pygame.image.load("C:\Users\adamt\OneDrive\Documents\programming\super-mango\assets\Logo.png")
    screen.blit(logo, (500,500))


startmenu()
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
