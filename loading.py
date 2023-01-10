import pygame
import random
import time
# UTF-8


if __name__ == "__main__":
    global image_loading, angle
    pygame.init()
    pygame.display.set_caption("Phantom")
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    image_loading = pygame.image.load("SPRITE\BOMB_ENEMY.png")
    angle = 0
    running = True
    width_line = 0
    text_loading = "Загрузка"
    schet = 0
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

        pos_x = random.randint(1920 // 2 - 10, 1920 // 2 + 10)
        screen.blit(image_loading, (pos_x - 50, 1080 // 2 - 50))
        pygame.draw.rect(screen, (255, 255, 255), (51, 887, width_line, 50))
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
        pygame.display.flip()