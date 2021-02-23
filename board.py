import pygame
from plate import Plate
import random


class Board:
    def __init__(self, width, height, screen, group):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.board[random.randint(0, 3)][random.randint(0, 3)] = random.choices([2, 4], [9, 1])[0]
        self.board[random.randint(0, 3)][random.randint(0, 3)] = random.choices([2, 4], [9, 1])[0]
        self.left = 20
        self.top = 20
        self.cell_size = 40
        self.screen = screen
        self.group = group
        print(self.board)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        plates = []
        self.screen.fill((221, 181, 148))
        for y in range(self.height):
            for x in range(self.width):
                plates.append(Plate(self.left + self.cell_size * x,
                                    self.top + self.cell_size * y,
                                    self.board[y][x], self.group))
        pygame.draw.rect(self.screen, (77, 77, 77), (self.left, self.top,
                                            self.cell_size * 4, self.cell_size * 4), 7)
        self.group.draw(self.screen)

    def move(self, direction):
        if direction == pygame.K_UP:
            for y in range(self.height - 1):
                for x in range(self.width):
                    if self.board[y + 1][x] == 0:
                        self.board[y + 1][x] = self.board[y][x]
                        self.board[y][x] = 0
                        print(self.board)
