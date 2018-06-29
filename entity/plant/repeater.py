from entity.plant.plant import Plant
from conf.settings import Setting

set = Setting()

class Repeater(Plant):
    def __init__(self, screen, x, y, images):
        self.screen = screen
        self.x = x
        self.y = y
        self.images = images
        self.image = images[0]
        self.width = 0
        self.height = 0
        super(Repeater,self).__init__(screen, self.x, self.y, self.image)

        # step要用到的index
        self.index = 0

        self.life = 100
        self.sunshine = 200
        self.attack = 50
        self.interval = 50
        self.cd = 10

    def function(self):
        pass

    def step(self):
        self.index += 1
        # 执行功能
        if self.index == self.interval:
            self.function()
            self.index = 0
        # 更改图片
        ix = self.index / 7 % len(self.images)
        self.image = self.images[int(ix)]