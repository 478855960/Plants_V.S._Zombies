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
from entity.zombie.zombie_head import Zombie_head
from entity.zombie.zombie_dead import Zombie_dead
from entity.plant.cherryBomb import CherryBomb
import threading
import time

bus = Bus()
sets = Setting()

screen = pygame.display.set_mode((1400, 600), 0, 0)
bus.music = MusicPlayer()

bus.music.play()

def initSun():
    for i in range(1):
        xx = random.randint(260, 880)
        yy = -random.randint(100, 300)
        goal = random.randint(300, 600)
        sun = Sun(screen, sets.sunImage, xx, yy,goal)
        bus.sunFall.append(sun)

'''
paint部分
'''

# 场景绘制主函数
def paint():
    if bus.state == bus.START:
        painter.initStartSurface(bus, screen, sets)
        return

    # 判断是否需要画暂停标志
    painter.initScenario(bus, screen, sets)
    paintZombies()
    painter.cardMovePaint(bus, screen, sets)
    paintPlants()
    paintBullets()

    # 绘制下落及在地上的太阳
    painter.paintSun(bus, screen, sets)
    # 绘制太阳总分数状态
    painter.paintSunScore(bus, screen, sets)
    # 绘制进度条
    painter.painProgressBar(bus, screen, sets)
    if bus.state == bus.PAUSE:
        painter.paintPause(bus, screen, sets)
    elif bus.state == bus.DEAD:
        painter.deadPaint(bus, screen, sets)
    elif bus.state == bus.END:
        painter.wonPaint(bus, screen, sets)
        

# 绘制僵尸
def paintZombies():
    for zombie in bus.zombies:
        zombie.blitme()
        if isinstance(zombie, Zombie_head) or isinstance(zombie, Zombie_dead):
            if zombie.reloadFlag == 1:
                bus.zombies.remove(zombie)
# 绘制植物
def paintPlants():
    for plant in bus.paintPlants:
        plant.blitme()
# 绘制子弹
def paintBullets():
    for bullet in bus.bullets:
        bullet.blitme()

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
            mouseListener.runOrPause(bus, screen, sets)
    if bus.state == bus.RUNNING:
        stepAction()
        zombiesAction()
        # 阳光的动作
        actioner.sunAction(bus, screen, sets)
        # 控制全局的时间轴时间增加
        bus.globalTime += 1
        for plant in bus.paintPlants:
            plant.step(bus, screen, sets)
        hitAction()
        actioner.endAction(bus, screen, sets)

# 走一步
def stepAction():
    # 僵尸走一步
    for zombie in bus.zombies:
        zombie.step(sets)
    for bullet in bus.bullets:
        bullet.step()


# 僵尸生成
def zombiesAction():
    bus.zombieIndex += 1
    if 7000 <= bus.globalTime <= 8000 or 14200 <= bus.globalTime <= 14400:
        bus.zombieRate = 50
    else:
        bus.zombieRate = 500

    if bus.globalTime == 14300:
        bus.zombies.append(Zombie_bucket(screen, sets.zombie_bucketImages))
        bus.endFlag = 1
    if bus.globalTime < 14400:
        if bus.zombieIndex % bus.zombieRate == 0:
            type = random.randint(0, 20)
            if type < 8:
                bus.zombies.append(Zombie_conehead(screen, sets.zombie_coneheadImages))
            else:
                # 1.存储到列表中
                bus.zombies.append(Zombie_normal(screen, sets.zombie_normalImages))


# 碰撞测试
def hitAction():
    for zombie in bus.zombies:
        eat(zombie)
        hit(zombie)
        if zombie.life == 5:
            if not isinstance(zombie, Zombie_normal):
                zombie.images = sets.zombie_normalImages
        elif zombie.life == 3:
            if zombie.headFlag is True:
                zombie.images = sets.zombieLostHeadImages
                zombie.headFlag = False
        elif zombie.life == 0:
            bus.zombies.remove(zombie)

# 僵尸吃植物
def eat(zb):
    for plant in bus.paintPlants:
        if not isinstance(plant, CherryBomb) and not isinstance(zb, Zombie_head) and not isinstance(zb, Zombie_dead):
            if plant.x + plant.width/2 == zb.x + 20 and zb.y + 100 < plant.y + 100 and zb.y + 100 > plant.y:
                if zb.life <= 3:
                    zb.images = sets.zombieLostHeadAttackImages
                elif zb.life <= 5:
                    zb.images = sets.normalAttackImages
                elif zb.life <= 8:
                    if not isinstance(zb, Zombie_bucket):
                        zb.images = sets.coneheadAttackImages
                    else:
                        zb.images = sets.bucketAttackImages
                else:
                    zb.images = sets.bucketAttackImages
                plant.life -= 0.5
                if plant.life == 0:
                    bus.gridList[plant.gridX][plant.gridY] = -1
                    bus.paintPlants.remove(plant)
                    if zb.images == sets.zombieLostHeadAttackImages:
                        zb.images = sets.zombieLostHeadImages
                    else:
                        if zb.images == sets.normalAttackImages:
                            zb.images = sets.zombie_normalImages
                        elif zb.images == sets.coneheadAttackImages:
                            zb.images = sets.zombie_coneheadImages
                        else:
                            zb.images = sets.zombie_bucketImages



# 僵尸被攻击
def hit(zombie):
    for bullet in bus.bullets:
        if zombie.hitBy(bullet) and not isinstance(zombie, Zombie_head) and not isinstance(zombie, Zombie_dead):
            zombie.life -= 1
            # 豌豆不穿透，仙人掌刺穿透
            if bullet.type == 0:
                # for i in range(100):
                #     screen.blit(sets.bulletHitImg, (zombie.x-100, zombie.y))
                bus.bullets.remove(bullet)

            if zombie.life == 5:
                if not isinstance(zombie, Zombie_normal):
                    zombie.images = sets.zombie_normalImages
            elif zombie.life == 3:
                if zombie.headFlag is True:
                    zombie.images = sets.zombieLostHeadImages
                    bus.zombies.append(Zombie_head(screen, sets.zombieHeadImages, zombie.x, zombie.y))
            elif zombie.life == 0:
                bus.zombies.append(Zombie_dead(screen, sets.zombieDieImages, zombie.x, zombie.y))

        # 子弹越界删除
        if bullet.outOfBounds():
            bus.bullets.remove(bullet)


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
