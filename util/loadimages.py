'''
用于读取图片集并返回
'''
import os, pygame
def getImages(dir):
    # 统计图片的数量
    imageCounts = 0
    for i in os.listdir(dir):
        imageCounts += 1
    images = []
    imageStr = ""
    for j in range(imageCounts):
        imageStr = dir + str(j) + '.png'
        img = pygame.image.load(imageStr)
        images.append(img)
    return images

