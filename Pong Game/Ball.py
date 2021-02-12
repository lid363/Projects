'''
Author:    Emma Li
Program:   Ball.py
Date:      05/04/2020
Descr:
I am using pygame (1.9.6 Version), this is Ball Class, contain all ball attributes.
move range, speed, border etc.
'''


import pygame
import math


class Ball(pygame.sprite.Sprite):
    def __init__(self, position, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./png/ballBlue.png").convert_alpha()
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        self.window = screen.get_rect()
        self.speed = speed
        self.rect.left = position[0] - self.rect.centerx
        self.rect.top = position[1] - self.rect.centery

    def move(self):
        self.rect = self.rect.move(self.speed)
        # border
        border = 3
        if self.rect.top < 0:
            self.y_change()
        if self.rect.bottom > self.window.bottom - border:
            self.y_change()
        # if self.rect.left < self.window.left + border:
        #     self.x_change()
        # if self.rect.right > self.window.right - border:
        #     self.x_change()

    def x_change(self):
        self.speed = self.speed[0] * (-1), self.speed[1]

    def y_change(self):
        self.speed = self.speed[0], self.speed[1] * (-1)

    def collide_check(self, items):
        for i in items:
            distance = math.sqrt(
                math.pow((self.rect.center[0] - i.rect.center[0]), 2) +
                math.pow((self.rect.center[1] - i.rect.center[1]), 2)
            )
            if distance <= (self.rect.width + i.rect.width) / 2:
                self.x_change()
                # self.y_change()

    def speedup(self):
        speedradio = 1.3
        self.speed = self.speed[0] * speedradio, self.speed[1] * speedradio
