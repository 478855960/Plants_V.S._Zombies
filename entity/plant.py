'''
author: debug2333
description: all specific plants's superclass
'''
import pygame, abc
class Plant(object):
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.img = ''
        self.width = 0
        self.height = 0

        # 生命值、阳光消耗、攻击力、射击间隔、冷却时间
        self.life = 0
        self.sunshine = 0
        self.attack = 0
        self.interval = 0
        self.cd = 0

    # 植物的功能：如向日葵即生产阳光、豌豆射手即攻击
    @abc.abstractmethod
    def function(self):
        pass

    # 在屏幕上绘制
    @abc.abstractmethod
    def blitme(self):
        pass

    # 进行一次功能执行
    @abc.abstractmethod
    def step(self):
        pass
