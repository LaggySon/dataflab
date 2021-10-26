import pygame
import random
from paddle import Paddle
from ball import Ball

pygame.init()

pygame.display.set_caption("Pong")

WIDTH = 800
HEIGHT = 480
VELOCITY = 5
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.update()

# walls
wcolor = pygame.Color("white")
bgcolor = pygame.Color("black")
borderwidth = 20
# upper wall
# Rect((left, top), (width, height))
pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (WIDTH, borderwidth)))
# left wall
pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (borderwidth, HEIGHT)))
# bottom wall
pygame.draw.rect(screen, wcolor, pygame.Rect(
    (0, HEIGHT-borderwidth), (WIDTH, borderwidth)))

# Ball Init
ballcolor = pygame.Color("green")

x0 = WIDTH - Ball.RADIUS
y0 = HEIGHT // 2
vx0 = -VELOCITY
vy0 = random.choice([VELOCITY, -VELOCITY])
# DONE: +/- 45 degrees randomly
b0 = Ball(x0, y0, vx0, vy0, ballcolor, bgcolor,
          screen, WIDTH, HEIGHT, borderwidth)
b0.show(ballcolor)

pygame.display.update()

running = True
clock = pygame.time.Clock()
#  main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False

    pygame.display.update()
    clock.tick(FPS)
    # Ball
    b0.update()

# TODO push lab3 to github
# include gif showing collisions with wall and rand start
