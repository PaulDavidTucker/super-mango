import pygame

pygame.init()

# Create the window
screen = pygame.display.set_mode((640, 480))

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
