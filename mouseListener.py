from util.constant import Constant
from conf.settings import Setting
import pygame
from util.loadimages import getImages
from entity.sun import Sun

from entity.plant.wallnut import Wallnut
from entity.plant.sunflower import Sunflower
from entity.plant.peashooter import Peashooter
from entity.plant.chomper import Chomper
from entity.plant.cherryBomb import CherryBomb
from entity.plant.repeater import Repeater
from entity.plant.cactus import Cactus

import random
sets = Setting()
# 当鼠标被点击时调用函数
# 用来绑定卡片监听事件
def cardMouseClickListener(bus):
    leftButtonDown = pygame.mouse.get_pressed()[0]
    rightButtonDown = pygame.mouse.get_pressed()[2]
    if leftButtonDown:
        mousex, mousey = pygame.mouse.get_pos()
        CARD_BASIC_X = 80
        CARD_BASIC_Y = 10
        CARD_HEIGHT = 68
        CARD_WIDTH = 55
        CARD_OFFSET = 60
        # i --> 0-坚果 1-向日葵 2-豌豆射手 3-食人花 4-樱桃炸弹 5-豌豆射手double
        # 设置count循环次数 控制暗色植物不能点击
        rangeCount = 0
        if bus.sunScore < 50:
            rangeCount = 0
        elif 50 <= bus.sunScore < 100:
            rangeCount = 2
        elif 100 <= bus.sunScore < 150:
            rangeCount = 3
        elif 150 <= bus.sunScore < 200:
            rangeCount = 5
        else:
            rangeCount = 6

        # 选择卡片
        for i in range(rangeCount):
            if CARD_BASIC_X + CARD_OFFSET * i < mousex < CARD_BASIC_X + CARD_WIDTH + CARD_OFFSET * i and \
                    CARD_BASIC_Y < mousey < CARD_BASIC_Y + CARD_HEIGHT:
                dict = {
                    0: Constant.NUT_SELECTED,
                    1: Constant.SUNFLOWER_SELECTED,
                    2: Constant.PEASHOOTER_SELECTED,
                    3: Constant.CHOMPER_SELECTED,
                    4: Constant.CHERRY_SELECTED,
                    5: Constant.REPEATER_SELECTED,
                }
                bus.cardState = Constant.CARD_CLICKED
                bus.cardSelection = dict[i]
        ## 选择铲子
        if CARD_BASIC_X + CARD_OFFSET * 6 < mousex < CARD_BASIC_X + CARD_WIDTH + CARD_OFFSET * 6 and \
                    CARD_BASIC_Y < mousey < CARD_BASIC_Y + CARD_HEIGHT:
            bus.cardState = Constant.CARD_CLICKED
            bus.cardSelection = Constant.SHOVEL_SELECTED
    if rightButtonDown:
        bus.cardState = Constant.CARD_NOT_CLICKED

# 用来判断格子的X坐标（即鼠标点击在第几列的格子里）
def getGridX(mouseX):
    if mouseX < sets.gridXIndexes[0]:
        return -1
    for i in range(len(sets.gridXIndexes)):
        if mouseX <= sets.gridXIndexes[i]:
            return i - 1
    return -1

# 用来绑定卡片监听事件
def initPlantsMouseClickListener(bus, screen):
    leftButtonDown = pygame.mouse.get_pressed()[0]
    if leftButtonDown:
        mouseX, mouseY = pygame.mouse.get_pos()
        gridX = getGridX(mouseX)
        gridY = int((mouseY - sets.topY) / sets.gridHeight)
        plantX = sets.gridXIndexes[gridX]
        plantY = sets.topY + sets.gridHeight * gridY
        if mouseX >= sets.leftX and mouseX <= sets.rightX \
            and mouseY <= sets.bottomY and mouseY >= sets.topY \
                    and bus.gridList[gridX][gridY] == -1:
            imagedict = {
                Constant.NUT_SELECTED: 0,
                Constant.SUNFLOWER_SELECTED: 1,
                Constant.PEASHOOTER_SELECTED: 2,
                Constant.CHOMPER_SELECTED: 3,
                Constant.CHERRY_SELECTED: 4,
                Constant.REPEATER_SELECTED: 5,
            }
            plantdict = [
                Wallnut(screen, plantX, plantY, getImages(sets.plantsInitImages[0])),
                Sunflower(screen, plantX, plantY, getImages(sets.plantsInitImages[1])),
                Peashooter(screen, plantX, plantY, getImages(sets.plantsInitImages[2])),
                Cactus(screen, plantX, plantY, getImages(sets.plantsInitImages[3])),
                CherryBomb(screen, plantX, plantY, getImages(sets.plantsInitImages[4]), bus),
                Repeater(screen, plantX, plantY, getImages(sets.plantsInitImages[5])),
            ]
            if bus.cardState == Constant.CARD_CLICKED and bus.cardSelection in imagedict:
                index = imagedict[bus.cardSelection]
                plantdict[index].gridX = gridX
                plantdict[index].gridY = gridY
                bus.paintPlants.append(plantdict[index])
                bus.cardState = Constant.CARD_NOT_CLICKED
                bus.sunScore -= plantdict[index].sunshine
                bus.gridList[gridX][gridY] = index

def sunMouseClickListener(bus, screen, sets):
        # 获取列表  中左键   返回 True  False
        leftFlag = pygame.mouse.get_pressed()[0]

        mouseX, mouseY = pygame.mouse.get_pos()

        # 判断鼠标是否点击到了材料
        for i in range(len(bus.sunFall)):
            if leftFlag and mouseX > bus.sunFall[i].x and mouseX < bus.sunFall[i].x + bus.sunFall[i].width and \
                    mouseY > bus.sunFall[i].y and mouseY < bus.sunFall[i].y + bus.sunFall[i].height:
                bus.sunScore += bus.sunFall[i].score
                xx = random.randint(260, 880)
                yy = -random.randint(100, 300)
                goal = random.randint(300, 600)
                bus.sunFall[i] = Sun(screen, sets.sunImage, xx, yy, goal)
                break

        for i in range(len(bus.sunStay)):
            if leftFlag and mouseX > bus.sunStay[i].x and mouseX < bus.sunStay[i].x + bus.sunStay[i].width and \
                    mouseY > bus.sunStay[i].y and mouseY < bus.sunStay[i].y + bus.sunStay[i].height:
                bus.sunScore += bus.sunStay[i].score
                xx = random.randint(260, 880)
                yy = -random.randint(100, 300)
                goal = random.randint(300, 600)
                bus.sunStay[i] = Sun(screen, sets.sunImage, xx, yy, goal)
                break

def runOrPause(bus, screen, sets):
    leftFlag = pygame.mouse.get_pressed()[0]

    mouseX, mouseY = pygame.mouse.get_pos()

    if mouseX >= 1265 and mouseX <= 1265 + 113 and mouseY >= 10 and mouseY <= 10 + 41 and bus.state == bus.RUNNING:
        bus.state = bus.PAUSE
    else:
        bus.state = bus.RUNNING
