import pygame

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))

        self.background = pygame.image.load("./img/bg0008_bg2.png")
        self.gameFiled = pygame.image.load("./img/game_field00^q.png")
        self.holdImage = pygame.image.load("./img/game_field_hold^q.png")
        self.nextImage = pygame.image.load("./img/game_field_next^q.png")

    def drawBackgroundImages(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.gameFiled, (520, 0))
        self.screen.blit(self.holdImage, (582, 50))
        self.screen.blit(self.nextImage, (1210, 50))

    def refreshScreen(self):
        self.drawBackgroundImages()

        pygame.display.flip()
        pygame.display.update()

    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.refreshScreen()


Game().run()
pygame.quit()
