import pygame
from entity.plant import Plant
from conf.settings import Setting

set = Setting()

class Peashooter(Plant):
    def __init__(self, screen, x, y, images):
        self.screen = screen
        self.x = x
        self.y = y
        self.images = images
        self.image = pygame.image.load(self.images[0])
        self.width = 0
        self.height = 0
        super(Peashooter, self).__init__(screen, self.x, self.y, self.image)
        # step要用到的index
        self.index = 0

        self.life = 100
        self.sunshine = 100
        self.attack = 50
        self.interval = 50
        self.cd = 10

    def function(self):
        pass

    def step(self):
        self.index += 1
        # 执行功能
        if self.index == self.interval:
            function()
            self.index = 0
        # 更改图片
        ix = self.index / 10 % len(self.images)
        self.image = pygame.image.load(self.images[int(ix)])





