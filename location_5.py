import pygame

class Heroy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        infoObject = pygame.display.Info()
        self.image= pygame.image.load('SPRITE\гг.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = 570
        self.rect.right = 100

        self.image_grass_bottom = pygame.image.load("location_house\sprite_collide\ottom_grass.png")
        self.image_grass_right = pygame.image.load("location_house\sprite_collide\ght_grass.png")
        
    
    def update(self):
        pass
    
    def top(self):
        global y
        self.image= pygame.image.load('SPRITE\гг.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        if not pygame.sprite.spritecollideany(self, bottom_sprite):
            self.rect.y -= 5
    
    def botton(self):
        global y
        self.image= pygame.image.load('SPRITE\гг.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.y += 5

    
    def right(self):
        global x
        self.image = pygame.image.load('SPRITE\гг_2.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        if not pygame.sprite.spritecollideany(self, right_sprite):
            self.rect.x += 5

    
    def left(self):
        global x
        self.image = pygame.image.load('SPRITE\гг_1.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.x -= 5

class Stop(pygame.sprite.Sprite):
    def __init__(self, filename, coord):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]



if __name__ == '__main__':
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
    bottom_sprite.add(Stop("location_5_men\RESULT\iblioteka_bottom_collide.png", (1542, 266)))
    right_sprite.add(Stop("location_5_men\RESULT\iblioteka_right_collide.png", (1542, 8)))

    music = pygame.mixer.Sound('MUSIC\FIRST\LOCATION_3_1.mp3')

    clock = pygame.time.Clock()

    gg = Heroy()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                print(event.pos)
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

        music.set_volume(0.2)
        music.play(-1)
                
        pygame.display.flip()
        clock.tick(60)
pygame.quit()