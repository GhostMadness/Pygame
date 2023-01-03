import pygame
import pytmx
from location_1 import Stop

class Heroy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        infoObject = pygame.display.Info()
        self.image= pygame.image.load('SPRITE\гг.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = infoObject.current_h // 2
        self.rect.right = infoObject.current_w // 2
    
    def update(self):
        pass
    
    def top(self):
        global y
        self.image= pygame.image.load('SPRITE\гг.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.y -= 10
    
    def botton(self):
        global y
        self.image= pygame.image.load('SPRITE\гг.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.y += 10

    
    def right(self):
        global x
        self.image = pygame.image.load('SPRITE\гг_2.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.x += 10

    
    def left(self):
        global x
        self.image = pygame.image.load('SPRITE\гг_1.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.x -= 10


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Phantom")
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    tmxdata_one = pytmx.load_pygame("location_house\\location_3.tmx")
    image_1 = pygame.image.load("location_house\location_3.png")
    image_2 = pygame.image.load("location_house\location_3_house.png")
    clock = pygame.time.Clock()

    gg = Heroy()

    screen.fill((0, 0, 0))
    for i in range(60):
        for j in range(34):
            image = tmxdata_one.get_tile_image(i, j, 0)
            screen.blit(image, (0 + i * 32, 0 + j * 32))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            gg.right()
        if key[pygame.K_a]:
            gg.left()
        if key[pygame.K_w]:
            gg.top()
        if key[pygame.K_s]:
            gg.botton()
        screen.blit(image_1, (0, 0))
        screen.blit(image_2, (0, 0))
        screen.blit(gg.image, gg.rect)
        pygame.display.flip()
        clock.tick(60)
pygame.quit()