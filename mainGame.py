import pygame, sys, random
from conf.settings import Setting
from entity.zombie.zombie_bucket import Zombie_bucket
from entity.zombie.zombie_conehead import Zombie_conehead
from entity.zombie.zombie_normal import Zombie_normal
from util.constant import Constant
from util.bus import Bus
import mouseListener
import painter

bus = Bus()
sets = Setting()

screen = pygame.display.set_mode((1400, 600), 0, 0)

# 僵尸存储列表
zombies = []
# 僵尸频率值
zombieIndex = 0

'''
paint部分
'''
# 场景绘制主函数
def paint():
    painter.initScenario(bus, screen, sets)
    paintZombies()
    painter.cardMovePaint(bus, screen, sets)


# 绘制僵尸
def paintZombies():
    for zombie in zombies:
        zombie.blitme()


'''
action部分
'''
# 业务逻辑主函数
def action():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseListener.cardMouseClickListener(bus)
    stepAction()
    zombiesAction()


# 走一步
def stepAction():
    # 僵尸走一步
    for zombie in zombies:
        zombie.step()

# 僵尸生成
def zombiesAction():
    global zombieIndex
    zombieIndex += 1

    if zombieIndex % 1000 == 0:
        type = random.randint(0, 20)
        if type < 8:
            zombies.append(Zombie_conehead(screen, sets.zombie_coneheadImages))
        else:
            # 1.存储到列表中
            zombies.append(Zombie_normal(screen, sets.zombie_normalImages))


'''
程序入口
'''


def main():
    pygame.display.set_caption("植物大战僵尸")

    while True:
        action()
        paint()
        pygame.display.update()


if __name__ == '__main__':
    main()
