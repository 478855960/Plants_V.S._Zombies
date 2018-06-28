"""
加载图片路径
"""
import pygame

# 植物贴图的路径
plantsImgDir = 'image/plants/'

class Setting(object):
    def __init__(self):
        self.background = pygame.image.load('image/background1.jpg')
        self.seedBank = pygame.image.load('image/SeedBank.png')
        self.peashooterImg = pygame.image.load(plantsImgDir + 'Peashooter/Peashooter.gif')
        self.cherryBombImg = pygame.image.load(plantsImgDir + 'CherryBomb/CherryBomb.gif')
        self.cherryBombBoomImg = pygame.image.load(plantsImgDir + 'CherryBomb/Boom.gif')
        self.chomperImg = pygame.image.load(plantsImgDir + 'Chomper/Chomper.gif')
        self.chomperAttackImg = pygame.image.load(plantsImgDir + 'Chomper/ChomperAttack.gif')
        self.chomperDigestImg = pygame.image.load(plantsImgDir + 'Chomper/ChomperDigest.gif')
        self.sunFlowerImg = pygame.image.load(plantsImgDir + 'SunFlower/SunFlower.gif')
        self.wallNutImg = pygame.image.load(plantsImgDir + 'WallNut/WallNut.gif')
        self.wallNutCrackeImg = pygame.image.load(plantsImgDir + 'WallNut/Wallnut_cracked1.gif')
        self.wallNutBadlyCrackeImg = pygame.image.load(plantsImgDir + 'WallNut/Wallnut_cracked2.gif')
        self.repeaterImg = pygame.image.load(plantsImgDir + 'Repeater/Repeater.gif')
