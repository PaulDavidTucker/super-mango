import os
import pygame

#A file written for this project, stored in local directory I think.
#If you want to use a module from a different directory, you need to add it to the path. Support modules are in the modules folder.
import sys
currentDirectory = os.getcwd()
sys.path.insert(0, currentDirectory+'/modules') 


import screenSize




#https://opensource.com/article/18/7/put-platforms-python-game

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ALPHA = (0, 255, 0)

# Variables for framerate
fps = 40
ani = 4

class Platform(pygame.sprite.Sprite):
    def __init__(self, X_location, Y_location, img_width, img_height, img):
        #Initialise the sprite object with this object. This is a subclass of Sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = X_location
        self.rect.y = Y_location


class Player(pygame.sprite.Sprite):
    """
    Spawn a player

    FramesMax is the maximum number of frames for the animation
    """

    def __init__(self, framesMax):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.framesMax = framesMax
        self.health = 10
        self.images = []
        for i in range(1, self.framesMax):
            #path needed here to load images for player
            img = pygame.image.load(os.path.join('./assets/', img)).convert()
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]

        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in hit_list:
            self.health -= 1
            print(self.health)


class Enemy(pygame.sprite.Sprite):
    """
    Spawn an enemy
    """

    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('./assets', img))
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

    def move(self):
        """
        enemy movement
        """
        distance = 80
        speed = 8

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance * 2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1


class Level:
    def ground(lvl, gloc, tx, ty):
        ground_list = pygame.sprite.Group()
        i = 0
        if lvl == 1:
            while i < len(gloc):
                #Using screen width rather than window size may cause bugs
                ground = Platform(gloc[i], screenSize.SCREEN_HEIGHT - ty, tx, ty, 'tile-ground.png')
                ground_list.add(ground)
                i = i + 1

        if lvl == 2:
            print("Level " + str(lvl))

        return ground_list

    def bad(lvl, eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0], eloc[1], 'Spider_1.png')
            enemy_list = pygame.sprite.Group()
            enemy_list.add(enemy)
        if lvl == 2:
            print("Level " + str(lvl))

        return enemy_list

    # x location, y location, img width, img height, img file
    def platform(lvl, tx, ty):
        plat_list = pygame.sprite.Group()
        ploc = []
        i = 0
        if lvl == 1:
            ploc.append((200,  - ty - 128, 3))
            ploc.append((300, screenSize.SCREEN_HEIGHT - ty - 256, 3))
            ploc.append((500, screenSize.SCREEN_HEIGHT - ty - 128, 4))
            while i < len(ploc):
                j = 0
                while j <= ploc[i][2]:
                    plat = Platform((ploc[i][0] + (j * tx)), ploc[i][1], tx, ty, 'tile.png')
                    plat_list.add(plat)
                    j = j + 1
                print('run' + str(i) + str(ploc[i]))
                i = i + 1

        if lvl == 2:
            print("Level " + str(lvl))

        return plat_list
    

enemy_list = Level.bad(1, [300, 0])