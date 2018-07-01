from entity.plant.plant import Plant
from conf.settings import Setting
from entity.bullet import Bullet
import threading

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
        self.interval = 150
        self.cd = 10


    def step(self, bus, screen, sets):
        self.index += 1
        # 执行功能
        if self.index == self.interval:
            bus.bullets.append(self.shootBy(screen, sets.peaBulletImg))
            timer = threading.Timer(0.3, self.shoot, (bus, screen, sets))
            timer.start()
            self.index = 0
        # 更改图片
        ix = self.index / 7 % len(self.images)
        self.image = self.images[int(ix)]


    def shootBy(self, screen, image):
        bs = Bullet(screen, image, self.x + 65, self.y + 2, 0)
        return bs

    def shoot(self, bus, screen, sets):
        bus.bullets.append(self.shootBy(screen, sets.peaBulletImg))
        print("timer start")