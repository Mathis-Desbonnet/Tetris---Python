import pygame
from basicBlock import BasicBlock


class BlockI(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()

        self.blocks1 = [
            [
                BasicBlock(x, y, color),
            ],
            [
                BasicBlock(x, y + 48, color),
            ],
            [
                BasicBlock(x, y + 96, color),
            ],
            [
                BasicBlock(x, y + 144, color),
            ],
        ]

        self.blocks2 = [
            [
                None,
            ],
            [
                BasicBlock(x, y + 48, color),
                BasicBlock(x + 48, y + 48, color),
                BasicBlock(x + 96, y + 48, color),
                BasicBlock(x + 144, y + 48, color),
            ],
            [
                None,
            ],
            [
                None,
            ],
        ]

        self.blocks3 = [
            [
                BasicBlock(x, y, color),
            ],
            [
                BasicBlock(x, y + 48, color),
            ],
            [
                BasicBlock(x, y + 96, color),
            ],
            [
                BasicBlock(x, y + 144, color),
            ],
        ]

        self.blocks4 = [
            [
                None,
            ],
            [None],
            [
                BasicBlock(x, y + 96, color),
                BasicBlock(x + 48, y + 96, color),
                BasicBlock(x + 96, y + 96, color),
                BasicBlock(x + 144, y + 96, color),
            ],
            [
                None,
            ],
        ]

        self.allBlocks = [self.blocks1, self.blocks2, self.blocks3, self.blocks4]
