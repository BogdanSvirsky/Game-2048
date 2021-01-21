import pygame
from board import Board


pygame.init()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((400, 600))
board = Board(4, 4, screen, all_sprites)
board.set_view(60, 250, 70)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        if event.type == pygame.KEYUP:
            board.move('up')
    screen.fill((239, 220, 214))
    board.render()
    pygame.display.flip()
pygame.quit()