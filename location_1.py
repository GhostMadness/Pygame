import pygame
import time
from start import screen, start_fn, Death_fLag
from location_2 import start_dias

location_3 = False
location_2 = False
location_1 = False



class Heroy(pygame.sprite.Sprite):
        def __init__(self, right=None, left=None, bottom=None, top=None, x=600, y=400):
            super().__init__()
            self.image= pygame.image.load('SPRITE\гг.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.bottom = x
            self.rect.right = y

            self.top_sprites = top
            self.bottom_sprites = bottom
            self.right_sprites = right
            self.left_sprites = left

            if self.right_sprites == None:
                self.right_sprites = pygame.sprite.Group()

            if self.left_sprites == None:
                self.left_sprites = pygame.sprite.Group()

            if self.top_sprites == None:
                self.top_sprites = pygame.sprite.Group()
        
        def update(self):
            pass
        
        def top(self):
            global y
            self.image= pygame.image.load('SPRITE\гг.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 100))
            if not pygame.sprite.spritecollideany(self, self.top_sprites):
                self.rect.y -= 5
        
        def botton(self):
            global y
            self.image= pygame.image.load('SPRITE\гг.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 100))
            if not pygame.sprite.spritecollideany(self, self.bottom_sprites):
                self.rect.y += 5
        
        def right(self):
            global x
            self.image = pygame.image.load('SPRITE\гг_2.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 100))
            if not pygame.sprite.spritecollideany(self, self.right_sprites):
                self.rect.x += 5
        
        def left(self):
            global x
            self.image = pygame.image.load('SPRITE\гг_1.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 100))
            if not pygame.sprite.spritecollideany(self, self.left_sprites):
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

class Stop_2(pygame.sprite.Sprite):
    def __init__(self, filename, coord):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]

def start_location_4():
    if __name__ == '__main__':
        global location_3
        pygame.init()
        pygame.display.set_caption("Phantom")
        size = width, height = 1920, 1080
        screen = pygame.display.set_mode(size)

        image_background = pygame.image.load("location_5_men\RESULT\location_5_man.png")
        image_1 = pygame.image.load("location_5_men\RESULT\iblioteka.png")
        image_3 = pygame.image.load("location_5_men\RESULT\cover.png")
        image_4 = pygame.image.load("location_5_men\RESULT\oxes.png")
        image_5 = pygame.image.load("location_5_men\RESULT\object.png")

        sc1 = pygame.Surface((1920, 1080))
        sc1.blit(image_background, (0, 0))
        sc1.blit(image_1, (0, 0))
        sc1.blit(image_3, (0, 0))
        sc1.blit(image_4, (0, 0))
        sc1.blit(image_5, (0, 0))

        bottom_sprite = pygame.sprite.Group()
        right_sprite = pygame.sprite.Group()
        left_sprites = pygame.sprite.Group()
        top_sprites = pygame.sprite.Group()
        bottom_sprite.add(Stop_2("location_5_men\RESULT\iblioteka_bottom_collide.png", (1542, 220)))
        right_sprite.add(Stop_2("location_5_men\RESULT\iblioteka_right_collide.png", (1570, 8)))
        right_sprite.add(Stop_2("location_5_men\RESULT\iblioteka_other.png", (1670, 479)))
        left_sprites.add(Stop_2("location_5_men\RESULT\oxes_collide.png", (0, 913)))
        top_sprites.add(Stop_2("location_5_men\RESULT\object_collide.png", (895, 0)))
        #object_collide

        music = pygame.mixer.Sound('MUSIC\FIRST\HOME.mp3')
        music.set_volume(0.2)
        music.play(-1)

        clock = pygame.time.Clock()

        gg_4 = Heroy(bottom=bottom_sprite, right=right_sprite, left=left_sprites, top=top_sprites, x=1050, y=1000)

        other_sprite_exit = pygame.sprite.Group()
        other_sprite_exit.add(Stop_2("SPRITE\VIXOD_LOC.png", (932, 1100)))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    print(event.pos)
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                gg_4.right()
            if key[pygame.K_a]:
                gg_4.left()
            if key[pygame.K_w]:
                gg_4.top()
            if key[pygame.K_s]:
                gg_4.botton()
            screen.blit(sc1, (0, 0))
            screen.blit(gg_4.image, gg_4.rect)

            if pygame.sprite.spritecollideany(gg_4, other_sprite_exit):
                music.stop()
                location_3 = True
                start_location_3()
                    
            pygame.display.flip()
            clock.tick(60)
    pygame.quit()

def start_location_3():
    if __name__ == '__main__':
        global location_2, location_3
        pygame.init()
        pygame.display.set_caption("Phantom")
        size = width, height = 1920, 1080
        screen = pygame.display.set_mode(size)
        image_background = pygame.image.load("location_house\ckground.png")
        image_1 = pygame.image.load("location_house\location_3.png")
        image_2 = pygame.image.load("location_house\location_3_house.png")
        sc1 = pygame.Surface((1920, 1080))
        sc1.blit(image_background, (0, 0))
        sc1.blit(image_2, (0, 0))
        sc1.blit(image_1, (0, 0))

        bottom_sprite = pygame.sprite.Group()
        right_sprite = pygame.sprite.Group()
        bottom_sprite.add(Stop_2("location_house\sprite_collide\ottom_grass.png", (0, 265)))
        right_sprite.add(Stop_2("location_house\sprite_collide\ght_grass.png", (830, 0)))

        music = pygame.mixer.Sound('MUSIC\FIRST\LOCATION_3_1.mp3')
        music.set_volume(0.1)
        music.play(-1)

        clock = pygame.time.Clock()

        gg_3 = Heroy(bottom=bottom_sprite, right=right_sprite, x=550, y=100)
        if location_3:
            gg_3.rect.x = 1230
            gg_3.rect.y = 500
            location_3 = False

        other_sprite_2 = pygame.sprite.Group()
        other_sprite_2.add(Stop_2("SPRITE\VIXOD_LOC.png", (1300, 25)))

        other_sprite_exit = pygame.sprite.Group()
        other_sprite_exit.add(Stop_2("SPRITE\VIXOD_LOC.png", (-350, 510)))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    print(event.pos)
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                gg_3.right()
            if key[pygame.K_a]:
                gg_3.left()
            if key[pygame.K_w]:
                gg_3.top()
            if key[pygame.K_s]:
                gg_3.botton()
            screen.blit(sc1, (0, 0))
            screen.blit(gg_3.image, gg_3.rect)

            if pygame.sprite.spritecollideany(gg_3, other_sprite_2):
                music.stop()
                start_location_4()
            if pygame.sprite.spritecollideany(gg_3, other_sprite_exit):
                music.stop()
                location_2 = True
                start_location_2()

            pygame.display.flip()
            clock.tick(60)
    pygame.quit()

def start_location_2():
    if __name__ == '__main__':
        global location_2, location_1
        pygame.init()
        pygame.display.set_caption("Phantom")
        size = width, height = 1920, 1080
        screen_local_2 = pygame.display.set_mode(size)
        image_background = pygame.image.load("location_4\esult_sprite\map.png")
        image_1 = pygame.image.load("location_4\esult_sprite\house.png")
        image_2 = pygame.image.load("location_4\esult_sprite\other.png")
        sc1 = pygame.Surface((1920, 1080))
        sc1.blit(image_background, (0, 0))
        sc1.blit(image_2, (0, 0))
        sc1.blit(image_1, (0, 0))
        bottom_sprites = pygame.sprite.Group()
        top_sprites = pygame.sprite.Group()
        bottom_sprites.add(Stop_2("location_4\esult_sprite\ground_bottom.png", (0, 716)))
        top_sprites.add(Stop_2("location_4\esult_sprite\house_2.png", (0, 0)))

        music = pygame.mixer.Sound('MUSIC\DOUBLE\location_2.mp3')
        music.set_volume(0.2)
        music.play(-1)

        clock = pygame.time.Clock()

        gg_2 = Heroy(top=top_sprites, bottom=bottom_sprites, x=580, y=70)
        if location_2:
            gg_2.rect.x = 1750
            gg_2.rect.y = 500
            location_2 = False

        other_sprite_2 = pygame.sprite.Group()
        other_sprite_2.add(Stop_2("SPRITE\VIXOD_LOC.png", (1916, 572)))

        other_sprite_exit = pygame.sprite.Group()
        other_sprite_exit.add(Stop_2("SPRITE\VIXOD_LOC.png", (-350, 523)))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    print(event.pos)
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                gg_2.right()
            if key[pygame.K_a]:
                gg_2.left()
            if key[pygame.K_w]:
                gg_2.top()
            if key[pygame.K_s]:
                gg_2.botton()
            screen_local_2.blit(sc1, (0, 0))
            screen_local_2.blit(gg_2.image, gg_2.rect)

            if pygame.sprite.spritecollideany(gg_2, other_sprite_2):
                music.stop()
                start_location_3()
            if pygame.sprite.spritecollideany(gg_2, other_sprite_exit):
                music.stop()
                location_1 = True
                start_location_1()

            pygame.display.flip()
            clock.tick(60)
    pygame.quit()

def start_location_1():
    if __name__ == '__main__':
        global location_1, gg, Death_fLag
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
        gg = Heroy(top=top_sprites, bottom=bottom_sprites, right=right_sprites, left=left_sprites)
        if location_1:
            gg.rect.x = 1800
            gg.rect.y = 572
            location_1 = False
            
        if Death_fLag:
            gg.rect.x = 600
            gg.rect.y = 400
            Death_fLag = False

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
        other_sprite.add(Stop_2("SPRITE\VIXOD_LOC.png", (1920 // 2, 1080 // 2)))

        other_sprite_2 = pygame.sprite.Group()
        other_sprite_2.add(Stop_2("SPRITE\VIXOD_LOC.png", (1916, 572)))


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

            if pygame.sprite.spritecollideany(gg, other_sprite_2):
                music.stop()
                start_location_2()
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
start_location_1()