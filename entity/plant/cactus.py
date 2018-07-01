from entity.plant.plant import Plant
from conf.settings import Setting
from entity.bullet import Bullet
from util.bus import Bus
set = Setting()

class Cactus(Plant):
    def __init__(self, screen, x, y, images):
        self.screen = screen
        self.x = x
        self.y = y
        self.images = images
        self.image = images[0]
        self.width = 0
        self.height = 0
        super(Cactus, self).__init__(screen, self.x, self.y, self.image)

        # step要用到的index
        self.index = 0

        self.life = 200
        self.sunshine = 125
        self.attack = 10
        self.interval = 500
        self.cd = 10

    def step(self, bus, screen, sets):
        self.index += 1
        # 执行功能
        if self.index == self.interval:
            bus.bullets.append(self.shootBy(screen, sets.cactusBulletImg))
            self.index = 0
        # 更改图片
        ix = self.index / 7 % len(self.images)
        self.image = self.images[int(ix)]

        # 子弹生成
    def shootBy(self, screen, image):
        bs = Bullet(screen, image, self.x + 65, self.y + 23, 1)
        return bs