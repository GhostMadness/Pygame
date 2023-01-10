import pygame
# UTF-8

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Phantom")
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    music = pygame.mixer.Sound('MUSIC\FIRST\MENU.mp3')
    music.set_volume(0.05)
    music.play(-1)
    IMG_MENU = pygame.image.load("SPRITE\MAIN_10.png")
    IMG_EXIT_BUTTON = pygame.image.load("SPRITE\EXIT_BUTTON.png")
    IMG_PLAY_BUTTON = pygame.image.load("SPRITE\PLAY_BUTTON.png")
    IMG_SETTING_BUTTON = pygame.image.load("SPRITE\SETTING_BUTTON.png")

    rect_1 = IMG_EXIT_BUTTON.get_rect()
    rect_1.x = 43
    rect_1.y = 620 + 50

    rect_2 = IMG_SETTING_BUTTON.get_rect()
    rect_2.x = 43
    rect_2.y = 345 + 50

    rect_3 = IMG_PLAY_BUTTON.get_rect()
    rect_3.x = 43
    rect_3.y = 70 + 50

    print(rect_1)



    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                print(str((x, y)))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect_1[0] < event.pos[0] < rect_1[0] + rect_1[2] and rect_1[1] < event.pos[1] < rect_1[1] + rect_1[3]:
                    running = False
                if rect_1[0] < event.pos[0] < rect_1[0] + rect_1[2] and rect_1[1] < event.pos[1] < rect_1[1] + rect_1[3]:
                    print("baba boy")
                if rect_1[0] < event.pos[0] < rect_1[0] + rect_1[2] and rect_1[1] < event.pos[1] < rect_1[1] + rect_1[3]:
                    print("baba boy")

        screen.fill((0, 0, 0))
        screen.blit(IMG_MENU, (0, 0))
        screen.blit(IMG_PLAY_BUTTON, (43, 70 + 50))
        screen.blit(IMG_SETTING_BUTTON, (43, 345 + 50))
        screen.blit(IMG_EXIT_BUTTON, (43, 620 + 50))
        pygame.display.flip()