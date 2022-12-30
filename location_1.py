import pygame
import pytmx

class Heroy(pygame.sprite.Sprite):
    def __init__(self):
        super()
        self.image= pygame.image.load('SPRITE\гг.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 200
    
    def update(self):
        pass
    
    def top(self):
        self.image= pygame.image.load('SPRITE\гг.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.rect.move(0, -3)
    
    def botton(self):
        self.image= pygame.image.load('SPRITE\гг.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.rect.move(0, 3)
    
    def right(self):
        self.image = pygame.image.load('SPRITE\гг_2.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.rect.move(3, 0)
    
    def left(self):
        self.image = pygame.image.load('SPRITE\гг_1.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.rect.move(-3, 0)
        

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Локация 1")
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen.fill((0, 0, 0))
    tmxdata = pytmx.load_pygame("location_1.tmx")
    gg = Heroy()
    clock = pygame.time.Clock()
    
    sc1 = pygame.Surface((800, 600), pygame.FULLSCREEN)
    
    for i in range(28):
        for j in range(20):
            image = tmxdata.get_tile_image(i, j, 0)
            sc1.blit(image, (0 + i * 32, 0 + j * 32))
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
        screen.blit(sc1, (0, 0))
        screen.blit(gg.image, gg.rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()