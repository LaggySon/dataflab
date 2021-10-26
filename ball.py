import pygame


class Ball:
    # pass
    # class variables
    RADIUS = 10

    def __init__(self, x, y, vx, vy, color, bgcolor, screen, width, height, bwidth):
        # instance variables
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.bgcolor = bgcolor
        self.screen = screen
        self.width = width
        self.height = height
        self.bwidth = bwidth

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    def update(self):
        # delete the old ball
        self.show(self.bgcolor)
        self.x += self.vx
        self.y += self.vy
        self.show(self.color)
        # print(self.x, self.y, self.vx, self.vy) DEBUG CODE
        # DONE: Check if colliding
        if(self.x <= (0 + self.bwidth + self.RADIUS)):
            self.vx = -self.vx
        if(self.y <= (0 + self.bwidth + self.RADIUS) or self.y >= (self.height - self.bwidth - self.RADIUS)):
            self.vy = -self.vy
        # flip the velocity
