import random
import pygame
from blockO import BlockO
from blockL import BlockL
from blockLMiror import BlockLMiror
from blockS import BlockS
from blockI import BlockI
from blockT import BlockT
from blockZ import BlockZ

pygame.init()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))

        self.background = pygame.image.load("./img/bg0008_bg2.png")
        self.gameFiled = pygame.image.load("./img/game_field00^q.png")
        self.holdImage = pygame.image.load("./img/game_field_hold^q.png")
        self.nextImage = pygame.image.load("./img/game_field_next^q.png")

        self.level = 0
        self.clock = pygame.time.Clock()
        self.speed = 30
        self.rotation = 0
        self.rotationCounter = 15
        self.movingCounter = 2

        self.game = [[None for j in range(10)] for i in range(20)]

        self.blockPossibilities = [
            BlockLMiror(912, 60, "red"),
            BlockL(912, 60, "darkBlue"),
            BlockO(912, 60, "yellow"),
            BlockI(912, 60, "green"),
            BlockS(912, 60, "purple"),
            BlockZ(912, 60, "orange"),
            BlockT(912, 60, "lightBlue"),
        ]
        self.block = random.choice(self.blockPossibilities)
        self.blockOnScreen = True
        self.bottomLimit = [20 for i in range(10)]
        self.onBottom = False

        self.nextBlock = []
        for i in range(3):
            self.blockPossibilities = [
                BlockLMiror(912, 60, "red"),
                BlockL(912, 60, "darkBlue"),
                BlockO(912, 60, "yellow"),
                BlockI(912, 60, "green"),
                BlockS(912, 60, "purple"),
                BlockZ(912, 60, "orange"),
                BlockT(912, 60, "lightBlue"),
            ]
            self.nextBlock.append(random.choice(self.blockPossibilities))

    def createBlock(self):
        self.blockPossibilities = [
            BlockLMiror(912, 60, "red"),
            BlockL(912, 60, "darkBlue"),
            BlockO(912, 60, "yellow"),
            BlockI(912, 60, "green"),
            BlockS(912, 60, "purple"),
            BlockZ(912, 60, "orange"),
            BlockT(912, 60, "lightBlue"),
        ]
        self.block = self.nextBlock[0]
        self.nextBlock[0], self.nextBlock[1], self.nextBlock[2] = (
            self.nextBlock[1],
            self.nextBlock[2],
            random.choice(self.blockPossibilities),
        )
        self.blockOnScreen = True
        self.speed = self.clock.get_fps()

    def input(self):
        keys = pygame.key.get_pressed()
        canLeft = True
        canRight = True

        canTurnLeft = True
        canTurnRight = True

        canGoDown = True

        if self.movingCounter <= 0 and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
            self.movingCounter = 0
            if keys[pygame.K_LEFT]:
                for i in self.block.allBlocks[self.rotation % 4]:
                    for j in i:
                        if j != None and j.rect.x > 720 and canLeft:
                            if (
                                self.game[(j.rect.y // 48) - 1][
                                    (j.rect.x // 48) - 15 - 1
                                ]
                                != None
                            ):
                                canLeft = False
                                self.movingCounter = 0
                        elif j != None:
                            canLeft = False
                            self.movingCounter = 0
                if canLeft:
                    for k in self.block.allBlocks:
                        for i in k:
                            for j in i:
                                if j != None:
                                    j.rect.x -= 48

            if keys[pygame.K_RIGHT]:
                for i in self.block.allBlocks[self.rotation % 4]:
                    for j in i:
                        if j != None and j.rect.x < 1152 and canRight:
                            if (
                                self.game[(j.rect.y // 48) - 1][
                                    (j.rect.x // 48) - 15 + 1
                                ]
                                != None
                            ):
                                canRight = False
                                self.movingCounter = 0
                        elif j != None:
                            canRight = False
                            self.movingCounter = 0
                if canRight:
                    for k in self.block.allBlocks:
                        for i in k:
                            for j in i:
                                if j != None:
                                    j.rect.x += 48

        if keys[pygame.K_DOWN]:
            for i in self.block.allBlocks[self.rotation % 4][-1]:
                if i != None and i.rect.y < 972:
                    if self.game[(i.rect.y // 48)][(i.rect.x // 48) - 15] != None:
                        canGoDown = False
                        break
                elif i != None:
                    canGoDown = False
                    break
            if canGoDown:
                self.speed -= 50

        # if keys[pygame.K_UP]:
        #     self.block.rotate()
        if self.rotationCounter <= 0 and (
            pygame.key.get_pressed()[pygame.K_q] or pygame.key.get_pressed()[pygame.K_d]
        ):
            self.rotationCounter = 10
            if pygame.key.get_pressed()[pygame.K_q]:
                for i in self.block.allBlocks[(self.rotation - 1) % 4]:
                    for j in i:
                        if (
                            j != None
                            and j.rect.x >= 720
                            and canTurnLeft
                            and j.rect.x <= 1152
                        ):
                            if (
                                self.game[(j.rect.y // 48) - 1][
                                    (j.rect.x // 48) - 15 - 1
                                ]
                                != None
                            ):
                                canTurnLeft = False
                        elif j != None:
                            canTurnLeft = False
                if canTurnLeft:
                    for i in self.block.allBlocks[(self.rotation - 1) % 4]:
                        for j in i:
                            if (
                                j != None
                                and j.rect.x <= 1152
                                and canTurnLeft
                                and j.rect.x >= 720
                            ):
                                if ((j.rect.x // 48) - 15 + 1) < 9:
                                    if (
                                        self.game[(j.rect.y // 48) - 1][
                                            (j.rect.x // 48) - 15 + 1
                                        ]
                                        != None
                                    ):
                                        canTurnLeft = False
                            elif j != None:
                                canTurnLeft = False
                    self.rotation -= 1

            if pygame.key.get_pressed()[pygame.K_d]:
                for i in self.block.allBlocks[(self.rotation + 1) % 4]:
                    for j in i:
                        if (
                            j != None
                            and j.rect.x >= 720
                            and canTurnRight
                            and j.rect.x <= 1152
                        ):
                            if (
                                self.game[(j.rect.y // 48) - 1][
                                    (j.rect.x // 48) - 15 - 1
                                ]
                                != None
                            ):
                                canTurnRight = False
                        elif j != None:
                            canTurnRight = False
                if canTurnRight:
                    for i in self.block.allBlocks[(self.rotation + 1) % 4]:
                        for j in i:
                            if (
                                j != None
                                and j.rect.x <= 1152
                                and canTurnRight
                                and j.rect.x >= 720
                            ):
                                if ((j.rect.x // 48) - 15 + 1) < 9:
                                    if (
                                        self.game[(j.rect.y // 48) - 1][
                                            (j.rect.x // 48) - 15 + 1
                                        ]
                                        != None
                                    ):
                                        canTurnRight = False
                            elif j != None:
                                canTurnRight = False
                    self.rotation += 1

    def deleteLine(self):
        for i in range(len(self.game)):
            deleteLine = True
            for j in self.game[i]:
                if j == None:
                    deleteLine = False
            if deleteLine:
                for k in range(i, 0, -1):
                    for l in range(len(self.game[k])):
                        if self.game[k][l] != None:
                            self.game[k][l].rect.y += 48
                        self.game[k][l] = self.game[k - 1][l]
        self.drawGame()
        pygame.display.flip()
        pygame.display.update()

    def drawBackgroundImages(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.gameFiled, (520, 0))
        self.screen.blit(self.holdImage, (582, 50))
        self.screen.blit(self.nextImage, (1210, 50))

    def drawBlock(self):
        for i in self.block.allBlocks[self.rotation % 4]:
            for j in i:
                if j != None:
                    self.screen.blit(j.image, (j.rect.x, j.rect.y))

    def drawGame(self):
        for i in self.game:
            for j in i:
                if j != None:
                    self.screen.blit(j.image, (j.rect.x, j.rect.y))

    def addBlockToGame(self):
        for i in self.block.allBlocks[self.rotation % 4]:
            for j in i:
                if j != None:
                    self.game[(j.rect.y // 48) - 1][(j.rect.x // 48) - 15] = j
                    self.onBottom = False

    def stopBottom(self):
        max = [20 for i in range(len(self.block.allBlocks[self.rotation % 4][0]))]
        self.onBottom = True
        self.blockOnScreen = False
        self.addBlockToGame()
        for j in self.block.allBlocks[self.rotation % 4]:
            counter = 0
            for k in j:
                if k != None and k.rect.y // 48 - 1 < max[counter]:
                    self.bottomLimit[(k.rect.x // 48) - 15] = (k.rect.y // 48) - 1
                    max[counter] = k.rect.y // 48 - 1
                counter += 1

    def touchBottom(self):
        for i in self.block.allBlocks[self.rotation % 4][-1]:
            if i != None and i.rect.y < 972:
                if self.game[(i.rect.y // 48)][(i.rect.x // 48) - 15] != None:
                    self.stopBottom()
                    break
            elif i != None:
                self.stopBottom()
                break

    def refreshScreen(self):
        self.input()
        self.drawBackgroundImages()
        self.drawBlock()
        self.drawGame()

        pygame.display.flip()
        pygame.display.update()

    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if self.speed <= 0 and not self.onBottom:
                self.speed = 40
                for k in self.block.allBlocks:
                    for i in k:
                        for j in i:
                            if j != None:
                                j.rect.y += 48
                self.input()
                self.touchBottom()
            else:
                self.speed -= 1

            self.refreshScreen()
            self.deleteLine()

            if self.blockOnScreen == False:
                self.createBlock()

            self.rotationCounter -= 1
            self.movingCounter -= 1

            self.clock.tick(60)


Game().run()
pygame.quit()
