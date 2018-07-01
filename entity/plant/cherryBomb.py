
import pygame
from conf.settings import Setting
from entity.plant.plant import Plant
from entity.sun import Sun
from util.bus import Bus
from util.loadimages import getImages

# 图片路径的全局变量
sets = Setting()

class CherryBomb(Plant):
    def __init__(self, screen, x, y, images, bus):
        self.screen = screen
        self.x = x
        self.y = y
        self.images = images
        self.image = images[0]
        self.bus = bus

        super(CherryBomb, self).__init__(screen, self.x, self.y, self.image)

        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]
        self.index = 0
        self.life = 50
        # 所需的阳光数
        self.sunshine = 150
        self.attack = 0
        # 产生阳光的间隔 单位次数
        self.interval = 50
        # 再次栽种的间隔 单位s
        self.cd = 10
        # 是否变到最大的标志
        self.isBigest = 0


    # 樱桃炸弹的功能，爆炸，并且杀死僵尸兵，执行之后消失
    def function(self):
        # 樱桃炸弹变大
        for i in range(len(self.bus.paintPlants)):
            # 判断是否是樱桃炸弹，是的话就去掉该对象

            if isinstance(self.bus.paintPlants[i], CherryBomb):
                # 此处是遍历僵尸列表，消灭在爆炸范围之内的全部僵尸


                self.bus.gridList[self.gridX][self.gridY] = -1
                del self.bus.paintPlants[i]
                break


    # 樱桃炸弹爆炸一次之后就死亡
    def step(self, bus, screen, sets):
        self.index += 1

        # 樱桃炸弹逐渐变大 , 在更改images后变为爆炸效果
        ix = self.index / 10 % len(self.images)
        self.image = self.images[int(ix)]


        # 变到最大之后，调用樱桃炸弹的爆炸功能，并且更改images
        if self.isBigest == 0 and self.index == 70:
            self.images = getImages(sets.plantsInitImages[6])
            self.image = self.images[0]
            self.width = self.image.get_rect()[2]
            self.height = self.image.get_rect()[3]
            # 重新调整绘图位置
            self.x -= 60
            self.y -= 60
            self.index = 0
            self.isBigest = 1

        # 当炸弹范围变到最大时，对僵尸造成伤害
        if ix == 7 and self.isBigest == 1:
            # 遍历僵尸列表
            for zombie in self.bus.zombies:
                # 对 3X3 范围内的僵尸统一造成5点伤害
                # 用僵尸脚的两个点判断是否被樱桃炸弹炸到
                if zombie.y + 100 > self.y - 80 and zombie.y + 100 <self.y + self.height and  \
                    ((zombie.x > self.x and zombie.x < self.x + self.width) \
                     or (zombie.x + zombie.width > self.x and \
                         zombie.x + zombie.width < self.x + self.width)):
                    zombie.life -= 5
                    if zombie.life <= 0:
                        self.bus.zombies.remove(zombie)


        if self.isBigest == 1 and self.index == 130:
            self.function()





