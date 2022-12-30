import pygame
import pytmx

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Локация 1")
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    tmxdata = pytmx.load_pygame("loc_1.tmx")
    for i in range(28):
        for j in range(20):
            image = tmxdata.get_tile_image(i, j, 0)
            screen.blit(image, (0 + i * 30, 0 + j * 30))
            pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False