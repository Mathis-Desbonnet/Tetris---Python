import pygame

pygame.init()


class Game:
    def __init__(self):
        pygame.display.set_mode((1920, 1080))

    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


pygame.quit()
