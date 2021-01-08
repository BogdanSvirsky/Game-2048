import pygame
from plate import Plate
from random import choices


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[2] * width for _ in range(height)]
        self.left = 20
        self.top = 20
        self.cell_size = 40
        self.plates = []

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        screen.fill((221, 181, 148))
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x]:
                    self.plates.append(Plate(self.left + self.cell_size * x,
                                             self.top + self.cell_size * y,
                                             self.board[y][x], all_sprites))
                else:
                    pygame.draw.rect(screen, (128, 128, 128), (self.left + self.cell_size * x,
                                                                self.top + self.cell_size * y,
                                                                self.cell_size,
                                                                self.cell_size), 0)
                pygame.draw.rect(screen, (77, 77, 77), (self.left + self.cell_size * x,
                                                    self.top + self.cell_size * y,
                                                    self.cell_size,
                                                    self.cell_size), 7)


pygame.init()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((400, 600))
board = Board(4, 4)
board.set_view(60, 250, 70)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((239, 220, 214))
    board.render()
    pygame.display.flip()
pygame.quit()
