'''
Author:    Emma Li
Program:   Pong.py
Date:      05/04/2020
Descr:
I am using pygame (1.9.6 Version), this is a menu file (tkinter).
'''


import sys
import random
import traceback

from Ball import *
from Paddle import *


def main(player_data):
    # create window
    window_size = width, height = 800, 600
    background = (0, 0, 0)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Pong game")
    green = (0, 255, 0)
    white = (255, 255, 255)

    pygame.font.init()
    font = pygame.font.SysFont("comicsansms", 28)
    score_font = pygame.font.Font("freesansbold.ttf", 24)

    p1 = Paddle("./png/paddleRed.png", [0, 300], player_data[0], player_data[1])
    p2 = Paddle("./png/paddleBlu.png", [800 - 24, 300], player_data[2], player_data[3])
    speed = [random.choice([-2, 2]), random.choice([-3, 3])]

    ball = Ball([400, 300], speed)
    # ball = Ball([400, 300], [-2, -3])

    stop = [0, 0]
    speed_radio = 10
    clock = pygame.time.Clock()

    running = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # keyboard control
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    p1.speed = [0, -1 * speed_radio]
                if event.key == pygame.K_s:
                    p1.speed = [0, 1 * speed_radio]
                if event.key == pygame.K_UP:
                    p2.speed = [0, -1 * speed_radio]
                if event.key == pygame.K_DOWN:
                    p2.speed = [0, 1 * speed_radio]
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    p1.speed = stop
                if event.key == pygame.K_s:
                    p1.speed = stop
                if event.key == pygame.K_UP:
                    p2.speed = stop
                if event.key == pygame.K_DOWN:
                    p2.speed = stop
        # Collide checking
        edge = ball.rect.width // 2
        if pygame.sprite.collide_rect(ball, p1):
            ball.speedup()
            if ball.rect.centery < p1.rect.top + edge or ball.rect.centery > p1.rect.bottom - edge:
                ball.x_change()
                ball.y_change()
                p1.add_point()
            else:
                ball.x_change()
                p1.add_point()
        if pygame.sprite.collide_rect(ball, p2):
            ball.speedup()
            if ball.rect.centery < p2.rect.top + edge or ball.rect.centery > p2.rect.bottom - edge:
                ball.x_change()
                ball.y_change()
                p2.add_point()
            else:
                ball.x_change()
                p2.add_point()
        # game over
        if ball.rect.centerx < p1.rect.centerx:
            paused = True
            text = font.render('Winner is %s, %s player, Get %s points!' % (p2.name, p2.gender, str(p2.point)), True,
                               green)
            textRect = text.get_rect()
            textRect.center = (width // 2, height // 2)
            screen.blit(text, textRect)
            pygame.display.flip()
        if ball.rect.centerx > p2.rect.centerx:
            paused = True
            text = font.render('Winner is %s, %s player, Get %s points!' % (p1.name, p1.gender, str(p1.point)), True,
                               green)
            textRect = text.get_rect()
            textRect.center = (width // 2, height // 2)
            screen.blit(text, textRect)
            pygame.display.flip()

        if not paused:
            p1.move()
            p2.move()
            ball.move()

            screen.fill(background)
            # refresh screen
            screen.blit(ball.image, ball.rect)
            screen.blit(p1.image, p1.rect)
            screen.blit(p2.image, p2.rect)
            point_text = score_font.render('%s Score: %s' % (p1.name,str(p1.point)), True, white)
            screen.blit(point_text, (0, 0))
            point_text = score_font.render('%s Score: %s' % (p2.name,str(p2.point)), True, white)
            screen.blit(point_text, (600, 0))


            pygame.display.flip()

            clock.tick(60)

