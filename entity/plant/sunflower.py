'''
author: debug2333
description: sunflower
'''
import pygame
from conf.settings import Setting
from entity.plant.plant import Plant
from entity.sun import Sun
from util.bus import Bus

# 图片路径的全局变量
sets = Setting()

class Sunflower(Plant):
    def __init__(self, screen, x, y, images):
        self.screen = screen
        self.x = x
        self.y = y
        self.images = images
        self.image = images[0]

        super(Sunflower, self).__init__(screen, self.x, self.y, self.image)

        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]
        self.index = 0
        self.life = 50
        self.sunshine = 50
        self.attack = 0
        # 产生阳光的间隔 单位次数
        self.interval = 50
        # 再次栽种的间隔 单位s
        self.cd = 5

    # 向日葵的功能：在自己的右上方生成阳光
    def function(self):
        sun = Sun(self.screen, sets.sunImage, self.x + self.width/2, self.y + self.height/2, 0)

        Bus.sunStay.append(sun)

    def step(self):
        self.index += 1
        # 执行功能
        if self.index % 600 == 0:
             self.function()
        #     self.index = 0
        # 更改图片
        ix = self.index / 10 % len(self.images)
        self.image = self.images[int(ix)]




