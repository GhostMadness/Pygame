import pygame
gl_mus = False
def button_music():
    global gl_mus
    with open('SETTING_FILES\SETTING.txt') as f:
        text = f.read()
        text = text.split('=')
        if text[0] == "music" and text[2] == 1:
            gl_mus = True
        else:
            gl_mus = False
def click():
    global rgb_but, rgb_fLag
    if rgb_fLag % 2 == 0:
        rgb_but = (255, 0, 0)
        with open ('SETTING_FILES\SETTING.txt', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace('music =1', 'music =0')
        with open ('SETTING_FILES\SETTING.txt', 'w') as f:
            f.write(new_data)
    else:
        rgb_but = (0, 255, 0)
        with open ('SETTING_FILES\SETTING.txt', 'r') as f:
            old_data = f.read()
        new_data = old_data.replace('music =0', 'music =1')
        with open ('SETTING_FILES\SETTING.txt', 'w') as f:
            f.write(new_data)

if __name__ == "__main__":
    global button, rgb_but, rgb_fLag
    pygame.init()
    pygame.display.set_caption("Phantom")
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    background_img = pygame.image.load("SPRITE\SETTINGS_FON_2.jpg")
    button_menu_img = pygame.image.load("SPRITE\EXIT_MENU_BUTTON.png")
    button_menu_img_tr = pygame.transform.scale(button_menu_img, (50, 50))
    
    rect_but_menu = button_menu_img_tr.get_rect()
    rect_but_menu.x = 10
    rect_but_menu.y = 10

    rgb_but = (0, 255, 0)
    rgb_fLag = 1

    font = pygame.font.Font(None, 50)
    text = font.render("МУЗЫКА", True, (100, 255, 100))
    text_x = 730
    text_y = 197
    text_w = text.get_width()
    text_h = text.get_height()

    with open('SETTING_FILES\SETTING.txt') as f:
        print(f.read())

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button[0] < event.pos[0] < button[0] + button[2] and button[1] < event.pos[1] < button[1] + button[3]:
                    click()
                    rgb_fLag += 1
                if rect_but_menu[0] < event.pos[0] < rect_but_menu[0] + rect_but_menu[2] and rect_but_menu[1] < event.pos[1] < rect_but_menu[1] + rect_but_menu[3]:
                    running = False
        screen.blit(background_img, (0, 0))
        screen.blit(button_menu_img_tr, rect_but_menu)
        button = pygame.draw.rect(screen, rgb_but, (900, 200, 25, 25))
        screen.blit(text, (text_x, text_y))
        button_music()
        pygame.display.flip()
pygame.quit()