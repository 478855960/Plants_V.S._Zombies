from util.constant import Constant
from conf.settings import Setting
import pygame
from util.loadimages import getImages
from entity.sunflower import Sunflower
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
        for i in range(6):
            if CARD_BASIC_X + CARD_OFFSET * i < mousex < CARD_BASIC_X + CARD_WIDTH + CARD_OFFSET * i and \
                    CARD_BASIC_Y < mousey < CARD_BASIC_Y + CARD_HEIGHT:
                dict = {
                    0: Constant.NUT_SELECTED,
                    1: Constant.SUNFLOWER_SELECTED,
                    2: Constant.PEASHOOTER_SELECTED,
                    3: Constant.CHOMPER_SELECTED,
                    4: Constant.CHERRY_SELECTED,
                    5: Constant.REPEATER_SELECTED
                }
                bus.cardState = Constant.CARD_CLICKED
                bus.cardSelection = dict[i]
    if rightButtonDown:
        bus.cardState = Constant.CARD_NOT_CLICKED

# 用来绑定卡片监听事件
def initPlantsMouseClickListener(bus, screen):
    leftButtonDown = pygame.mouse.get_pressed()[0]
    if leftButtonDown:
        mousex, mousey = pygame.mouse.get_pos()
        if bus.cardState == Constant.CARD_CLICKED:
            if bus.cardSelection == Constant.SUNFLOWER_SELECTED:
                imgsPath = sets.initPlantsImg[1]
                imgs = getImages(imgsPath)
                sunflower = Sunflower(screen, mousex, mousey, imgs)
                bus.paintPlants.append(sunflower)
