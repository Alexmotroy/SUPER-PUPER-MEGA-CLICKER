import pygame.image


class Boss:
    def __init__(self):
        self.level = level
        self.gold = level * 2
        self.health = level * 100


        self.font = pygame.font.SysFont('arial', 30)
        self.block_picture = self.font.render(str(level), False, (0, 0, 255))


        self.picture = pygame.image.load('img/boss.jpg')
        self.pos = (100, 100)


    def draw_block(self, screen):
        screen.blit(self.block_picture, self.pos)
