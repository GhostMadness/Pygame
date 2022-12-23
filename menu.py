import pygame

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

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                pos = event.pos
                print(pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] >= 45 and pos[0] <= 360:
                    if pos[1] >= 167 and pos[1] <= 503:
                        running = False
                        print('goodbye')
                        #ÇÄÅÑÜ ÏÎÒÎÌ ÁÓÄÅÌ ÇÀÃÐÓÆÀÒÜ ÎÒÄÅËÜÍÓÞ ÑÖÅÍÓ ÈÃÐÛ
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] >= 46 and pos[0] <= 715:
                    if pos[1] >= 502 and pos[1] <= 913:
                        running = False
                        print('goodbye2')
                        #ÂÛÕÎÄ
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] >= 45 and pos[0] <= 503:
                    if pos[1] >= 441 and pos[1] <= 640:
                        running = False
                        print('goodbye1')
                        #ÇÄÅÑÜ ÏÎÒÎÌ ÁÓÄÅÌ ÇÀÃÐÓÆÀÒÜ ÎÒÄÅËÜÍÓÞ ÑÖÅÍÓ ÍÀÑÒÐÎÅÊ

        screen.fill((0, 0, 0))
        screen.blit(IMG_MENU, (0, 0))
        screen.blit(IMG_PLAY_BUTTON, (25, 50))
        screen.blit(IMG_SETTING_BUTTON, (25, 325))
        screen.blit(IMG_EXIT_BUTTON, (25, 600))
        pygame.display.flip()