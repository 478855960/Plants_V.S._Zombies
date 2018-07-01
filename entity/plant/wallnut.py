from entity.plant.plant import Plant
from conf.settings import Setting
from util.loadimages import getImages
set = Setting()

class Wallnut(Plant):
    def __init__(self, screen, x, y, images):
        self.screen = screen
        self.x = x
        self.y = y
        self.images = images
        self.image = images[0]
        self.width = 0
        self.height = 0
        super(Wallnut,self).__init__(screen, self.x, self.y, self.image)

        # step要用到的index
        self.index = 0

        self.life = 200
        self.sunshine = 50
        self.attack = 0
        self.interval = 50
        self.cd = 10

    def function(self):
        pass

    def step(self, bus, screen, sets):
        self.index += 1
        # 执行功能
        if self.index == self.interval:
            self.function()
            self.index = 0
        # 更改图片
        if self.life == 150:
            self.images = getImages('image/plants/WallNutCracked/')
        if self.life == 50:
            self.images = getImages('image/plants/WallNutBadlyCracked/')
        ix = self.index / 7 % len(self.images)
        self.image = self.images[int(ix)]