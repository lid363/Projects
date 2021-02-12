'''
Author:    Emma Li
Program:   Paddle.py
Date:      05/04/2020
Descr:
I am using pygame (1.9.6 Version), this is the file contain paddle movement
 and player information.
'''
import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, image, position, name, gender):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.window = screen.get_rect()
        self.speed = [0, 0]
        self.rect.left = position[0]
        self.rect.top = position[1] - self.rect.centery
        self.point = 0
        self.name = name
        if gender == 1:
            self.gender = "Female"
        else:
            self.gender = "Male"

    def move(self):
        self.rect = self.rect.move(self.speed)
        # border
        if self.rect.top < 0:
            self.speed = [0, 0]
            self.rect.top = 0
        if self.rect.bottom > self.window.bottom:
            self.speed = [0, 0]
            self.rect.bottom = self.window.bottom

    def add_point(self):
        self.point += 1
