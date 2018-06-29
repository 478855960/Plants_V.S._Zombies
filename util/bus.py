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