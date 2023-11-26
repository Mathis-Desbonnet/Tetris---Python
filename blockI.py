import pygame
from basicBlock import BasicBlock


class BlockI(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()

        self.blocks = [
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
