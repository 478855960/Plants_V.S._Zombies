from util.constant import Constant
import pygame
from  pygame.locals import *

# 卡片图标鼠标跟随绘制
def cardMovePaint(bus, screen, sets):
    if bus.cardState == Constant.CARD_CLICKED:
        dict = {
            Constant.NUT_SELECTED: 0,
            Constant.SUNFLOWER_SELECTED: 1,
            Constant.PEASHOOTER_SELECTED: 2,
            Constant.CHOMPER_SELECTED: 3,
            Constant.CHERRY_SELECTED: 4,
            Constant.REPEATER_SELECTED: 5,
            Constant.SHOVEL_SELECTED: 6
        }
        drawImgIdx = dict[bus.cardSelection]
        mousex, mousey = pygame.mouse.get_pos()
        screen.blit(sets.cardImgs[drawImgIdx], (mousex - 27, mousey - 34))

# 初始场景绘制
def initScenario(bus, screen, sets):
    screen.blit(sets.background, (0, 0))
    screen.blit(sets.seedBank, (0, 0))
    # 绘制卡片
    CARD_OFFSET = 60
    dict = {
        0: sets.cardNutWall,
        1: sets.sunflower,
        2: sets.cardPeashooter,
        3: sets.cactus,
        4: sets.cherry,
        5: sets.cardPeashooterdouble
    }
    dictDark = {
        0: sets.cardNutWallDark,
        1: sets.sunflowerDark,
        2: sets.cardPeashooterDark,
        3: sets.cactusDark,
        4: sets.cherryDark,
        5: sets.cardPeashooterdoubleDark
    }
    for i in range(6):
        if i <= 1 and bus.sunScore >= 50:
            screen.blit(dict[i], (80 + CARD_OFFSET * i, 10))
        elif  1 < i <= 2 and bus.sunScore >= 100:
            screen.blit(dict[i], (80 + CARD_OFFSET * i, 10))
        elif 2 < i <= 3 and bus.sunScore >= 125:
            screen.blit(dict[i], (80 + CARD_OFFSET * i, 10))
        elif 3 < i <= 4 and bus.sunScore >= 150:
            screen.blit(dict[i], (80 + CARD_OFFSET * i, 10))
        elif 4 < i <= 5 and bus.sunScore >= 200:
            screen.blit(dict[i], (80 + CARD_OFFSET * i, 10))
        else:
            screen.blit(dictDark[i], (80 + CARD_OFFSET * i, 10))
    screen.blit(sets.cardShovelBack, (448, 0))
    screen.blit(sets.cardShovel, (444, 10))

    # 绘制暂停按钮
    screen.blit(sets.Button, (1265, 10))
    pygame.font.init()
    ft = pygame.font.Font('msyh.ttf', 28)
    Str = ft.render("暂 停", True, (0, 0, 0))
    screen.blit(Str, (1290, 10))

# 绘制太阳，包括在正在下落的和在地上的
def paintSun(bus, screen, sets):
    for i in range(len(bus.sunFall)):
        bus.sunFall[i].blitme()

    for i in range(len(bus.sunStay)):
        bus.sunStay[i].blitme()

# 绘制阳光数
def paintSunScore(bus, screen, sets):
    pygame.font.init()
    ft = pygame.font.Font('msyh.ttf', 20)
    scoreStr = ft.render("%d"%bus.sunScore, True, (0, 0, 0))
    if bus.sunScore <= 1000:
        screen.blit(scoreStr, (19, 59))
    else:
        screen.blit(scoreStr, (17, 59))


# 绘制进度条
def painProgressBar(bus, screen, sets):
    # 绘制进度条
    percentage = bus.globalTime / 100

    # 绘制开始提示标语
    if percentage <= 2 and percentage >= 1:
        screen.blit(sets.prepareGrowPlants.subsurface(Rect((0, 0), (255, 112))), (550, 240))

    if percentage >= 2 and percentage <= 3:
        screen.blit(sets.prepareGrowPlants.subsurface(Rect((0, 112), (255, 100))), (550, 240))

    if percentage >= 3 and percentage <= 4:
        screen.blit(sets.prepareGrowPlants.subsurface(Rect((0, 212), (255, 112))), (550, 240))
    if not bus.midPercentage and 40 < percentage < 99 :
        bus.music.water()
        bus.midPercentage = True

    # 绘制最后一波提示语
    if percentage >= 99 and percentage <= 100:
        screen.blit(sets.finalWave, (550, 240))
        if not bus.finalPercentage:
            bus.music.urgent()
            bus.finalPercentage = True


    screen.blit(sets.flagMeterFull, (1200, 560))

    if percentage <= 157:
        screen.blit(sets.flagMeterEmpty.subsurface(Rect((0, 0), (157 - percentage, 21))), (1200, 560))
        screen.blit(sets.flagMeterParts1, (1340 - percentage, 560))

    screen.blit(sets.flagMeterParts2, (1205, 557))

# 绘制暂停标志
def paintPause(bus, screen, sets):
    screen.blit(sets.Pause, (500, 0))
    pygame.font.init()
    ft = pygame.font.Font('msyh.ttf', 20)
    Str = ft.render("请点击鼠标左键继续", True, (255, 0, 0))
    screen.blit(Str, (550, 90))