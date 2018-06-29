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
        self.sunImage = 'image/sun.png'
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

        # 植物贴图文件夹路径
        self.plantsInitImages = [
            plantsImgDir + 'WallNut/',
            plantsImgDir + 'SunFlower/',
            plantsImgDir + 'Peashooter/',
            plantsImgDir + 'Chomper/',
            plantsImgDir + 'CherryBomb/',
            plantsImgDir + 'Repeater/'
        ]
        self.peashooterImg = plantsImgDir + 'Peashooter/'
        self.cherryBombImg = plantsImgDir + 'CherryBomb/'
        self.cherryBombBoomImg = plantsImgDir + 'CherryBombBoom/'
        self.chomperImg = plantsImgDir + 'Chomper/'
        self.chomperAttackImg = plantsImgDir + 'ChomperAttack/'
        self.chomperDigestImg = plantsImgDir + 'ChomperDigest/'
        self.sunFlowerImg = plantsImgDir + 'SunFlower/'
        self.wallNutImg = plantsImgDir + 'WallNut/'
        self.wallNutCrackedImg = plantsImgDir + 'WallNutCracked/'
        self.wallNutBadlyCrackedImg = plantsImgDir + 'WallNutBadlyCracked/'
        self.repeaterImg = plantsImgDir + 'Repeater/'

        # 加载卡片路径
        self.cardNutWall = pygame.image.load('image/card/nutWall.png')
        self.cardPeashooter = pygame.image.load('image/card/peashooter.png')
        self.cherry = pygame.image.load('image/card/cherry.png')
        self.chomper = pygame.image.load('image/card/chomper.png')
        self.sunflower = pygame.image.load('image/card/sunflower.png')
        self.cardPeashooterdouble = pygame.image.load('image/card/peashooterdouble.png')

        # 卡片图片缩放
        self.cardNutWall = pygame.transform.scale(self.cardNutWall, (55,68))
        self.cardPeashooter = pygame.transform.scale(self.cardPeashooter, (55, 68))
        self.cherry = pygame.transform.scale(self.cherry, (55, 68))
        self.chomper = pygame.transform.scale(self.chomper, (55, 68))
        self.sunflower = pygame.transform.scale(self.sunflower, (55, 68))
        self.cardPeashooterdouble = pygame.transform.scale(self.cardPeashooterdouble, (55, 68))

        # 卡片点击图片集合
        self.cardImgs = [
            pygame.image.load('image/mouseMoveCard/mouseNut.gif'),
            pygame.image.load('image/mouseMoveCard/mouseSunflower.gif'),
            pygame.image.load('image/mouseMoveCard/mousepeashooter.gif'),
            pygame.image.load('image/mouseMoveCard/mouseChomper.gif'),
            pygame.image.load('image/mouseMoveCard/mouseCherry.gif'),
            pygame.image.load('image/mouseMoveCard/repeater.gif')
        ]
