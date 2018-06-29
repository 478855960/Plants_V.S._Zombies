'''
author: debug2333
description: sunflower
'''
import pygame
from conf.settings import Setting
from entity.plant import Plant

# 图片路径的全局变量
sets = Setting()

class Sunflower(Plant):
    def __init__(self, screen, x, y, images):
        self.screen = screen
        self.x = x
        self.y = y
        self.images = images
        self.img = images[0]
        self.width = self.img.get_rect()[2]
        self.height = self.img.get_rect()[3]
        self.index = 0

        self.life = 50
        self.sunshine = 50
        self.attack = 0
        # 产生阳光的间隔 单位s
        self.interval = 3
        # 再次栽种的间隔 单位s
        self.cd = 5
        super(Sunflower, self).__init__(screen, self.x, self.y, self.img)

    # 向日葵的功能：在自己的右上方生成阳光
    def function(self, img):
        self.screen.blit(self.img, (self.x + self.width/2, self.y + self.height/2))

    def step(self):
        pass




