import pygame
import random
from entity.sun import Sun

def sunAction(bus, screen, sets):
    for i in range(len(bus.sunFall)):
        bus.sunFall[i].step()
        # 阳光落到地上后，生成新的下落阳光
        if bus.sunFall[i].index == bus.sunFall[i].goal:
            bus.sunStay.append(bus.sunFall[i])
            xx = random.randint(260, 880)
            yy = -random.randint(100, 300)
            goal = random.randint(300, 600)
            bus.sunFall[i] = Sun(screen, sets.sunImage, xx, yy, goal)

            break
    # 掉在地上的阳光如果不去点击收集，过一段时间会自动消失
    for i in range(len(bus.sunStay)):
        bus.sunStay[i].disappearTime += 1

    for i in range(len(bus.sunStay)):
        if bus.sunStay[i].disappearTime == 200:
            del bus.sunStay[i]
            break

def endAction(bus, screen, sets):
    if bus.endFlag == 1 and len(bus.zombies) == 0:
        bus.state = bus.END
        return

    for zombie in bus.zombies:
        if zombie.outOfBounds():
            bus.state = bus.DEAD
            break

