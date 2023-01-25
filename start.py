import pygame
import random
import time
import sqlite3

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
sc_2 = pygame.display.set_mode((1920, 1080))
Death_fLag = False
go_or_no = False
number = 20
war_now = 1
clock = pygame.time.Clock()
conez = False
what_ahaha = False

def conzovka():
    pygame.init()
    pygame.display.set_caption("Phantom")
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)

    image_player = pygame.image.load("SPRITE\гг.png")
    image_shiza = pygame.image.load("SPRITE\Megashiza.png")
    image_kitten = pygame.image.load("SPRITE\KITTEN.png")
    image_player = pygame.transform.scale(image_player, (250, 250))
    image_shiza = pygame.transform.scale(image_shiza, (250, 250))
    image_kitten = pygame.transform.scale(image_kitten, (150, 100))

    rect = image_kitten.get_rect()

    music_finall_yra = pygame.mixer.Sound("MUSIC\FIRST\FINALL_TITRI.mp3")
    music_finall_yra.set_volume(0.2)
    music_finall_yra.play(-1)

    music_ydar = pygame.mixer.Sound("MUSIC\WHAT\ok.mp3")
    music_ydar.set_volume(0.2)


    color_1 = 0

    font = pygame.font.Font(None, 50)
    text = font.render("СПАСИБО ЗА ПРОХОЖДЕНИЕ", True, (230, 230, 230))
    text_x = 1920 // 2 - 50 - 200
    text_y = 1080 // 2 - 300 + 600

    text_a = font.render("В ГЛАВНЫХ РОЛЯХ:", True, (255, 255, 230))
    text_a_x = 100
    text_a_y = 100

    x = -400
    
    F_Men = True
    chpok = False
    fLaf = False
    y_kitten = -1500

    running = True
    while running:
        text_b = font.render("Артём - Художник, Программист, Геймдизайнер", True, (color_1, 206, 250))
        text_b_x = 100
        text_b_y = 200

        text_c = font.render("Дима - Художник, Программист, Геймдизайнер, Саунд-дизайнер", True, (color_1, 206, 250))
        text_c_x = 100
        text_c_y = 300

        text_d = font.render("Гранат(друг Димочки) - Художник", True, (color_1, 206, 250))
        text_d_x = 100
        text_d_y = 400

        text_f = font.render("Даня(друг Артёмочки) - Художник", True, (color_1, 206, 250))
        text_f_x = 100
        text_f_y = 500

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.K_ESCAPE:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEMOTION:
                print(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect[0] < event.pos[0] < rect[0] + rect[2] and rect[1] < \
                        event.pos[1] < rect[1] + rect[3]:
                    running = False
                    pygame.quit()
        screen.fill((0, 0, 0))
        screen.blit(text, (text_x, text_y))
        screen.blit(text_a, (text_a_x, text_a_y))
        screen.blit(text_b, (text_b_x, text_b_y))
        screen.blit(text_c, (text_c_x, text_c_y))
        screen.blit(text_d, (text_d_x, text_d_y))
        screen.blit(text_f, (text_f_x, text_f_y))

        if x <= 800:
            x += 1
        elif x >= 800 and F_Men:
            image_shiza = pygame.transform.scale(image_shiza, (250, 50))
            F_Men = False
            chpok = True
        if chpok:
            music_ydar.play()
            chpok = False
        if fLaf:
            color_1 -= 1
        else:
            color_1 += 1
        if color_1 == 255:
            fLaf = True
        if color_1 == 0:
                fLaf = False
        if y_kitten <= 20:
            y_kitten += 1
        
        screen.blit(image_player, (x, 1080 // 2))
        screen.blit(image_shiza, (1920 // 2, 1080 // 2))
        screen.blit(image_kitten, (1700, y_kitten))
        pygame.display.flip()

list_sprites_osminog = ['SPRITE\Osminog\Osminog_1.png', 'SPRITE\Osminog\Osminog_2.png', 'SPRITE\Osminog\Osminog_3.png', 'SPRITE\Osminog\Osminog_4.png', 'SPRITE\Osminog\Osminog_5.png',
                        'SPRITE\Osminog\Osminog_6.png', 'SPRITE\Osminog\Osminog_7.png', 'SPRITE\Osminog\Osminog_8.png', 'SPRITE\Osminog\Osminog_9.png', 'SPRITE\Osminog\Osminog_10.png',
                        'SPRITE\Osminog\Osminog_11.png', 'SPRITE\Osminog\Osminog_12.png', 'SPRITE\Osminog\Osminog_13.png', 'SPRITE\Osminog\Osminog_14.png', 'SPRITE\Osminog\Osminog_15.png',
                        'SPRITE\Osminog\Osminog_16.png', 'SPRITE\Osminog\Osminog_17.png', 'SPRITE\Osminog\Osminog_18.png']
list_sprites_crow = ['SPRITE\CROW_1.png', 'SPRITE\CROW_2.png', 'SPRITE\CROW_3.png', 'SPRITE\CROW_4.png']

class BossAtck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_wars)
        self.image = pygame.image.load("final_boss\Atack\cerp.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (270, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = random.randint(50, 400)
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0

    def update(self):
        global number, heart
        self.angle -= 0.2

        loc = self.image.get_rect().center
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.image.get_rect().center = loc
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.x += 7

        if self.rect.x >= 350 or self.rect.y >= 400:
            self.kill()
            return
        if pygame.sprite.collide_mask(self, heart):
            pygame.mixer.music.load('MUSIC\FIRST\ARGH_2.mp3')
            pygame.mixer.music.set_volume(0.2)
            number -= 5
            hp(number)
            self.kill()
            pygame.mixer.music.play(0)


class War(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__(all_wars)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(cell.rect.left + 1, cell.rect.right - 25)
        self.rect.y = cell.rect.top
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        global number
        self.rect = self.rect.move(random.randrange(-5, 6), 1)
        if self.rect.centery >= cell.rect.bottom - 5 or self.rect.centerx >= cell.rect.right - 5 or self.rect.centerx <= cell.rect.left + 5 or b == 0:
            self.kill()
            screen.fill((0, 0, 0), (self.rect.centerx - 6, self.rect.centery -7, 15, 16))
        if pygame.sprite.collide_mask(self, heart):
            pygame.mixer.music.load('MUSIC\FIRST\ARGH_2.mp3')
            pygame.mixer.music.set_volume(0.2)
            number -= 1
            hp(number)
            screen.fill((0, 0, 0), (self.rect.centerx - 6, self.rect.centery -7, 15, 16))
            self.kill()
            pygame.mixer.music.play(0)


class WarTwo(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__(all_wars)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(cell.rect.left + 27, cell.rect.right - 54)
        self.rect.y = random.randrange(cell.rect.top + 27, cell.rect.bottom - 54)
        self.mask = pygame.mask.from_surface(self.image)
        self.p = 0
    
    def update(self):
        global number
        if self.p == 0:
            self.image = pygame.image.load('SPRITE\BOMB_VZRIV.png').convert_alpha()
            self.p = 1
            self.image = pygame.transform.scale(self.image, (52, 52))
            self.mask = pygame.mask.from_surface(self.image)
        else:
            self.kill()
        if self.rect.centery >= cell.rect.bottom - 5 or self.rect.centerx >= cell.rect.right - 5 or self.rect.centerx <= cell.rect.left + 5 or b == 0:
            screen.fill((0, 0, 0), (self.rect.centerx - 27, self.rect.centery - 27, 54, 54))
            self.kill()
        if pygame.sprite.collide_mask(self, heart) and self.p == 1:
            pygame.mixer.music.load('MUSIC\FIRST\ARGH_2.mp3')
            pygame.mixer.music.set_volume(0.2)
            number -= 2
            hp(number)
            screen.fill((0, 0, 0), (self.rect.centerx - 27, self.rect.centery - 27, 54, 54))
            self.kill()
            pygame.mixer.music.play(0)


class WarThree(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__(all_wars)
        self.image = pygame.Surface((120, cell.rect.bottom - cell.rect.y - 20))
        pygame.draw.rect(self.image, (205, 92, 92), (0, 0, 120, cell.rect.bottom - cell.rect.y - 20)) #(205, 92, 92) (240, 128, 128)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(cell.rect.left, cell.rect.right - 120)
        self.rect.y = cell.rect.top + 10
        self.mask = pygame.mask.from_surface(self.image)
        self.p = 0
        self.filename = filename
    
    def update(self):
        global number
        if self.p == 0:
            self.image = pygame.image.load(self.filename).convert_alpha()
            self.image = pygame.transform.scale(self.image, (120, cell.rect.bottom - cell.rect.y - 20))
            self.mask = pygame.mask.from_surface(self.image)
            self.p = 1
        elif self.p == 1:
            self.p = 2
        else:
            screen.fill((0, 0, 0), (self.rect.x, self.rect.y, self.rect.right - self.rect.x, self.rect.bottom - self.rect.y))
            self.kill()
        if self.rect.centery >= cell.rect.bottom - 5 or self.rect.centerx >= cell.rect.right - 5 or self.rect.centerx <= cell.rect.left + 5 or b == 0:
            screen.fill((0, 0, 0), (self.rect.x, self.rect.y, self.rect.right - self.rect.x, self.rect.bottom - self.rect.y))
            self.kill()
        if pygame.sprite.collide_mask(self, heart) and self.p >= 1:
            pygame.mixer.music.load('MUSIC\FIRST\ARGH_2.mp3')
            pygame.mixer.music.set_volume(0.2)
            number -= 3
            hp(number)
            screen.fill((0, 0, 0), (self.rect.x, self.rect.y, self.rect.right - self.rect.x, self.rect.bottom - self.rect.y))
            self.kill()
            pygame.mixer.music.play(0)


class Osminog(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_wars)
        self.image = pygame.image.load(list_sprites_osminog[0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.index = 0
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        global number
        self.index += 1
        screen.fill((0, 0, 0), (self.rect.x, self.rect.y, self.rect.right - self.rect.x, self.rect.bottom - self.rect.y))
        self.image = pygame.image.load(list_sprites_osminog[self.index]).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        if pygame.sprite.collide_mask(self, heart):
            pygame.mixer.music.load('MUSIC\FIRST\ARGH_2.mp3')
            pygame.mixer.music.set_volume(0.2)
            number -= 2
            hp(number)
            pygame.mixer.music.play(0)
        if self.index == 17:
            self.index = 1


class Megashiza(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_wars)
        self.image = pygame.image.load('SPRITE\Megashiza.png').convert_alpha()
        self.im = pygame.image.load('SPRITE\Megashiza.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = -50
        self.x = 50
        
    def update(self):
        if self.rect.right >= 1920:
            self.x = -5
        if self.rect.left <= 0:
            self.x = 5
        self.rect = self.rect.move(self.x, 0)


class BossAtck(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_wars)
        self.image = pygame.image.load('SPRITE\Atk_0.png')
        rotate = random.randrange(0, 360)
        self.image = pygame.transform.rotate(self.image, rotate)
        self.rect = self.image.get_rect()
        print(rotate)
        if rotate < 90:
            self.rect.y = cell.rect.top - (self.rect.bottom - self.rect.y)
            self.rect.x = random.randrange(cell.rect.x, cell.rect.right - (self.rect.right - self.rect.x))
        elif rotate < 180:
            self.rect.y = random.randrange(cell.rect.y, cell.rect.bottom - (self.rect.bottom - self.rect.y))
            self.rect.x = cell.rect.right + (self.rect.right - self.rect.x)
        elif rotate < 270:
            self.rect.y = cell.rect.bottom + (self.rect.bottom - self.rect.y)
            self.rect.x = random.randrange(cell.rect.x, cell.rect.right - (self.rect.right - self.rect.x))
        else:
            self.rect.y = random.randrange(cell.rect.y, cell.rect.bottom - (self.rect.bottom - self.rect.y))
            self.rect.x = cell.rect.left - (self.rect.right - self.rect.x)


class Knopka(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(atak_sprites)
        self.image = pygame.image.load('SPRITE\knopka_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(700, 1000)
        self.rect.y = random.randint(400, 600)
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        if pygame.sprite.collide_mask(self, heart):
            root()
            self.kill()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def root():
    global mg, hp_Hide, war_now, sc1, apple
    image = pygame.image.load('SPRITE\Brevno.png').convert_alpha()
    image1 = image
    rect = mg.rect.left - 100
    
    if war_now >= 3:
        war_now = 1
    else:
        war_now += 1

    for i in range(-90, 90):
        screen.blit(sc1, (0, 0))
        screen.blit(apple,  (1500, 600))
        screen.blit(cell.image, cell.rect)
        screen.blit(heart.image, heart.rect)
        screen.blit(mg.image, mg.rect)
        screen.blit(image1, (rect, 0))
        image1 = pygame.transform.rotate(image, i)
        rect += 2
        pygame.display.flip()
    hp_Hide -= 5


class Heart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('SPRITE\сердце-export.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = cell.rect.center
        self.mask = pygame.mask.from_surface(self.image)
        self.image_load = self.image
    
    def right(self):
        if self.rect.centerx + (max(self.mask.outline(), key=lambda x: x[0])[0] // 2) < cell.rect.right:
            self.rect = self.rect.move(3, 0)

    def left(self):
        if self.rect.centerx - (max(self.mask.outline(), key=lambda x: x[0])[0] // 2) + 10 > cell.rect.left:
            self.rect = self.rect.move(-3, 0)

    def top(self):
        if self.rect.centery - (max(self.mask.outline(), key=lambda x: x[1])[0] // 2) > cell.rect.top:
            self.rect = self.rect.move(0, -3)
    
    def bottom(self):
        if self.rect.centery + (max(self.mask.outline(), key=lambda x: x[1])[0] // 2) + 10 < cell.rect.bottom:
            self.rect= self.rect.move(0, 3)
    
    def update(self):
        global Death_fLag
        pygame.init()
        if number <= 0:
            con = sqlite3.connect('SQL\Bag.db')
            cur = con.cursor()
            res = cur.execute("""update Bag
                                set Count = 0""").fetchall()
            con.commit()
            con.close()
            music_dead = pygame.mixer.Sound('MUSIC\DOUBLE\DEATH.mp3')
            music_dead.set_volume(0.2)

            with open('SETTING_FILES\SETTING.txt') as f:
                text_ms = f.read()
                text_ms = text_ms.split('=')
                if text_ms[0] == "music" and text_ms[2] == 0:
                    music_dead.stop()
                else:
                    music_dead.play(-1)
            
            music_fight.stop()
            self.image = pygame.image.load('SPRITE\сердце-export.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = cell.rect.center
            self.rect.x -= 10
            self.rect.y -= 10
            screen.blit(cell.image, cell.rect)
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.5)
            self.image = pygame.image.load('SPRITE\сердце_2-export.png').convert_alpha()
            self.rect.center = cell.rect.center
            screen.blit(cell.image, cell.rect)
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.5)
            self.image = pygame.image.load('SPRITE\сердце_3-export.png').convert_alpha()
            self.rect.center = cell.rect.center
            screen.blit(cell.image, cell.rect)
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.5)
            self.image = pygame.image.load('SPRITE\сердце_4-export.png').convert_alpha()
            self.rect.center = cell.rect.center
            screen.blit(cell.image, cell.rect)
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.9)
            self.image = pygame.image.load('SPRITE\сердце_5-export.png').convert_alpha()
            self.rect.center = cell.rect.center
            screen.blit(cell.image, cell.rect)
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.5)
            music_dead.stop()
            Death_fLag = True
            if what_ahaha:
                pygame.quit()
        music_dead.stop()
    
    def update_yes(self):
        global music_fight
        if number <= 0:
            return True
        return False
    
    def death(self):
        self.image = pygame.Surface((0, 0))
        
    def live(self):
        self.image = self.image_load


def hp(number):
    font = pygame.font.Font(None, 50)
    text = font.render(f"{number} HP", True, (200, 255, 100))
    text_x = 1130 + 20
    text_y = 780 - text.get_height()
    screen.fill((0, 0, 0), pygame.Rect(text_x, text_y, text.get_width() + 100, text.get_height()))
    screen.blit(text, (text_x, text_y))


def fight():
    global image1
    global hp_Hide
    global texth, text_xh, text_yh
    hp_Hide -= 7
    texth = font.render("-7 HP", True, (255, 100, 100))
    text_xh = 800 + image1.get_rect().right
    text_yh = 100 + image1.get_rect().top
    screen.fill((0, 0, 0), pygame.Rect(text_xh, text_yh, texth.get_width() + 100, texth.get_height()))
    screen.blit(texth, (text_xh, text_yh))


def bag():
    global w
    global number
    con = sqlite3.connect('SQL\Bag.db')
    cur = con.cursor()
    res = cur.execute("""select Object from Bag where Count > 0""").fetchall()
    if res:
        res = cur.execute("""update Bag
                            set Count = Count - 1
                            where Object = 'Яблоко'""").fetchall()
        w += 1
        number += 5
    con.commit()
    con.close()
        

def hope():
    global image1
    global hp_Hide
    global texth, text_xh, text_yh
    hp_Hide += 5
    texth = myfont.render("我原谅你", True, (100, 255, 100))
    text_xh = 800 + image1.get_rect().right
    text_yh = 100 + image1.get_rect().top
    screen.fill((0, 0, 0), pygame.Rect(text_xh, text_yh, texth.get_width() + 100, texth.get_height()))
    screen.blit(texth, (text_xh, text_yh))


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
    WarThree('SPRITE\war_2.png')
    w += 11


def dialog_1():
    global cell
    global for_text
    cell = Cell('SPRITE\для_диалога.png', 400, 600)
    screen.blit(cell.image, cell.rect)
    for i, obj in enumerate(file_dialog[for_text].split('N')):
        font = pygame.font.Font(None, 50)
        text = font.render(obj, True, (100, 150, 100))
        text_x = cell.rect.x + 10
        text_y = cell.rect.y + 10 + text.get_height() * i
        screen.blit(text, (text_x, text_y))


def war_3():
    pass


def war_4():
    global w
    WarTwo('SPRITE\BOMB_ATACK.png')
    w += 1


def war_0():
    global w
    w += 1
    all_wars.update()
    all_wars.draw(screen)


wars = {'dialog_1': dialog_1, 'war_1': war_1, 'war_2': war_2, 'war_3': war_3, 'war_4': war_4, 'war_0': war_0}
file_wars = open('wars.txt').readlines()
file_dialog = open('dialog.txt', encoding='utf8').readlines()
w = 0


def one(sorce, react, for_text_beta):
    global running
    global q
    global s
    global heart
    global flag
    global b
    global cell
    global Fight
    global texth
    global text_yh
    global text_xh
    global w, Death_fLag, for_text
    if not heart.update_yes():
        if w == 0:
            cell = Cell('SPRITE\для_диалога.png', 400, 600)
            for_text = for_text_beta
            s = sorce
            Fight = False
        elif w < 100 and flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для update-export.png', 400, 750)
            heart.rect.center = cell.rect.center
            heart.live()
            s += 1
            flag = False
            Fight = True
            b = 1
        elif w == 100 and not flag:
            if type(texth) != str:
                screen.fill((0, 0, 0), pygame.Rect(text_xh, text_yh, texth.get_width() + 100, texth.get_height()))
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для_диалога.png', 400, 600)
            heart.death()
            s += 1
            b = 0
            flag = True
            Fight = False
            for_text += 1
        elif 100 < w < 200 and flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для update-export.png', 400, 750)
            heart.rect.center = cell.rect.center
            heart.live()
            s += 1
            b = 1
            flag = False
            Fight = True
        elif w == 200 and not flag:
            if type(texth) != str:
                screen.fill((0, 0, 0), pygame.Rect(text_xh, text_yh, texth.get_width() + 100, texth.get_height()))
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для_диалога.png', 400, 600)
            heart.death()
            s += 1
            b = 0
            flag = True
            Fight = False
            for_text += 1
        elif 200 < w < 300 and flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для update-export.png', 400, 750)
            heart.rect.center = cell.rect.center
            heart.live()
            s += 1
            b = 1
            flag = False
            Fight = True
        elif w == 300 and not flag:
            if type(texth) != str:
                screen.fill((0, 0, 0), pygame.Rect(text_xh, text_yh, texth.get_width() + 100, texth.get_height()))
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для_диалога.png', 400, 600)
            heart.death()
            s += 1
            b = 0
            flag = True
            Fight = False
            for_text += 1
        elif w > 300:
            w = 1
            for_text = for_text_beta
        if react == 'p' and q % 30 == 0 or react == 'c' and q % 30 == 0 or react == 'ch' and q % 200 == 0 or b == 0:
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
        if react == 'p' or react == 'c' and q % 100 == 0 or react == 'ch' and q % 100 == 0:
            all_wars.update()
        all_wars.draw(screen)
        screen.blit(heart.image, heart.rect)
        pygame.display.flip()
        hp(number)
    else:
        heart.update()
        #Death_fLag = True
        running = False


def two(sorce, for_text_beta):
    global running, w, flag, q, for_text, cell, heart, s, b, Fight
    if not heart.update_yes():
        if w == 0:
            cell = Cell('SPRITE\для_диалога.png', 400, 600)
            for_text = for_text_beta
            s = sorce
            Fight = False
        elif w < 7 and flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для update-export.png', 400, 750)
            heart.rect.center = cell.rect.center
            heart.live()
            s += 1
            flag = False
            Fight = True
            b = 1
        elif w == 7 and not flag:
            if type(texth) != str:
                screen.fill((0, 0, 0), pygame.Rect(text_xh, text_yh, texth.get_width() + 100, texth.get_height()))
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для_диалога.png', 400, 600)
            heart.death()
            s += 1
            b = 0
            flag = True
            Fight = False
            for_text += 1
        elif 7 < w < 14 and flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для update-export.png', 400, 750)
            heart.rect.center = cell.rect.center
            heart.live()
            s += 1
            b = 1
            flag = False
            Fight = True
        elif w == 14 and not flag:
            if type(texth) != str:
                screen.fill((0, 0, 0), pygame.Rect(text_xh, text_yh, texth.get_width() + 100, texth.get_height()))
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для_диалога.png', 400, 600)
            heart.death()
            s += 1
            b = 0
            flag = True
            Fight = False
            for_text += 1
        elif 14 < w < 21 and flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для update-export.png', 400, 750)
            heart.rect.center = cell.rect.center
            heart.live()
            s += 1
            b = 1
            flag = False
            Fight = True
        elif w == 21 and not flag:
            if type(texth) != str:
                screen.fill((0, 0, 0), pygame.Rect(text_xh, text_yh, texth.get_width() + 100, texth.get_height()))
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для_диалога.png', 400, 600)
            heart.death()
            s += 1
            b = 0
            flag = True
            Fight = False
            for_text += 1
        elif w > 21:
            w = 1
            s = sorce
            for_text = for_text_beta
        if b == 1:
            screen.blit(cell.image, cell.rect)
            all_wars.draw(screen)
        if q % 200 == 0:
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
        screen.blit(heart.image, heart.rect)
        q += 1
        pygame.display.flip()
        hp(number)
    else:
        heart.update()
        #Death_fLag = True
        running = False


class Death_hide_cl():
    def death_hide(self):
        global running
        global image1, go_or_no
        global Death_fLag
        global cell, number
        Death_fLag = False
        screen.fill((0, 0, 0), (800, 0, 300, 300))
        pygame.display.update()
        screen.fill((0, 0, 0))
        image1 = pygame.image.load('SPRITE\Hide_2.png').convert()
        screen.blit(image1, (800, 100))
        cell = Cell('SPRITE\для_диалога.png', 400, 600)
        font = pygame.font.Font(None, 50)
        text = font.render("Призрак убит.", True, (100, 150, 100))
        text_x = cell.rect.x + 10
        text_y = cell.rect.y + 10
        screen.blit(cell.image, cell.rect)
        screen.blit(text, (text_x, text_y))
        text = font.render("Вы получили 10 HP", True, (100, 150, 100))
        text_x = cell.rect.x + 10
        text_y = cell.rect.y + 10 + text.get_rect().bottom
        screen.blit(text, (text_x, text_y))
        number += 10
        pygame.display.update()
        time.sleep(2)
        music_fight.stop()
        running = False
        go_or_no = True

    def death_print(self):
        global go_or_no
        return go_or_no


class Live_hide_cl():
    def live_hide(self):
        global running
        global cell
        global go_or_no
        global Death_fLag, number
        Death_fLag = False
        cell = Cell('SPRITE\для_диалога.png', 400, 600)
        font = pygame.font.Font(None, 50)
        text = font.render("Призрак уходит.", True, (100, 150, 100))
        text_x = cell.rect.x + 10
        text_y = cell.rect.y + 10
        screen.blit(cell.image, cell.rect)
        screen.blit(text, (text_x, text_y))
        text = font.render("Вы получили 1 HP", True, (100, 150, 100))
        text_x = cell.rect.x + 10
        text_y = cell.rect.y + 10 + text.get_rect().bottom
        screen.blit(text, (text_x, text_y))
        number += 1
        pygame.display.update()
        time.sleep(2)
        music_fight.stop()
        running = False
        go_or_no = True

    def live_print(self):
        global go_or_no
        return go_or_no


def three(sorce, for_text_beta):
    pygame.init()
    global running, w, flag, q, for_text, cell, heart, s, b, Fight, mg, sc1, apple, number, war_now, screen2, clock
    if not heart.update_yes():
        if w == 0:
            cell = Cell('SPRITE\для_диалога.png', 400, 600)
            for_text = for_text_beta
            s = sorce
            Fight = False
        elif w < 100 and flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для update-export.png', 400, 750)
            heart.rect.center = cell.rect.center
            heart.live()
            s += 1
            flag = False
            Fight = True
            b = 1
        elif w == 100 and not flag:
            # if type(texth) != str:
            #     screen.fill((0, 0, 0), pygame.Rect(text_xh, text_yh, texth.get_width() + 100, texth.get_height()))
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для_диалога.png', 400, 600)
            heart.death()
            s += 1
            b = 0
            flag = True
            Fight = False
            for_text += 1
        elif 100 < w < 200 and flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для update-export.png', 400, 750)
            heart.rect.center = cell.rect.center
            heart.live()
            s += 1
            b = 1
            flag = False
            Fight = True
        elif w == 200 and not flag:
            # if type(texth) != str:
            #     screen.fill((0, 0, 0), pygame.Rect(text_xh, text_yh, texth.get_width() + 100, texth.get_height()))
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для_диалога.png', 400, 600)
            heart.death()
            s += 1
            b = 0
            flag = True
            Fight = False
            for_text += 1
        elif 200 < w < 300 and flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для update-export.png', 400, 750)
            heart.rect.center = cell.rect.center
            heart.live()
            s += 1
            b = 1
            flag = False
            Fight = True
        elif w == 300 and not flag:
            # if type(texth) != str:
            #     screen.fill((0, 0, 0), pygame.Rect(text_xh, text_yh, texth.get_width() + 100, texth.get_height()))
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\для_диалога.png', 400, 600)
            heart.death()
            s += 1
            b = 0
            flag = True
            Fight = False
            for_text += 1
        elif w > 300:
            w = 1
            s = sorce
            for_text = for_text_beta
        screen2 = pygame.display.set_mode((1920, 1080))
        screen2.blit(sc1, (0, 0))
        # if b == 1:
        #     screen2.blit(sc1, (0, 0))
        #     all_wars.update()
        #     all_wars.draw(screen2)
        if q % 10 == 0 and Fight:
            if war_now == 1:
                war_1()
            elif war_now == 2:
                BossAtck()
                war_now = 1
            w += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            heart.right()
        elif keys[pygame.K_a]:
            heart.left()
        elif keys[pygame.K_w]:
            heart.top()
        elif keys[pygame.K_s]:
            heart.bottom()
        mg.update()
        q += 1
        #wars[file_wars[s].rstrip()]()
        screen2.blit(cell.image, cell.rect)
        atak_sprites.draw(screen2)
        atak_sprites.update()
        screen2.blit(heart.image, heart.rect)
        screen.blit(apple,  (1500, 600))
        screen2.blit(mg.image, mg.rect)
        all_wars.update()
        all_wars.draw(screen2)
        hp(number)
        if q % 400 == 0 and Fight:
            Knopka()
        pygame.display.flip()
        #clock.tick(100)
    else:
        heart.update()
        running = False


def boss():
    global number, all_wars, hp_Hide, mg, sc1, cell, heart, s, b, q, flag, w, atak_sprites, apple, Death_hide_cl, music_fight, sc_2, clock, conez, what_ahaha
    #screen.fill((0, 0, 0))
    
    sc1 = pygame.image.load('SPRITE\Boss_fon.png').convert_alpha()
    sc1 = pygame.transform.scale(sc1, (1920, 1080))
    screen.blit(sc1, (0, 0))
    
    apple = pygame.image.load('SPRITE\APPLE_HILL.png').convert_alpha()
    #screen.blit(apple,  (1500, 600))
    
    s = 0
    b = 0
    w = 0
    
    q = 0
    flag = True
    
    all_wars = pygame.sprite.Group()
    atak_sprites = pygame.sprite.Group()
    
    mg = Megashiza()
    # screen.blit(mg.image, mg.rect)
    
    music_fight = pygame.mixer.Sound('MUSIC\FIRST\FIGHT_BOSS_FINAL.mp3')
    music_fight.set_volume(0.20)
    with open('SETTING_FILES\SETTING.txt') as f:
            text_ms = f.read()
            text_ms = text_ms.split('=')
            if text_ms[0] == "music" and text_ms[2] == 0:
                music_fight.stop()
            else:
                music_fight.play(-1)
    
    cell = Cell('SPRITE\для_диалога.png', 400, 600)
    
    heart = Heart()
    heart.death()
    
    Death_hide_class = Death_hide_cl()
    
    hp_Hide = 50
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not Fight:
                    if 1500 < event.pos[0] < 1611 and 600 < event.pos[1] < 741:
                        bag()
                        w += 1
        three(32, 20)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            con = sqlite3.connect('SQL\Bag.db')
            cur = con.cursor()
            res = cur.execute("""update Bag
                                set Count = 0""").fetchall()
            con.commit()
            con.close()
            pygame.quit()
        if hp_Hide <= 0:
            conez = True
            what_ahaha = True
            music_fight.stop()
            conzovka()
            Death_hide_class.death_hide()
            music_fight.stop()
            running = False
        clock.tick(100)
    
    
def start_fn(event, monstr):
    global texth, text_xh, text_yh, image1, flag, Fight, s, b, music_fight, hp_Hide, font, myfont, number, all_wars, q, running, heart, w, Death_fLag, cell
    
    texth = ''
    text_xh = ''
    text_yh = ''
    w = 0
    y = 0
    x = 0

    screen.fill((0, 0, 0))
    
    all_wars = pygame.sprite.Group()
    
    if monstr == 1:
        image1 = pygame.image.load('SPRITE\Hide_1.png').convert_alpha()
    if monstr == 2:
        image1 = pygame.image.load('SPRITE\ENEMY.png').convert_alpha()
    if monstr == 3:
        image1 = pygame.image.load('SPRITE\CHUDICK.png').convert_alpha()
        y = 100
    if monstr == 4:
        image1 = pygame.image.load('SPRITE\Osminog\Osminog_1.png').convert_alpha()
        Osminog(650, 100)
        x = 150
    if monstr == 5:
        screen.fill((0, 0, 0))
        image1 = pygame.image.load('SPRITE\Megashiza.png').convert_alpha()
        x = 150
        y = 100
    music_fight = pygame.mixer.Sound('MUSIC\DOUBLE\IGHT_BOSS.mp3')
    music_fight.set_volume(0.20)
    with open('SETTING_FILES\SETTING.txt') as f:
            text_ms = f.read()
            text_ms = text_ms.split('=')
            if text_ms[0] == "music" and text_ms[2] == 0:
                music_fight.stop()
            else:
                music_fight.play(-1)
    
    hp_Hide = 22
    
    s = 0
    b = 0
    
    flag = True
    Fight = False
    screen.blit(image1, (800 - x, 100 - y))
    pygame.display.flip()
    
    font = pygame.font.Font(None, 50)
    myfont = pygame.font.SysFont("SimSun", 15)
    text = font.render("АТАКА", True, (100, 255, 100))
    text_x = 620
    text_y = 800
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    ataka = pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                        text_w + 20, text_h + 20), 1)
    
    text = font.render("СЪЕСТЬ ЯБЛОКО", True, (100, 255, 100))
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
    
    
    clock = pygame.time.Clock()
    
    running = True
    q = 0
    flag = True
    
    hp(number)
    
    cell = Cell('SPRITE\для_диалога.png', 400, 600)
    
    heart = Heart()
    heart.death()

    Death_hide_class = Death_hide_cl()
    Live_hide_class = Live_hide_cl()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not Fight:
                    if ataka[0] < event.pos[0] < ataka[0] + ataka[2] and ataka[1] < event.pos[1] < ataka[1] + ataka[3]:
                        fight()
                        w += 1
                    elif inventar[0] < event.pos[0] < inventar[0] + inventar[2] and inventar[1] < event.pos[1] < inventar[1] + inventar[3]:
                        bag()
                        w += 1
                    elif posada[0] < event.pos[0] < posada[0] + posada[2] and posada[1] < event.pos[1] < posada[1] + posada[3]:
                        hope()
                        w += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            con = sqlite3.connect('SQL\Bag.db')
            cur = con.cursor()
            res = cur.execute("""update Bag
                                set Count = 0""").fetchall()
            con.commit()
            con.close()
            pygame.quit()
        if monstr == 1:
            one(0, 'p', 0)
        if monstr == 2:
            one(8, 'c', 5)
        if monstr == 3:
            one(16, 'ch', 10)
        if monstr == 4:
            two(24, 15)
        if monstr == 5:
            one(32, 'p', 20)
        if hp_Hide <= 0:
            Death_hide_class.death_hide()
            music_fight.stop()
        if hp_Hide > 32:
            Live_hide_class.live_hide()
            music_fight.stop()
    return Death_fLag


def give_hp():
    global number
    return number


def load_number(n):
    global number
    number = n

clock.tick(30)