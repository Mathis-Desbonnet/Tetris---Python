import pygame
from basicBlock import BasicBlock


class BlockZ(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()

        self.name = "Z"

        self.blocks1 = [
            [BasicBlock(x, y, color), BasicBlock(x + 48, y, color), None],
            [
                None,
                BasicBlock(x + 48, y + 48, color),
                BasicBlock(x + 96, y + 48, color),
            ],
        ]

        self.blocks2 = [
            [None, BasicBlock(x + 48, y, color)],
            [BasicBlock(x, y + 48, color), BasicBlock(x + 48, y + 48, color)],
            [BasicBlock(x, y + 96, color), None],
        ]

        self.blocks3 = [
            [BasicBlock(x, y, color), BasicBlock(x + 48, y, color), None],
            [
                None,
                BasicBlock(x + 48, y + 48, color),
                BasicBlock(x + 96, y + 48, color),
            ],
        ]

        self.blocks4 = [
            [None, BasicBlock(x + 48, y, color)],
            [BasicBlock(x, y + 48, color), BasicBlock(x + 48, y + 48, color)],
            [BasicBlock(x, y + 96, color), None],
        ]

        self.allBlocks = [self.blocks1, self.blocks2, self.blocks3, self.blocks4]
