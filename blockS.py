import pygame
from basicBlock import BasicBlock


class BlockS(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()

        self.name = "S"

        self.blocks1 = [
            [None, BasicBlock(x + 48, y, color), BasicBlock(x + 96, y, color)],
            [
                BasicBlock(x, y + 48, color),
                BasicBlock(x + 48, y + 48, color),
                None,
            ],
        ]

        self.blocks2 = [
            [BasicBlock(x, y, color), None],
            [BasicBlock(x, y + 48, color), BasicBlock(x + 48, y + 48, color)],
            [None, BasicBlock(x + 48, y + 96, color)],
        ]

        self.blocks3 = [
            [None, BasicBlock(x + 48, y, color), BasicBlock(x + 96, y, color)],
            [
                BasicBlock(x, y + 48, color),
                BasicBlock(x + 48, y + 48, color),
                None,
            ],
        ]

        self.blocks4 = [
            [BasicBlock(x, y, color), None],
            [BasicBlock(x, y + 48, color), BasicBlock(x + 48, y + 48, color)],
            [None, BasicBlock(x + 48, y + 96, color)],
        ]

        self.allBlocks = [self.blocks1, self.blocks2, self.blocks3, self.blocks4]
