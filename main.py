import pygame
import pygame_gui
from board import Board


def draw_screen(screnn):
    board.render()
    font = pygame.font.Font(None, 50)
    text_score = font.render("Счёт", True, (100, 50, 0))
    text_x = 50
    text_y = 30
    text_w = text_score.get_width()
    text_h = text_score.get_height()
    screen.blit(text_score, (text_x, text_y))
    pygame.draw.rect(screen, (180, 130, 80), (text_x - 10, text_y + 50,
                                              text_w + 20, text_h + 20), 0, border_radius=5)
    text_score_value = font.render(str(sum([sum(x) for x in board.board])), True, (100, 50, 0))
    screen.blit(text_score_value, (40 + ((text_w + 20 - text_score_value.get_width()) // 2),
                                   81 + ((text_h + 20 - text_score_value.get_height()) // 2)))
    pygame.display.flip()


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
        if event.type == pygame.KEYDOWN:
            board.move(event.type)
    draw_screen(screen)
pygame.quit()
