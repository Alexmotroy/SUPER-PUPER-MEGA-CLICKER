import pygame

from boss import Boss


class BossMenu:
    def __init__(self):
        self.blocks = []
        self.fill_boss_info()
        self.fill_level_changers()

    def fill_boss_info(self):
        for i in range (1, 5):
            self.blocks.append(Boss(i))

    def fill_level_changers(self):
        self.blocks.insert(0, level_changer('left'))
        self.blocks.append(level_changer('right'))

    def draw_blocks(self,screen):
        for block in self.blocks:
            block.draw_block(screen)