"""
加载图片路径
"""
import pygame

# 植物贴图的路径
plantsImgDir = 'image/plants/'

class Setting(object):
    def __init__(self):
        pygame.display.init()
        self.background = pygame.image.load('image/background1.jpg')
        self.seedBank = pygame.image.load('image/SeedBank.png')
        self.sunImage = 'image/sun.png'
        # 进度条   指示标   终点标
        self.flagMeterEmpty = pygame.image.load('image/progress_bar/FlagMeterEmpty.png')
        self.flagMeterFull = pygame.image.load('image/progress_bar/FlagMeterFull.png')
        self.flagMeterParts1 = pygame.image.load('image/progress_bar/FlagMeterParts1.png')
        self.flagMeterParts2 = pygame.image.load('image/progress_bar/FlagMeterParts2.png')
        # 提示标语
        self.prepareGrowPlants = pygame.image.load('image/prompt_words/PrepareGrowPlants.png')
        self.finalWave = pygame.image.load('image/prompt_words/FinalWave.gif')
        # 普通僵尸
        self.zombie_normalImages = [
            "image/zombie_normal/0.png",
            "image/zombie_normal/1.png",
            "image/zombie_normal/2.png",
            "image/zombie_normal/3.png",
            "image/zombie_normal/4.png",
            "image/zombie_normal/5.png",
            "image/zombie_normal/6.png",
            "image/zombie_normal/7.png",
            "image/zombie_normal/8.png",
            "image/zombie_normal/9.png",
            "image/zombie_normal/10.png",
            "image/zombie_normal/11.png",
            "image/zombie_normal/12.png",
            "image/zombie_normal/13.png",
            "image/zombie_normal/14.png",
            "image/zombie_normal/15.png",
            "image/zombie_normal/16.png",
            "image/zombie_normal/17.png",
            "image/zombie_normal/18.png",
            "image/zombie_normal/19.png",
            "image/zombie_normal/20.png",
            "image/zombie_normal/21.png"
        ]
        # 帽子僵尸
        self.zombie_coneheadImages = [
            "image/zombie_conehead/0.png",
            "image/zombie_conehead/1.png",
            "image/zombie_conehead/2.png",
            "image/zombie_conehead/3.png",
            "image/zombie_conehead/4.png",
            "image/zombie_conehead/5.png",
            "image/zombie_conehead/6.png",
            "image/zombie_conehead/7.png",
            "image/zombie_conehead/8.png",
            "image/zombie_conehead/9.png",
            "image/zombie_conehead/10.png",
            "image/zombie_conehead/11.png",
            "image/zombie_conehead/12.png",
            "image/zombie_conehead/13.png",
            "image/zombie_conehead/14.png",
            "image/zombie_conehead/15.png",
            "image/zombie_conehead/16.png",
            "image/zombie_conehead/17.png",
            "image/zombie_conehead/18.png",
            "image/zombie_conehead/19.png",
            "image/zombie_conehead/20.png"
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
            "image/zombie_bucketAttack/9.png",
            "image/zombie_bucketAttack/10.png"
        ]

        # 僵尸死掉
        self.zombieDieImages = [
            "image/zombieDie/0.png",
            "image/zombieDie/1.png",
            "image/zombieDie/2.png",
            "image/zombieDie/3.png",
            "image/zombieDie/4.png",
            "image/zombieDie/5.png",
            "image/zombieDie/6.png",
            "image/zombieDie/7.png",
            "image/zombieDie/8.png",
            "image/zombieDie/9.png"
        ]

        # 掉头僵尸碰撞图片
        self.zombieLostHeadAttackImages = [
            "image/zombieLostHeadAttack/0.png",
            "image/zombieLostHeadAttack/1.png",
            "image/zombieLostHeadAttack/2.png",
            "image/zombieLostHeadAttack/3.png",
            "image/zombieLostHeadAttack/4.png",
            "image/zombieLostHeadAttack/5.png",
            "image/zombieLostHeadAttack/6.png",
            "image/zombieLostHeadAttack/7.png",
            "image/zombieLostHeadAttack/8.png",
            "image/zombieLostHeadAttack/9.png",
            "image/zombieLostHeadAttack/10.png"
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

        self.cardNutWallDark = pygame.image.load('image/card/nutdark.png')
        self.cardPeashooterDark = pygame.image.load('image/card/peashooterdark.png')
        self.cherryDark = pygame.image.load('image/card/cherrydark.png')
        self.chomperDark = pygame.image.load('image/card/chomperdark.png')
        self.sunflowerDark = pygame.image.load('image/card/sunflowerdark.png')
        self.cardPeashooterdoubleDark = pygame.image.load('image/card/peashooterdoubledark.png')

        # 卡片图片缩放
        self.cardNutWall = pygame.transform.scale(self.cardNutWall, (55,68))
        self.cardPeashooter = pygame.transform.scale(self.cardPeashooter, (55, 68))
        self.cherry = pygame.transform.scale(self.cherry, (55, 68))
        self.chomper = pygame.transform.scale(self.chomper, (55, 68))
        self.sunflower = pygame.transform.scale(self.sunflower, (55, 68))
        self.cardPeashooterdouble = pygame.transform.scale(self.cardPeashooterdouble, (55, 68))
        self.cardShovelBack = pygame.transform.scale(self.cardShovelBack, (70,86))
        self.cardShovel = pygame.transform.scale(self.cardShovel, (55,55))

        self.cardNutWallDark = pygame.transform.scale(self.cardNutWallDark, (55, 68))
        self.cardPeashooterDark = pygame.transform.scale(self.cardPeashooterDark, (55, 68))
        self.cherryDark = pygame.transform.scale(self.cherryDark, (55, 68))
        self.chomperDark = pygame.transform.scale(self.chomperDark, (55, 68))
        self.sunflowerDark = pygame.transform.scale(self.sunflowerDark, (55, 68))
        self.cardPeashooterdoubleDark = pygame.transform.scale(self.cardPeashooterdoubleDark, (55, 68))

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

        # 子弹贴图
        bulletImg = 'image/bullet_01.png'

        # 关于草地格子的坐标
        # 格子X坐标
        self.gridXIndexes = [260, 340, 418, 500, 580, 662, 740, 820, 910, 996]
        # 格子高度：
        self.gridHeight = 95
        # 下边界
        self.bottomY = 574
        # 左边界：
        self.leftX = self.gridXIndexes[0]
        # 上边界：
        self.topY = self.bottomY - 5 * self.gridHeight
        # 右边界：
        self.rightX = 996
