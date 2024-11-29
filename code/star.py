import pygame
from os.path import join
from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from random import randint


class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf: pygame.Surface):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(
            center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))
