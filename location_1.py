import pygame
import pytmx

class Heroy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
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
        if not pygame.sprite.spritecollideany(self, top_sprites):
            self.rect.y -= 10
    
    def botton(self):
        global y
        self.image= pygame.image.load('SPRITE\гг.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        if not pygame.sprite.spritecollideany(self, bottom_sprites):
            self.rect.y += 10
    
    def right(self):
        global x
        self.image = pygame.image.load('SPRITE\гг_2.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        if not pygame.sprite.spritecollideany(self, right_sprites):
            self.rect.x += 10
    
    def left(self):
        global x
        self.image = pygame.image.load('SPRITE\гг_1.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        if not pygame.sprite.spritecollideany(self, left_sprites):
            self.rect.x -= 10


class Stop(pygame.sprite.Sprite):
    def __init__(self, filename, coords, i):
        super().__init__()
        if i == 'l':
            self.image = pygame.transform.scale(pygame.image.load(filename), (infoObject.current_w // 6 - 60, infoObject.current_h))
        elif i == 't':
            self.image = pygame.transform.scale(pygame.image.load(filename), (infoObject.current_w, infoObject.current_h // 3))
        elif i == 'b':
            self.image = pygame.transform.scale(pygame.image.load(filename), (infoObject.current_w, infoObject.current_h // 3))
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]


class Shiza(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('SPRITE\Shiza_01')
        self.rect = self.image.get_rect()
        
    def update(self):
        pass


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Локация 1")
    infoObject = pygame.display.Info()
    screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
    screen.fill((0, 0, 0))
    tmxdata = pytmx.load_pygame("location_6432.tmx")
    
    top_sprites = pygame.sprite.Group()
    bottom_sprites = pygame.sprite.Group()
    right_sprites = pygame.sprite.Group()
    left_sprites = pygame.sprite.Group()
    
    left_sprites.add(Stop('location_1c0.png', (0, 0), 'l'))
    top_sprites.add(Stop('location_1c1.png', (0, -120), 't'))
    bottom_sprites.add(Stop('location_1c2.png', (0, infoObject.current_h // 3 * 2 + 40), 'b'))
    
    gg = Heroy()
    
    clock = pygame.time.Clock()
    
    sc1 = pygame.Surface((2048, 1024))
    
    for i in range(64):
        for j in range(32):
            image = tmxdata.get_tile_image(i, j, 0)
            sc1.blit(image, (0 + i * 32, 0 + j * 32))
            pygame.display.flip()
    # sc1 = pygame.transform.rotozoom(sc1, 0, 1)
    running = True
    x, y = 0, 0
    
    top_sprites.draw(screen)
    bottom_sprites.draw(screen)
    right_sprites.draw(screen)
    left_sprites.draw(screen)

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
        screen.blit(sc1, (x, y))
        screen.blit(gg.image, gg.rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()