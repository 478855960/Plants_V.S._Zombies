"""
僵尸父类
1.图片image
2.x,y,width,height
3.damage life 伤害 生命
4.限定活动区域 重写该方法
5.step 走一步 重写该方法
6.blitme 绘图方法
7.hit 碰撞方法
"""
import abc


class ZombieObject(object):
    def __init__(self, screen, x, y, image, life, damage):
        # 获取屏幕
        self.screen = screen
        # 获取坐标
        self.x = x
        self.y = y
        # 获取图片
        self.image = image
        self.width = image.get_rect()[2]
        self.height = image.get_rect()[3]
        self.life = life
        self.damage = damage

    def outOfBounds(self):
        return self.x < 100

    @abc.abstractmethod
    def step(self, sets):
        pass

    # 绘图方法
    def blitme(self):
        self.screen.blit(self.image, (self.x, self.y))

    # 子弹与僵尸碰撞
    def hitBy(self, bt):
        # 1.获取子弹的坐标值
        btX = bt.x
        btY = bt.y
        btXW = bt.x + bt.width
        btYH = bt.y + bt.height
        # 2.获取飞行物的坐标值
        fX = self.x + self.width/2
        fY = self.y
        fXW = self.x + self.width
        fYH = self.y + self.height
        # 3.返回判断值
        return fX >= btX-2 and fX <= btX+1.5 and fY < btY and fYH > btYH
