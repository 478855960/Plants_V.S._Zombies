"""
游戏音乐模块
"""

import pygame

class MusicPlayer:
    def __init__(self):
        self.curMusic = 'music/UraniwaNi.mp3'
        pygame.mixer.init()


    def play(self):
        pygame.mixer.music.load(self.curMusic)
        pygame.mixer.music.play(3)

    def stop(self):
        pygame.mixer.music.stop()

    def water(self):
        self.curMusic = 'music/WateryGraves.mp3'
        self.play()

    def urgent(self):
        self.curMusic = 'music/urgent.mp3'
        self.play()