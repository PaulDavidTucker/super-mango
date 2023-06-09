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

    def __init__(self, image, start_X, start_Y, X_size, Y_size):
        super().__init__(image, start_X, start_Y)
        
        self.X_size = X_size
        self.Y_size = Y_size
        
        self.image = pygame.transform.scale(self.image, (self.X_size, self.Y_size))

        self.stand_image = self.image

        self.jump_cycle = [pygame.image.load(f"./assets/SplitPNGs/Files/jump_{i:0>2}.png") for i in range (1,2)]
        self.walk_cycle = [pygame.image.load(f"./assets/SplitPNGs/Files/walk_{i:0>2}.png") for i in range(1,4)]
        
        self.animation_index = 0
        self.facing_left = False
        self.jump_animation_counter = 0

        #Movememt vals. 
        self.speed = 5
        self.jump_speed = 20
        self.gravity = 1
        self.vert_speed = 0
        
        

    def update(self, boxes):
        #Values to create gravity.
        horiz_speed = 0

        #Collision logic
        onground = pygame.sprite.spritecollideany(self, boxes)
        if onground != None:
            onground = True
        else:
            onground = False
    
        print(onground)
        #alter self gravity values when in the air. 
        if self.vert_speed < 10 and not onground:
            print("gravity")
            self.jump_animation()
            self.vert_speed += self.gravity

        #If we have vertical speed and are touching, stop moving
        if self.vert_speed > 0 and onground:
            print("stop")
            self.vert_speed = 0
        
        #get the queue of keys pressed.
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.facing_left = True
            self.walk_animation()
            self.move(-self.speed,0)
        elif key[pygame.K_RIGHT]:
            self.facing_left = False
            self.walk_animation()
            self.move(self.speed,0)
        else:
            self.image = self.stand_image

        #jump logic.
        if key[pygame.K_UP] and onground:
            self.vert_speed = -self.jump_speed


        #Updating the value with call to move
        self.move(horiz_speed, self.vert_speed)
            
    def walk_animation(self):
        self.image = self.walk_cycle[self.animation_index]
        self.image = pygame.transform.scale(self.image, (self.X_size, self.Y_size))
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

        if self.animation_index < len(self.walk_cycle)-1:
            self.animation_index += 1
        else:
            self.animation_index = 0

    def jump_animation(self):
    
        self.image = self.jump_cycle[self.jump_animation_counter]
        self.image = pygame.transform.scale(self.image, (self.X_size, self.Y_size))

        #Flip img if facing left
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)

        if self.animation_index < len(self.jump_cycle)-1:
            self.jump_animation_counter += 1
        else:
            self.jump_animation_counter = 0
    
    def move(self, X, Y):
        self.rect.move_ip([X, Y])

    

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
    
        self.counter-=2

    
