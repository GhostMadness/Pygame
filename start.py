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
        self.rect = self.rect.move(random.randrange(-5, 5), 1)
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
        self.image_load = self.image
    
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
            music = pygame.mixer.Sound('MUSIC\DOUBLE\DEATH.mp3')
            music.set_volume(0.2)
            music.play(-1)
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
            music.stop()
    
    def update_yes(self):
        if number == 0:
            return True
        return False
    
    def death(self):
        self.image = pygame.Surface((0, 0))
        
    def live(self):
        self.image = self.image_load


def hp(number):
    text = font.render(f"{number} HP", True, (200, 255, 100))
    text_x = 1130 + 20
    text_y = 780 - text.get_height()
    screen.fill((0, 0, 0), pygame.Rect(text_x, text_y, text.get_width() + 100, text.get_height()))
    screen.blit(text, (text_x, text_y))


def fight():
    pass

class Deistvie:
    def __init__(self):
        pass


class Inventar:
    def __init__(self):
        pass


class Posada:
    def __init__(self):
        pass


class Dialog:
    def __init__(self):
        pass


class Cell(pygame.sprite.Sprite):
    def __init__(self, filename, top, left):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.top = top
        self.rect.left = left     


def war_1():
    global w
    War('SPRITE\war_1.png')
    w += 1


def war_2():
    global w
    War('SPRITE\war_2.png')
    w += 1


def dialog_1():
    global cell
    cell = Cell('SPRITE\для диалога.png', 400, 600)
    font = pygame.font.Font(None, 50)
    text = font.render("Призрак не выражает эмоций", True, (100, 150, 100))
    text_x = cell.rect.x + 10
    text_y = cell.rect.y + 10
    screen.blit(cell.image, cell.rect)
    screen.blit(text, (text_x, text_y))


def dialog_2():
    global cell
    font = pygame.font.Font(None, 50)
    text = font.render("Призрак о чём-то думает", True, (100, 150, 100))
    text_x = cell.rect.x + 10
    text_y = cell.rect.y + 10
    screen.blit(cell.image, cell.rect)
    screen.blit(text, (text_x, text_y))

def dialog_3():
    global cell
    font = pygame.font.Font(None, 50)
    text = font.render("Призрак не понимает, что он тут делает", True, (100, 150, 100))
    text_x = cell.rect.x + 10
    text_y = cell.rect.y + 10
    screen.blit(cell.image, cell.rect)
    screen.blit(text, (text_x, text_y))

def war_3():
    pass


wars = {'dialog_1': dialog_1, 'war_1': war_1, 'dialog_2': dialog_2, 'war_2': war_2, 'dialog_3': dialog_3, 'war_3': war_3}
file_wars = open('wars.txt').readlines()
w = 0


def one():
    global running
    global q
    global s
    global heart
    global flag
    global b
    global cell
    if not heart.update_yes():
        if q % 20 == 0:
            wars[file_wars[s].rstrip()]()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            heart.right()
        elif keys[pygame.K_a]:
            heart.left()
        elif keys[pygame.K_w]:
            heart.top()
        elif keys[pygame.K_s]:
            heart.bottom()
        q += 1
        if b == 1:
            screen.blit(cell.image, cell.rect)
        all_wars.draw(screen)
        all_wars.update()
        screen.blit(heart.image, heart.rect)
        pygame.display.flip()
        if w == 0:
            s = 0
        elif w < 100 and flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, cell.rect.bottom - cell.rect.y))
            cell = Cell('SPRITE\для update-export.png', 400, 750)
            heart.rect.center = cell.rect.center
            heart.live()
            s = 1
            flag = False
            b = 1
        elif w == 100 and not flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, cell.rect.bottom - cell.rect.y))
            cell = Cell('SPRITE\для диалога.png', 400, 600)
            heart.death()
            s = 2
            b = 0
            flag = True
        elif 100 < w < 200 and flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, cell.rect.bottom - cell.rect.y))
            cell = Cell('SPRITE\для update-export.png', 400, 750)
            heart.rect.center = cell.rect.center
            heart.live()
            s = 3
            b = 1
            flag = False
        elif w == 200 and not flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, cell.rect.bottom - cell.rect.y))
            cell = Cell('SPRITE\для диалога.png', 400, 600)
            heart.death()
            s = 4
            b = 0
            flag = True
        hp(number)
    else:
        heart.update()
        running = False


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1920, 1080
    
    screen = pygame.display.set_mode(size)
    
    screen.fill((0, 0, 0))
    
    image1 = pygame.image.load('SPRITE\Hide_1.png')
    
    s = 0
    b = 0
    
    flag = True
    
    screen.blit(image1, (800, 100))
    pygame.display.flip()
    
    font = pygame.font.Font(None, 50)
    text = font.render("АТАКА", True, (100, 255, 100))
    text_x = 500
    text_y = 800
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    ataka = pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                        text_w + 20, text_h + 20), 1)
    
    text = font.render("ДЕЙСТВИЕ", True, (100, 255, 100))
    text_x = text_x + text_w + 50
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    deistvie = pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                        text_w + 20, text_h + 20), 1)
    
    text = font.render("ИНВЕНТАРЬ", True, (100, 255, 100))
    text_x = text_x + text_w + 50
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    inventar = pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                        text_w + 20, text_h + 20), 1)
    
    text = font.render("ПОЩАДА", True, (100, 255, 100))
    text_x = text_x + text_w + 50
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    posada = pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                        text_w + 20, text_h + 20), 1)
    
    number = 20
    
    all_wars = pygame.sprite.Group()
    
    clock = pygame.time.Clock()
    
    running = True
    q = 0
    flag = True
    
    hp(number)
    
    dialog_1()
    
    heart = Heart()
    heart.death()
    
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    w += 1
        one()
    pygame.quit()