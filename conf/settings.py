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
        # 掉头僵尸
        self.zombieLostHeadImages = [
            "image/zombieLostHead/0.png",
            "image/zombieLostHead/1.png",
            "image/zombieLostHead/2.png",
            "image/zombieLostHead/3.png",
            "image/zombieLostHead/4.png",
            "image/zombieLostHead/5.png",
            "image/zombieLostHead/6.png",
            "image/zombieLostHead/7.png",
            "image/zombieLostHead/8.png",
            "image/zombieLostHead/9.png",
            "image/zombieLostHead/10.png",
            "image/zombieLostHead/11.png",
            "image/zombieLostHead/12.png",
            "image/zombieLostHead/13.png",
            "image/zombieLostHead/14.png",
            "image/zombieLostHead/15.png",
            "image/zombieLostHead/16.png",
            "image/zombieLostHead/17.png"
        ]
        # 掉头
        self.zombieHeadImages = [
            "image/zombieHead/0.png",
            "image/zombieHead/1.png",
            "image/zombieHead/2.png",
            "image/zombieHead/3.png",
            "image/zombieHead/4.png",
            "image/zombieHead/5.png",
            "image/zombieHead/6.png",
            "image/zombieHead/7.png",
            "image/zombieHead/8.png",
            "image/zombieHead/9.png",
            "image/zombieHead/10.png",
            "image/zombieHead/11.png"
        ]
        # 普通僵尸碰撞图片
        self.normalAttackImages = [
            "image/zombie_normalAttack/0.png",
            "image/zombie_normalAttack/1.png",
            "image/zombie_normalAttack/2.png",
            "image/zombie_normalAttack/3.png",
            "image/zombie_normalAttack/4.png",
            "image/zombie_normalAttack/5.png",
            "image/zombie_normalAttack/6.png",
            "image/zombie_normalAttack/7.png",
            "image/zombie_normalAttack/8.png",
            "image/zombie_normalAttack/9.png",
            "image/zombie_normalAttack/10.png",
            "image/zombie_normalAttack/11.png",
            "image/zombie_normalAttack/12.png",
            "image/zombie_normalAttack/13.png",
            "image/zombie_normalAttack/14.png",
            "image/zombie_normalAttack/15.png",
            "image/zombie_normalAttack/16.png",
            "image/zombie_normalAttack/17.png",
            "image/zombie_normalAttack/18.png",
            "image/zombie_normalAttack/19.png",
            "image/zombie_normalAttack/20.png"

        ]

        # 帽子僵尸碰撞图片
        self.coneheadAttackImages = [
            "image/zombie_coneheadAttack/0.png",
            "image/zombie_coneheadAttack/1.png",
            "image/zombie_coneheadAttack/2.png",
            "image/zombie_coneheadAttack/3.png",
            "image/zombie_coneheadAttack/4.png",
            "image/zombie_coneheadAttack/5.png",
            "image/zombie_coneheadAttack/6.png",
            "image/zombie_coneheadAttack/7.png",
            "image/zombie_coneheadAttack/8.png",
            "image/zombie_coneheadAttack/9.png",
            "image/zombie_coneheadAttack/10.png"

        ]
        # 铁桶僵尸碰撞图片
        self.bucketAttackImages = [
            "image/zombie_bucketAttack/0.png",
            "image/zombie_bucketAttack/1.png",
            "image/zombie_bucketAttack/2.png",
            "image/zombie_bucketAttack/3.png",
            "image/zombie_bucketAttack/4.png",
            "image/zombie_bucketAttack/5.png",
            "image/zombie_bucketAttack/6.png",
            "image/zombie_bucketAttack/7.png",
            "image/zombie_bucketAttack/8.png",
            "image/zombie_bucketAttack/8.png",
            "image/zombie_bucketAttack/10.png",
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
        self.cardShovelBack = pygame.image.load('image/card/ShovelBack.png')
        self.cardShovel = pygame.image.load('image/card/Shovel.png')

        # 卡片图片缩放
        self.cardNutWall = pygame.transform.scale(self.cardNutWall, (55,68))
        self.cardPeashooter = pygame.transform.scale(self.cardPeashooter, (55, 68))
        self.cherry = pygame.transform.scale(self.cherry, (55, 68))
        self.chomper = pygame.transform.scale(self.chomper, (55, 68))
        self.sunflower = pygame.transform.scale(self.sunflower, (55, 68))
        self.cardPeashooterdouble = pygame.transform.scale(self.cardPeashooterdouble, (55, 68))
        self.cardShovelBack = pygame.transform.scale(self.cardShovelBack, (70,86))
        self.cardShovel = pygame.transform.scale(self.cardShovel, (55,55))

        #图片旋转
        self.cardShovel = pygame.transform.rotate(self.cardShovel, 45)

        # 卡片点击图片集合
        self.cardImgs = [
            pygame.image.load('image/mouseMoveCard/mouseNut.gif'),
            pygame.image.load('image/mouseMoveCard/mouseSunflower.gif'),
            pygame.image.load('image/mouseMoveCard/mousepeashooter.gif'),
            pygame.image.load('image/mouseMoveCard/mouseChomper.gif'),
            pygame.image.load('image/mouseMoveCard/mouseCherry.gif'),
            pygame.image.load('image/mouseMoveCard/repeater.gif'),
            self.cardShovel
        ]
