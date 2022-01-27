import pygame


class Main:
    def __init__(self):
        pygame.init()
        self.WINDOW_WIGHT = 600
        self.WINDOW_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WINDOW_WIGHT, self.WINDOW_HEIGHT))

    def launch(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0

    def draw(self):
        self.boss.menu.draw_blocks(self.screen)
        pygame.display.flip()

main = Main()
main.launch()
