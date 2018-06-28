"""
加载图片路径
"""
import pygame


class Setting(object):
    def __init__(self):
        self.background = pygame.image.load('image/background1.jpg')
        self.seedBank = pygame.image.load('image/SeedBank.png')