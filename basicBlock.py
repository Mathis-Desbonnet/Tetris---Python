import pygame


class BasicBlock(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.posByColor = {
            "grey": (4, 4),
            "darkBlue": (60, 4),
            "green": (116, 4),
            "orange": (172, 4),
            "purple": (228, 4),
            "red": (284, 4),
            "lightBlue": (340, 4),
            "yellow": (396, 4),
        }

        self.image = pygame.image.load("./img/minos00.png").subsurface(
            self.posByColor[color][0], self.posByColor[color][1], 48, 48
        )
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
