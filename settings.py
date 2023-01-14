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
        pygame.display.flip()
pygame.quit()