"""
铁桶僵尸
"""
import pygame, random
from entity.zombie.zombieObject import ZombieObject


class Zombie_bucket(ZombieObject):
    def __init__(self, screen, images):
        self.screen = screen
        self.images = images
        self.image = pygame.image.load(self.images[0])
        # 取值范围暂定
        self.x = 1000
        self.y = 30 + random.randint(0, 4)*100
        self.life = 10
        self.damage = 1
        super(Zombie_bucket, self).__init__(screen, self.x, self.y, self.image, self.life, self.damage)
        # 图片集转换集
        self.index = 0

    def outOfBounds(self):
        return self.x < 0

    def step(self):
        # 1.更改坐标值
        self.x -= 0.5
        # 2.更改图片
        self.index += 1
        ix = self.index / 8 % len(self.images)
        # 设置图片
        self.image = pygame.image.load(self.images[int(ix)])
