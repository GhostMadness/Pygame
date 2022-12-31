import pygame
import pytmx

class Heroy(pygame.sprite.Sprite):
    def __init__(self):
        super()
        self.image= pygame.image.load('SPRITE\гг.png')
        self.image = pygame.transform.scale(self.image, (250, 250))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = infoObject.current_h // 2
        self.rect.right = infoObject.current_w // 2
    
    def update(self):
        pass
    
    def top(self):
        global y
        self.image= pygame.image.load('SPRITE\гг.png')
        self.image = pygame.transform.scale(self.image, (250, 250))
        print(pygame.sprite.collide_mask(self, dc1))
        if not pygame.sprite.collide_mask(self, dc1):
            y += 3
    
    def botton(self):
        global y
        self.image= pygame.image.load('SPRITE\гг.png')
        self.image = pygame.transform.scale(self.image, (250, 250))
        y -= 3
    
    def right(self):
        global x
        self.image = pygame.image.load('SPRITE\гг_2.png')
        self.image = pygame.transform.scale(self.image, (250, 250))
        x -= 3
    
    def left(self):
        global x
        self.image = pygame.image.load('SPRITE\гг_1.png')
        self.image = pygame.transform.scale(self.image, (250, 250))
        x += 3


class Stop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('location_1.png'), (infoObject.current_w, infoObject.current_h))
        self.rect= self.image.get_rect()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Локация 1")
    infoObject = pygame.display.Info()
    screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
    screen.fill((0, 0, 0))
    tmxdata = pytmx.load_pygame("location_6432.tmx")
    gg = Heroy()
    clock = pygame.time.Clock()
    
    sc1 = pygame.Surface((2048, 1024))
    
    dc1 =pygame.sprite.Sprite()
    dc1.image = 
    dc1.rect = dc1.image.get_rect()
    dc1. = pygame.mask.from_surface(dc1.image)
    
    for i in range(64):
        for j in range(32):
            image = tmxdata.get_tile_image(i, j, 0)
            sc1.blit(image, (0 + i * 32, 0 + j * 32))
            pygame.display.flip()
    sc1 = pygame.transform.rotozoom(sc1, 0, 1)
    running = True
    x, y = 0, 0
    
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
        screen.blit(dc1.image, (x, y))
        # screen.blit(sc1, (x, y))
        screen.blit(gg.image, gg.rect)
        pygame.display.flip()
        clock.tick(200)
    pygame.quit()