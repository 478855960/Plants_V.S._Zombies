import pygame

class Bullet(object):
    def __init__(self, screen, image, peaX, peaY):
        self.screen = screen
        self.image = pygame.image.load(image)
        # x,y
        self.x = peaX
        self.y = peaY

    def outOfBounds(self):
        return self.x > 1400

    def step(self):
        self.x += 3
