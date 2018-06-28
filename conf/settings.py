"""
加载图片路径
"""
import pygame


class Setting(object):
    def __init__(self):
        self.background = pygame.image.load('image/background1.jpg')
        self.seedBank = pygame.image.load('image/SeedBank.png')
        # 普通僵尸
        self.zombie_normalImages = [
            "image/zombie_normal/z_00_01.png",
            "image/zombie_normal/z_00_02.png",
            "image/zombie_normal/z_00_03.png",
            "image/zombie_normal/z_00_04.png",
            "image/zombie_normal/z_00_05.png",
            "image/zombie_normal/z_00_06.png",
            "image/zombie_normal/z_00_07.png"
        ]
        # 帽子僵尸
        self.zombie_coneheadImages = [
            "image/zombie_conehead/z_01_01.png",
            "image/zombie_conehead/z_01_02.png",
            "image/zombie_conehead/z_01_03.png",
            "image/zombie_conehead/z_01_04.png",
            "image/zombie_conehead/z_01_05.png",
            "image/zombie_conehead/z_01_06.png",
            "image/zombie_conehead/z_01_07.png",
            "image/zombie_conehead/z_01_08.png"
        ]
        # 铁桶僵尸
        self.zombie_bucketImages = [
            "image/zombie_bucket/z_02_01.png",
            "image/zombie_bucket/z_02_02.png",
            "image/zombie_bucket/z_02_03.png",
            "image/zombie_bucket/z_02_04.png",
            "image/zombie_bucket/z_02_05.png",
            "image/zombie_bucket/z_02_06.png",
            "image/zombie_bucket/z_02_07.png",
            "image/zombie_bucket/z_02_08.png"
        ]