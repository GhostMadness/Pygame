import pygame
import time
from start import screen, start_fn

class Heroy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image= pygame.image.load('SPRITE\гг.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.bottom = 600
            self.rect.right = 400
        
        def update(self):
            pass
        
        def top(self):
            global y
            self.image= pygame.image.load('SPRITE\гг.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 100))
            if not pygame.sprite.spritecollideany(self, top_sprites):
                self.rect.y -= 5
        
        def botton(self):
            global y
            self.image= pygame.image.load('SPRITE\гг.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 100))
            if not pygame.sprite.spritecollideany(self, bottom_sprites):
                self.rect.y += 5
        
        def right(self):
            global x
            self.image = pygame.image.load('SPRITE\гг_2.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 100))
            if not pygame.sprite.spritecollideany(self, right_sprites):
                self.rect.x += 5
        
        def left(self):
            global x
            self.image = pygame.image.load('SPRITE\гг_1.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 100))
            if not pygame.sprite.spritecollideany(self, left_sprites):
                self.rect.x -= 5

class Stop(pygame.sprite.Sprite):
        def __init__(self, filename, coords, i):
            super().__init__()
            infoObject = pygame.display.Info()
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
        infoObject = pygame.display.Info()
        self.image = pygame.image.load('SPRITE\Shiza_01.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = infoObject.current_h // 3 * 2 + 250
        self.rect.right = infoObject.current_w // 6 - 60
        
    def update(self):
        pass

class Stop_local_2(pygame.sprite.Sprite):
    def __init__(self, filename, coord):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]

if __name__ == '__main__':
    pygame.init()
    running = True
    x, y = 0, 0
    pygame.display.set_caption("Phantom")
    infoObject = pygame.display.Info()
    width, height = 1920, 1080
    screen.fill((0, 0, 0))

    music = pygame.mixer.Sound('MUSIC\DOUBLE\location_1.mp3')

    top_sprites = pygame.sprite.Group()
    bottom_sprites = pygame.sprite.Group()
    right_sprites = pygame.sprite.Group()
    left_sprites = pygame.sprite.Group()

    left_sprites.add(Stop('SPRITE\location_1c0.png', (-50, 0), 'l'))
    top_sprites.add(Stop('SPRITE\location_1c1.png', (0, 50), 't'))
    bottom_sprites.add(Stop('SPRITE\location_1c2.png', (0, infoObject.current_h // 3 * 2 + 70), 'b'))

    image_background = pygame.image.load("location_4\esult_sprite\map.png")
    image_1 = pygame.image.load("location_4\esult_sprite\house.png")
    image_2 = pygame.image.load("location_4\esult_sprite\other.png")
    image_sprite = pygame.image.load("SPRITE\VIXOD_LOC.png")

    music.set_volume(0.2)
    music.play(-1)

    gg = Heroy()

    sh1 = Shiza()

    ferowguib = False
    sdegfoin = True

    clock = pygame.time.Clock()

    img = pygame.transform.scale(pygame.image.load("location_1\location_1.png").convert_alpha(), (2048, 1024))

    sc1 = pygame.Surface((2048, 1024))

    top_sprites.draw(screen)
    bottom_sprites.draw(screen)
    right_sprites.draw(screen)
    left_sprites.draw(screen)

    other_sprite = pygame.sprite.Group()
    other_sprite.add(Stop_local_2("SPRITE\VIXOD_LOC.png", (1920 // 2, 1080 // 2)))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                print(event.pos)
            if ferowguib:
                start_fn(event)

        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            gg.right()
        if key[pygame.K_a]:
            gg.left()
        if key[pygame.K_w]:
            gg.top()
        if key[pygame.K_s]:
            gg.botton()
        screen.blit(img, (x, y))
        screen.blit(gg.image, gg.rect)
        screen.blit(sh1.image, sh1.rect)
        if pygame.sprite.spritecollideany(gg, other_sprite) and sdegfoin:
            music.stop()
            start_fn(event)
            sdegfoin = False
            music.play(-1)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
