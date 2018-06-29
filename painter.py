from util.constant import Constant
import pygame

# 卡片图标鼠标跟随绘制
def cardMovePaint(bus, screen, sets):
    if bus.cardState == Constant.CARD_CLICKED:
        dict = {
            Constant.NUT_SELECTED: 0,
            Constant.SUNFLOWER_SELECTED: 1,
            Constant.PEASHOOTER_SELECTED: 2,
            Constant.CHOMPER_SELECTED: 3,
            Constant.CHERRY_SELECTED: 4,
            Constant.REPEATER_SELECTED: 5
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
    screen.blit(sets.cardNutWall, (80, 10))
    screen.blit(sets.sunflower, (80 + CARD_OFFSET * 1, 10))
    screen.blit(sets.cardPeashooter, (80 + CARD_OFFSET * 2, 10))
    screen.blit(sets.chomper, (80 + CARD_OFFSET * 3, 10))
    screen.blit(sets.cherry, (80 + CARD_OFFSET * 4, 10))
    screen.blit(sets.cardPeashooterdouble, (80 + CARD_OFFSET * 5, 10))