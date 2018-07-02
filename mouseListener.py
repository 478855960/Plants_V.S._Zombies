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
import sys
from util.bus import Bus
from musicplayer import MusicPlayer

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
        # i --> 0-坚果 1-向日葵 2-豌豆射手 3-仙人掌 4-樱桃炸弹 5-豌豆射手double
        # 设置count循环次数 控制暗色植物不能点击
        rangeCount = 0
        if bus.sunScore < 50:
            rangeCount = 0
        elif 50 <= bus.sunScore < 100:
            rangeCount = 2
        elif 100 <= bus.sunScore < 125:
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
        # 如果选中的是铲子
        elif bus.cardState == Constant.CARD_CLICKED and bus.cardSelection == Constant.SHOVEL_SELECTED \
                and bus.gridList[gridX][gridY] != -1:
            for i in range(len(bus.paintPlants)):
                if bus.paintPlants[i].gridX == gridX \
                        and bus.paintPlants[i].gridY == gridY:
                    del bus.paintPlants[i]
                    break
            bus.gridList[gridX][gridY] = -1
            bus.cardState = Constant.CARD_NOT_CLICKED

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
    elif 740 < mouseX  < 740 + 500 and 100 < mouseY < 200 + 100 and bus.state == bus.START:
        bus.state = bus.RUNNING
    elif 1257 < mouseX < 1350 and 495 < mouseY < 539:
        sys.exit(0)
    elif leftFlag and bus.state == bus.PAUSE:
        bus.state = bus.RUNNING
    elif bus.state == bus.DEAD or bus.state == bus.END:
        if 555 < mouseX < 780 and  340 < mouseY < 390 :
            restart(bus, screen)
            bus.state = bus.START
        elif 555 < mouseX < 780 and  410 < mouseY < 460 :
            sys.exit(0)

# 初始化bus中的各个值
def restart(bus, screen):
    # 用于表示是否选择了卡片
    bus.cardState = Constant.CARD_NOT_CLICKED

    # 表示选择卡片的类型
    bus.cardSelection = Constant.NUT_SELECTED

    # 表示当前需要绘制的图片
    bus.paintPlants = []

    # 僵尸存储列表
    bus.zombies = []
    # 僵尸频率值
    bus.zombieIndex = 0
    # 掉头信号
    bus.headFlag = True
    bus.zombieRate = 0

    # 存放正在下落太阳的列表
    bus.sunFall = []
    # 存放已经停止的太阳的列表
    bus.sunStay = []

    for i in range(1):
        xx = random.randint(260, 880)
        yy = -random.randint(100, 300)
        goal = random.randint(300, 600)
        sun = Sun(screen, sets.sunImage, xx, yy,goal)
        bus.sunFall.append(sun)
    # 记录初始阳光数的
    bus.sunScore = 100
    # 初始化4个太阳  xx  yy 分别记录太阳的x坐标和y坐标
    # xx = []
    # yy = []

    # 全局统一的时间轴
    bus.globalTime = 0

    # 格子的二维数组
    bus.gridList = [([-1] * 5) for i in range(9)]

    # 游戏状态
    bus.state = bus.START

    # 子弹存储列表
    bus.bullets = []

    #是否进入中段和末段
    bus.midPercentage = False
    bus.finalPercentage = False

    # 植物频率值
    bus.plantIndex = 0
    # 子弹生成频率值
    bus.shootIndex = 0

    # 游戏结束信号
    bus.endFlag = 0

    bus.music = MusicPlayer()
    bus.music.play()
