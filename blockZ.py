import pygame
from basicBlock import BasicBlock


class BlockZ(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()

        self.blocks = [
            [BasicBlock(x, y, color), BasicBlock(x + 48, y, color), None],
            [
                None,
                BasicBlock(x + 48, y + 48, color),
                BasicBlock(x + 96, y + 48, color),
            ],
        ]
