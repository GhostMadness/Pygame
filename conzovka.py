import pygame

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Phantom")
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)

    image_player = pygame.image.load("SPRITE\гг.png")
    image_shiza = pygame.image.load("SPRITE\Megashiza.png")
    image_player = pygame.transform.scale(image_player, (250, 250))
    image_shiza = pygame.transform.scale(image_shiza, (250, 250))

    font = pygame.font.Font(None, 50)
    text = font.render("СПАСИБО ЗА ПРОХОЖДЕНИЕ", True, (230, 230, 230))
    text_x = 1920 // 2 - 50 - 200
    text_y = 1080 // 2 - 300

    x = -400

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                print(event.pos)
        screen.fill((0, 0, 0))
        screen.blit(text, (text_x, text_y))
        screen.blit(image_player, (x, 1080 // 2))
        screen.blit(image_shiza, (1920 // 2, 1080 // 2))
        if x <= 800:
            x += 1
        elif x >= 800:
            image_shiza = pygame.transform.scale(image_shiza, (250, 50))
        pygame.display.flip()
pygame.quit()