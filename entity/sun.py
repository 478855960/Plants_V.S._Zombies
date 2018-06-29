"""
太阳类
"""
import pygame

class Sun(object):
    def __init__(self, screen, image, x, y, goal):
        self.screen = screen
        # 加载太阳图片
        self.image = pygame.image.load(image)
        self.goal = goal
        self.x = x
        self.y = y
        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]

        # 控制太阳停止的位置
        self.index = 0

        # 一个太阳的分数
        self.score = 25

        # 太阳掉到地上后的消失时间
        self.disappearTime = 0



    def blitme(self):
        self.screen.blit(self.image, (self.x, self.y))


    def step(self):
        self.y += 1
        self.index += 1
