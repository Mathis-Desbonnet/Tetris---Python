import pygame
from basicBlock import BasicBlock


class BlockLMiror(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()

        self.blocks = [
            [None, None, BasicBlock(x + 96, y, color)],
            [
                BasicBlock(x, y + 48, color),
                BasicBlock(x + 48, y + 48, color),
                BasicBlock(x + 96, y + 48, color),
            ],
        ]
