import pygame
import sys

def characters_screen(screen, clock, WIDTH, HEIGHT, font_button, BROWN):
    background_image = pygame.image.load("characters/char_mainphoto.jpg")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    color=(238,212,161)
    characters = [
        {"button_label": "choose", "var_name": "CHAR1", "image": "none"},
        {"button_label": "choose", "var_name": "CHAR2", "image": "characters/superman.png"},
        {"button_label": "choose", "var_name": "CHAR3", "image": "characters/char3.png"},
        {"button_label": "choose", "var_name": "CHAR4", "image": "characters/char4.png"},
        {"button_label": "choose", "var_name": "CHAR5", "image": "characters/char5.png"},
        {"button_label": "choose", "var_name": "CHAR6", "image": "characters/char6.png"},
        {"button_label": "choose", "var_name": "CHAR7", "image": "characters/char7.png"},
        {"button_label": "choose", "var_name": "CHAR8", "image": "characters/char8.png"},
        {"button_label":"choose", "var_name": "CHAR9", "image": "characters/char9.png"},
        {"button_label": "choose", "var_name": "CHAR10", "image": "characters/char10.png"},
        {"button_label": "choose", "var_name": "CHAR11", "image": "characters/char11.png"},
        {"button_label": "choose", "var_name": "CHAR12", "image": "characters/char12.png"},
    ]

    button_positions = [
        (50, 90), (200, 90), (350, 90),

        (50, 250), (200, 250), (350, 250),

        (50, 410), (200, 410), (350, 410),

        (50, 570), (200, 570), (350, 570),
    ]

    buttons = [pygame.Rect(x, y+100, 100, 20) for (x, y) in button_positions]

    while True:
        screen.blit(background_image, (0, 0))

        # The title of menu of the Characters
        title_font = pygame.font.SysFont("comicsansms", 40)
        title2_font = pygame.font.SysFont("comicsansms", 55)
        title = title_font.render("CHOOSE A", True, color)
        title2=title2_font.render("CHARACTER", True, color)
        screen.blit(title, (WIDTH//2-80, 5))
        screen.blit(title2, (WIDTH // 2 - title.get_width()// 2-40, 30))

        # Draw the choose Buttonss
        for i, rect in enumerate(buttons):
            
            pygame.draw.rect(screen, (19, 66, 63), rect, border_radius=10)
            pygame.draw.rect(screen,  (19, 66, 63), rect, 2, border_radius=10)
            
            
            button_text = font_button.render(characters[i]["button_label"], True, color)
            text_rect = button_text.get_rect(center=rect.center)
            screen.blit(button_text, text_rect)
 
        back_button = pygame.Rect(20, 20, 80, 40)
        pygame.draw.rect(screen, (230, 230, 230), back_button, border_radius=10)
        pygame.draw.rect(screen, BROWN, back_button, 2, border_radius=10)
        back_text = font_button.render("Back", True, BROWN)
        screen.blit(back_text, back_text.get_rect(center=back_button.center))

        #  cheack for Mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return None  
                for i, rect in enumerate(buttons):
                    if rect.collidepoint(event.pos):
                        return characters[i]["image"] 

        pygame.display.update()
        clock.tick(30)
