import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return pygame.transform.scale(image, (70, 70))


class Plate(pygame.sprite.Sprite):
    def __init__(self, x, y, num, group):
        super().__init__(group)
        self.image = load_image(f"{str(num)}.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, x, y, num):
        self.rect.x = x
        self.rect.y = y
        self.image = load_image(f"{str(num)}.png")
