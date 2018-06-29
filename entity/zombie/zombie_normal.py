import pygame
from entity.zombie.zombieObject import ZombieObject
import random


class Zombie_normal(ZombieObject):
    def __init__(self, screen, images):
        self.screen = screen
        self.images = images
        self.image = pygame.image.load(images[0])
        self.x = 1000
        self.y = 30 + random.randint(0, 4) * 100
        self.life = 5
        self.damage = 1
        super(Zombie_normal, self).__init__(screen, self.x, self.y, self.image, self.life, self.damage)

        self.index = 0

    def outOfBounds(self):
        pass

    def step(self):
        self.x -= 0.5
        self.index += 1
        ix = self.index / len(self.images) % len(self.images)
        self.image = pygame.image.load(self.images[int(ix)])
