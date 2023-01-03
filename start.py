import pygame
import random
import time

class War(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__(all_wars)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(cell.rect.left + 1, cell.rect.right - 25)
        self.rect.y = cell.rect.top
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        global number
        self.rect = self.rect.move(random.randrange(-3, 5), 1)
        if self.rect.centery >= cell.rect.bottom - 5 or self.rect.centerx >= cell.rect.right - 5 or self.rect.centerx <= cell.rect.left + 5:
            self.kill()
        if pygame.sprite.collide_mask(self, heart):
            number -= 1
            hp(number) 
            self.kill()


class Heart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('SPRITE\сердце-export.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = cell.rect.center
        self.mask = pygame.mask.from_surface(self.image)
    
    def right(self):
        if self.rect.centerx + (max(self.mask.outline(), key=lambda x: x[0])[0] // 2) < cell.rect.right:
            self.rect = self.rect.move(3, 0)

    def left(self):
        if self.rect.centerx - (max(self.mask.outline(), key=lambda x: x[0])[0] // 2) > cell.rect.left:
            self.rect = self.rect.move(-3, 0)

    def top(self):
        if self.rect.centery - (max(self.mask.outline(), key=lambda x: x[1])[0] // 2) > cell.rect.top:
            self.rect = self.rect.move(0, -3)
    
    def bottom(self):
        if self.rect.centery + (max(self.mask.outline(), key=lambda x: x[1])[0] // 2) + 10 < cell.rect.bottom:
            self.rect= self.rect.move(0, 3)
    
    def update(self):
        if number == 0:
            self.image = pygame.image.load('SPRITE\сердце-export.png')
            self.rect = self.image.get_rect()
            self.rect.center = cell.rect.center
            self.rect.x -= 10
            self.rect.y -= 10
            screen.blit(cell.image, cell.rect)
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(1)
            self.image = pygame.image.load('SPRITE\сердце_2-export.png')
            self.rect.center = cell.rect.center
            screen.blit(cell.image, cell.rect)
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(1)
            self.image = pygame.image.load('SPRITE\сердце_3-export.png')
            self.rect.center = cell.rect.center
            screen.blit(cell.image, cell.rect)
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(1)
            self.image = pygame.image.load('SPRITE\сердце_4-export.png')
            self.rect.center = cell.rect.center
            screen.blit(cell.image, cell.rect)
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(1)
            self.image = pygame.image.load('SPRITE\сердце_5-export.png')
            self.rect.center = cell.rect.center
            screen.blit(cell.image, cell.rect)
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(1)
    
    def update_yes(self):
        if number == 0:
            return True
        return False


def hp(number):
    text = font.render(f"{number} HP", True, (200, 255, 100))
    text_x = cell.rect.right + 20
    text_y = cell.rect.bottom - text.get_height()
    screen.fill((0, 0, 0), pygame.Rect(text_x, text_y, text.get_width() + 10, text.get_height()))
    screen.blit(text, (text_x, text_y))


class Cell(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('SPRITE\для update-export.png')  
        self.rect = self.image.get_rect()
        self.rect.top = 400
        self.rect.left = 750     


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1920, 1080
    
    screen = pygame.display.set_mode(size)
    
    screen.fill((0, 0, 0))
    
    image1 = pygame.image.load('SPRITE\Hide_1.png')
    
    screen.blit(image1, (800, 100))
    pygame.display.flip()
    
    cell = Cell()
    
    font = pygame.font.Font(None, 50)
    text = font.render("АТАКА", True, (100, 255, 100))
    text_x = 500
    text_y = cell.rect.bottom + 20
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    ataka = pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                        text_w + 20, text_h + 20), 1)
    
    text = font.render("ДЕЙСТВИЕ", True, (100, 255, 100))
    text_x = text_x + text_w + 50
    text_y = cell.rect.bottom + 20
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    deistvie = pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                        text_w + 20, text_h + 20), 1)
    
    text = font.render("ИНВЕНТАРЬ", True, (100, 255, 100))
    text_x = text_x + text_w + 50
    text_y = cell.rect.bottom + 20
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    inventar = pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                        text_w + 20, text_h + 20), 1)
    
    text = font.render("ПОЩАДА", True, (100, 255, 100))
    text_x = text_x + text_w + 50
    text_y = cell.rect.bottom + 20
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    posada = pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                        text_w + 20, text_h + 20), 1)
    
    number = 20
    
    hp(number)
    
    heart = Heart()
    
    all_wars = pygame.sprite.Group()
    
    clock = pygame.time.Clock()
    
    running = True
    flag = True
    q = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ataka[0] < event.pos[0] < ataka[0] + ataka[2] and ataka[1] < event.pos[1] < ataka[1] + ataka[3]:
                    print(1)
                elif deistvie[0] < event.pos[0] < deistvie[0] + deistvie[2] and deistvie[1] < event.pos[1] < deistvie[1] + deistvie[3]:
                    print(2)
                elif inventar[0] < event.pos[0] < inventar[0] + inventar[2] and inventar[1] < event.pos[1] < inventar[1] + inventar[3]:
                    print(3)
                elif posada[0] < event.pos[0] < posada[0] + posada[2] and posada[1] < event.pos[1] < posada[1] + posada[3]:
                    print(4)
        if not heart.update_yes():
            if q % 20 == 0:
                War('SPRITE\war_1.png')
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
            all_wars.draw(screen)
            all_wars.update()
            screen.blit(heart.image, heart.rect)
            pygame.display.update()
            clock.tick(100)
            q += 1
        elif flag:
            heart.update()
            flag = False
    pygame.quit()