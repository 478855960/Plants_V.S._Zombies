import pygame, sys, random
from conf.settings import Setting
from entity.zombie.zombie_bucket import Zombie_bucket
from entity.zombie.zombie_conehead import Zombie_conehead
from entity.zombie.zombie_normal import Zombie_normal
from util.constant import Constant
from musicplayer import MusicPlayer
from entity.sun import Sun
from util.bus import Bus
import mouseListener
import painter
import actioner

bus = Bus()
sets = Setting()

screen = pygame.display.set_mode((1400, 600), 0, 0)
sets = Setting()
bus.music = MusicPlayer()

bus.music.play()



def initSun():
    for i in range(4):
        xx = random.randint(260, 880)
        yy = -random.randint(100, 300)
        goal = random.randint(300, 600)
        sun = Sun(screen, sets.sunImage, xx, yy,goal)
        bus.sunFall.append(sun)

# 初始场景绘制
def initScenario():
    screen.blit(sets.background, (0, 0))
    screen.blit(sets.seedBank, (0, 0))

'''
paint部分
'''

# 场景绘制主函数
def paint():
    painter.initScenario(bus, screen, sets)
    paintZombies()
    painter.cardMovePaint(bus, screen, sets)
    paintPlants()

    # 绘制下落及在地上的太阳
    painter.paintSun(bus, screen, sets)


    # 绘制太阳总分数状态
    painter.paintSunScore(bus, screen, sets)

    # 绘制进度条
    painter.painProgressBar(bus, screen, sets)



# 绘制僵尸
def paintZombies():
    for zombie in bus.zombies:
        zombie.blitme()
# 绘制植物
def paintPlants():
    for plant in bus.paintPlants:
        plant.step()
        plant.blitme()

'''
action部分
'''


# 业务逻辑主函数
def action():

    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseListener.initPlantsMouseClickListener(bus, screen)
            mouseListener.cardMouseClickListener(bus)
            mouseListener.sunMouseClickListener(bus, screen, sets)
    stepAction()
    zombiesAction()

    hitAction()
    # 阳光的动作
    actioner.sunAction(bus, screen, sets)

    # 控制全局的时间轴时间增加
    bus.globalTime += 1


# 走一步
def stepAction():
    # 僵尸走一步
    for zombie in bus.zombies:
        zombie.step()


# 僵尸生成
def zombiesAction():
    bus.zombieIndex += 1

    if bus.zombieIndex % 1000 == 0:
        type = random.randint(0, 20)
        if type < 8:
            bus.zombies.append(Zombie_conehead(screen, sets.zombie_coneheadImages))
        else:
            # 1.存储到列表中
            bus.zombies.append(Zombie_normal(screen, sets.zombie_normalImages))


# 碰撞测试
def hitAction():
    for zombie in bus.zombies:
        if not isinstance(zombie, Zombie_normal):
            if zombie.life == 5:
                zombie.images = sets.zombie_normalImages
        if zombie.life == 3 and bus.headFlag is True:
            zombie.images = sets.zombieLostHeadImages
            screen.blit(sets.zombieHeadImages, (zombie.x, zombie.y))
            bus.headFlag = False
        elif zombie.life == 0:
            bus.zombies(zombie)
            screen.blit(sets.zombieDieImages, (zombie.x, zombie.y))

        hit(zombie)


def hit(zb):
    if zb.x == 500:
        if zb.life <= 3:
            zb.images = sets.zombieLostHeadAttackImages
        else:
            if isinstance(zb, Zombie_normal):
                zb.images = sets.normalAttackImages
            elif isinstance(zb, Zombie_conehead):
                zb.images = sets.coneheadAttackImages
'''
程序入口
'''


def main():
    pygame.display.set_caption("植物大战僵尸")
    initSun()
    while True:
        action()
        paint()
        pygame.display.update()


if __name__ == '__main__':
    main()
