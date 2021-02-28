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
    manager.draw_ui(screnn)
    pygame.display.flip()


pygame.init()
all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((400, 600))
manager = pygame_gui.UIManager((800, 600))
board = Board(4, 4, screen, all_sprites)
board.set_view(60, 250, 70)
save_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(200, 30, 170, 50),
                                           text="Сохранить", manager=manager)
open_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(200, 90, 170, 50),
                                           text="Загрузить", manager=manager)
help_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(360, 550, 30, 30),
                                           text="?", manager=manager)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
        if event.type == pygame.KEYDOWN:
            board.move(pygame.key.get_pressed())
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == save_button:
                    print('Hello World!')
        manager.process_events(event)
    manager.update(time_delta=1)
    draw_screen(screen)
pygame.quit()
