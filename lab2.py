import pygame

pygame.init()

pygame.display.set_caption("Lab 2")

WIDTH = 800
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.update()

# walls
wcolor = pygame.Color("green")
borderwidth = 10
# upper wall
# Rect((left, top), (width, height))
pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (WIDTH, borderwidth)))
# left wall
pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (borderwidth, HEIGHT)))
# bottom wall
pygame.draw.rect(screen, wcolor, pygame.Rect(
    (0, HEIGHT-borderwidth), (WIDTH, borderwidth)))

pygame.display.update()

running = True
#  main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
