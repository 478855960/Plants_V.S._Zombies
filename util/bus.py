"""
用于保存全局状态的类
"""
from util.constant import Constant


class Bus:
    # 用于表示是否选择了卡片
    cardState = Constant.CARD_NOT_CLICKED
    # 表示选择卡片的类型
    cardSelection = Constant.NUT_SELECTED
    # 僵尸存储列表
    zombies = []
    # 僵尸频率值
    zombieIndex = 0
    # 掉头信号
    headFlag = True
