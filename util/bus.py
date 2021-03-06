"""
用于保存全局状态的类
"""
from util.constant import Constant


class Bus:
    # 用于表示是否选择了卡片
    cardState = Constant.CARD_NOT_CLICKED

    # 表示选择卡片的类型
    cardSelection = Constant.NUT_SELECTED

    # 表示当前需要绘制的图片
    paintPlants = []

    # 僵尸存储列表
    zombies = []
    # 僵尸频率值
    zombieIndex = 0
    # 掉头信号
    headFlag = True
    zombieRate = 0

    # 存放正在下落太阳的列表
    sunFall = []
    # 存放已经停止的太阳的列表
    sunStay = []
    # 记录初始阳光数的
    sunScore = 100
    # 初始化4个太阳  xx  yy 分别记录太阳的x坐标和y坐标
    # xx = []
    # yy = []

    # 全局统一的时间轴
    globalTime = 0

    # 格子的二维数组
    gridList = [([-1] * 5) for i in range(9)]

    # 游戏状态
    START = 0
    RUNNING = 1
    PAUSE = 2
    END = 3
    DEAD = 4
    state = START

    music = None

    # 子弹存储列表
    bullets = []

    #是否进入中段和末段
    midPercentage = False
    finalPercentage = False

    # 植物频率值
    plantIndex = 0
    # 子弹生成频率值
    shootIndex = 0

    # 游戏结束信号
    endFlag = 0

