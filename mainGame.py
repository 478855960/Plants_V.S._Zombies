import pygame,sys
from conf.settings import Setting

sets = Setting()

screen = pygame.display.set_mode((1400, 600), 0, 0)


# 初始场景绘制
def initScenario():
    screen.blit(sets.background, (0, 0))
    screen.blit(sets.seedBank, (0, 0))



# 场景绘制主函数
def paint():
    initScenario()



# 业务逻辑主函数
def action():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



def main():
    pygame.display.set_caption("植物大战僵尸")

    while True:

        action()
        paint()

        pygame.display.update()





if __name__ == '__main__':
    main()