import pygame

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Phantom")
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    background_img = pygame.image.load("SPRITE\SETTINGS_FON_2.jpg")
    button_menu_img = pygame.image.load("SPRITE\EXIT_MENU_BUTTON.png")
    button_menu_img_tr = pygame.transform.scale(button_menu_img, (50, 50))

    music_settings = pygame.mixer.Sound('SETTING_FILES\SETTING.oga')
    
    rect_but_menu = button_menu_img_tr.get_rect()
    rect_but_menu.x = 10
    rect_but_menu.y = 10

    music_settings.set_volume(0.1)
    music_settings.play(-1)

    font = pygame.font.Font(None, 50)
    text = font.render("УПРАВЛЕНИЕ", True, (230, 230, 230))
    text_x = 1920 // 2 - 50
    text_y = 1080 // 2 - 50
    text_w = text.get_width()
    text_h = text.get_height()

    text_w = font.render("ВВЕРХ - W", True, (230, 230, 230))
    text_w_x = 1920 // 2 - 50
    text_w_y = 1080 // 2 - 20
    text_w_w = text_w.get_width()
    text_w_h = text_w.get_height()

    text_s = font.render("ВНИЗ - S", True, (230, 230, 230))
    text_s_x = 1920 // 2 - 50
    text_s_y = 1080 // 2 + 10
    text_s_w = text_s.get_width()
    text_s_h = text_s.get_height()

    text_d = font.render("ВПРАВО - D", True, (230, 230, 230))
    text_d_x = 1920 // 2 - 50
    text_d_y = 1080 // 2 + 40
    text_d_w = text_d.get_width()
    text_d_h = text_d.get_height()
    
    text_a = font.render("ВЛЕВО - A", True, (230, 230, 230))
    text_a_x = 1920 // 2 - 50
    text_a_y = 1080 // 2 + 70
    text_a_w = text_a.get_width()
    text_a_h = text_a.get_height()

    text_enter = font.render("ГОВОРИТЬ - ENTER", True, (230, 230, 230))
    text_enter_x = 1920 // 2 - 50
    text_enter_y = 1080 // 2 + 100
    text_enter_w = text_enter.get_width()
    text_enter_h = text_enter.get_height()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_but_menu[0] < event.pos[0] < rect_but_menu[0] + rect_but_menu[2] and rect_but_menu[1] < event.pos[1] < rect_but_menu[1] + rect_but_menu[3]:
                        running = False
        screen.blit(background_img, (0, 0))
        screen.blit(button_menu_img_tr, (10, 10))
        screen.blit(text, (text_x, text_y))
        screen.blit(text_w, (text_w_x, text_w_y))
        screen.blit(text_s, (text_s_x, text_s_y))
        screen.blit(text_a, (text_a_x, text_a_y))
        screen.blit(text_d, (text_d_x, text_d_y))
        screen.blit(text_enter, (text_enter_x, text_enter_y))
        pygame.display.flip()
pygame.quit()