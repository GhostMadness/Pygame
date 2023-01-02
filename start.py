import pygame

class War(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Heart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('SPRITE\сердце-export.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = cell.rect.center
    
    def right(self):
        if self.rect.right <= cell.rect.right:
            self.rect = self.rect.move(3, 0)

    def left(self):
        if self.rect.left <= cell.rect.left:
            self.rect = self.rect.move(-3, 0)

    def top(self):
        if self.rect.top <= cell.rect.top:
            self.rect = self.rect.move(0, -3)
    
    def bottom(self):
        if self.rect.bottom <= cell.rect.bottom:
            self.rect= self.rect.move(0, 3)


class Cell(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('SPRITE\для update-export.png')  
        self.rect = self.image.get_rect()
        self.rect.top = 500
        self.rect.left = 750     

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1920, 1080
    
    screen = pygame.display.set_mode(size)
    
    screen.fill((0, 0, 0))
    
    image1 = pygame.image.load('SPRITE\Hide_1.png')
    
    screen.blit(image1, (800, 200))
    pygame.display.flip()
    
    cell = Cell()
    
    screen.blit(cell.image, cell.rect)
    pygame.display.flip()
    
    heart = Heart()
    
    screen.blit(heart.image, heart.rect)
    pygame.display.update()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            heart.right()
        elif keys[pygame.K_a]:
            heart.left()
        elif keys[pygame.K_w]:
            heart.top()
        elif keys[pygame.K_s]:
            heart.bottom()
        screen.blit(cell.image, cell.rect)
        screen.blit(heart.image, heart.rect)
        pygame.display.update()
    
    pygame.quit()