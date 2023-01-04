import pygame
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

        self.image_grass_bottom = pygame.image.load("location_house\sprite_collide\ottom_grass.png")
        self.image_grass_right = pygame.image.load("location_house\sprite_collide\ght_grass.png")
        
    
    def update(self):
        pass
    
    def top(self):
        global y
        self.image= pygame.image.load('SPRITE\гг.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        if not pygame.sprite.spritecollideany(self, bottom_sprites):
            self.rect.y -= 6
    
    def botton(self):
        global y
        self.image= pygame.image.load('SPRITE\гг.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.y += 6

    
    def right(self):
        global x
        self.image = pygame.image.load('SPRITE\гг_2.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.x += 6

    
    def left(self):
        global x
        self.image = pygame.image.load('SPRITE\гг_1.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.x -= 6

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
    image_background = pygame.image.load("location_4\esult_sprite\map.png")
    image_1 = pygame.image.load("location_4\esult_sprite\house.png")
    image_2 = pygame.image.load("location_4\esult_sprite\other.png")
    sc1 = pygame.Surface((1920, 1080))
    sc1.blit(image_background, (0, 0))
    sc1.blit(image_2, (0, 0))
    sc1.blit(image_1, (0, 0))

    bottom_sprites = pygame.sprite.Group()
    bottom_sprites.add(Stop("location_4\esult_sprite\house_2.png", (0, 0)))

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
        pygame.display.flip()
        clock.tick(60)
pygame.quit()