import pygame
import random
import time
# UTF-8


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Phantom")
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    image_loading = pygame.image.load("SPRITE\APPLE_HILL.png")
    image_player = pygame.image.load("SPRITE\гг.png")
    music = pygame.mixer.Sound('MUSIC\WHAT\ZVEK_KYCANIA.mp3')
    angle = 0
    running = True
    width_line = 0
    text_loading = "Загрузка"
    schet = 0
    apple_x = 2000
    a = True
    b = False
    schet_2 = -30
    schet_3 = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                print(event.pos)
        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 50)
        myfont = pygame.font.SysFont("SimSun", 15)
        text = font.render(text_loading, True, (100, 255, 100))
        text_x = 51
        text_y = 850
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))


        pygame.draw.rect(screen, (255, 255, 255), (51, 887, width_line, 50))

        screen.blit(image_player, (1920 // 2 - 100, 1080 // 2 - 100))
        if apple_x >= 1920 // 2:
            screen.blit(image_loading, (apple_x, 1080 // 2- 100))
        elif a and apple_x <= 1920 // 2:
            music.set_volume(0.2)
            music.play(0)
            a = False

        if width_line >= 1800:
            time.sleep(1)
            width_line += 10
            time.sleep(0.5)
            running = False
        width_line += 1
        if schet == 100:
            if text_loading == "Загрузка...":
                text_loading = "Загрузка"
            else:
                text_loading = text_loading + '.'
            schet = 0
        schet += 1
        apple_x -= 2

        text_hill = font.render("+20 HP", True, (0, 250, 0))
        text_hill_x = 1920 // 2
        text_hill_y = schet_2
        text_hill_w = text_hill.get_width()
        text_hill_h = text_hill.get_height()

        if a == False and schet_2 != 400:
            schet_2 += 2
        if schet_2 >= 400:
            text_ok = font.render("НЕ СДАВАЙСЯ", True, (0, 200, 0))
            text_ok_x = 1920 // 2 - 50
            text_ok_y = 800
            text_ok_w = text_ok.get_width()
            text_ok_h = text_ok.get_height()
            screen.blit(text_ok, (text_ok_x, text_ok_y))
        if schet_3 <= 500:
            screen.blit(text_hill, (text_hill_x, schet_2))
        if schet_2 == 400:
            schet_3 += 2
        pygame.display.flip()