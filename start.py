import pygame
import random
import time
import sqlite3

screen = pygame.display.set_mode((1920, 1080))
Death_fLag = False
go_or_no = False

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
        self.rect = self.rect.move(random.randrange(-5, 6), 1)
        if self.rect.centery >= cell.rect.bottom - 5 or self.rect.centerx >= cell.rect.right - 5 or self.rect.centerx <= cell.rect.left + 5 or b == 0:
            self.kill()
        if pygame.sprite.collide_mask(self, heart):
            pygame.mixer.music.load('MUSIC\FIRST\ARGH_2.mp3')
            pygame.mixer.music.set_volume(0.2)
            number -= 1
            hp(number)
            self.kill()
            pygame.mixer.music.play(0)


class WarTwo(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__(all_wars)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(cell.rect.left + 1, cell.rect.right - 25)
        self.rect.y = random.randrange(cell.rect.top + 1, cell.rect.bottom - 25)
        self.mask = pygame.mask.from_surface(self.image)
        self.p = 0
    
    def update(self):
        global number
        if self.p == 0:
            self.image = pygame.image.load('SPRITE\BOMB_VZRIV.png')
            self.p = 1
            self.image = pygame.transform.scale(self.image, (52, 52))
            self.mask = pygame.mask.from_surface(self.image)
        else:
            self.kill()
        if self.rect.centery >= cell.rect.bottom - 5 or self.rect.centerx >= cell.rect.right - 5 or self.rect.centerx <= cell.rect.left + 5 or b == 0:
            self.kill()
        if pygame.sprite.collide_mask(self, heart):
            pygame.mixer.music.load('MUSIC\FIRST\ARGH_2.mp3')
            pygame.mixer.music.set_volume(0.2)
            number -= 2
            hp(number)
            self.kill()
            pygame.mixer.music.play(0)
    

class Heart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('SPRITE\????????????-export.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = cell.rect.center
        self.mask = pygame.mask.from_surface(self.image)
        self.image_load = self.image
    
    def right(self):
        if self.rect.centerx + (max(self.mask.outline(), key=lambda x: x[0])[0] // 2) < cell.rect.right:
            self.rect = self.rect.move(2, 0)

    def left(self):
        if self.rect.centerx - (max(self.mask.outline(), key=lambda x: x[0])[0] // 2) > cell.rect.left:
            self.rect = self.rect.move(-2, 0)

    def top(self):
        if self.rect.centery - (max(self.mask.outline(), key=lambda x: x[1])[0] // 2) > cell.rect.top:
            self.rect = self.rect.move(0, -2)
    
    def bottom(self):
        if self.rect.centery + (max(self.mask.outline(), key=lambda x: x[1])[0] // 2) + 10 < cell.rect.bottom:
            self.rect= self.rect.move(0, 2)
    
    def update(self):
        global Death_fLag
        if number == 0:
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
            self.image = pygame.image.load('SPRITE\????????????-export.png')
            self.rect = self.image.get_rect()
            self.rect.center = cell.rect.center
            self.rect.x -= 10
            self.rect.y -= 10
            screen.blit(cell.image, cell.rect)
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.5)
            self.image = pygame.image.load('SPRITE\????????????_2-export.png')
            self.rect.center = cell.rect.center
            screen.blit(cell.image, cell.rect)
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.5)
            self.image = pygame.image.load('SPRITE\????????????_3-export.png')
            self.rect.center = cell.rect.center
            screen.blit(cell.image, cell.rect)
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.5)
            self.image = pygame.image.load('SPRITE\????????????_4-export.png')
            self.rect.center = cell.rect.center
            screen.blit(cell.image, cell.rect)
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.9)
            self.image = pygame.image.load('SPRITE\????????????_5-export.png')
            self.rect.center = cell.rect.center
            screen.blit(cell.image, cell.rect)
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.5)
            music_dead.stop()
            Death_fLag = True
        music_dead.stop()
    
    def update_yes(self):
        global music_fight
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
                            where Object = '????????????'""").fetchall()
        w += 1
        number += 5
    con.commit()
    con.close()
        


def hope():
    global image1
    global hp_Hide
    global texth, text_xh, text_yh
    hp_Hide += 5
    texth = myfont.render("????????????", True, (100, 255, 100))
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
    War('SPRITE\war_2.png')
    w += 1


def dialog_1():
    global cell
    cell = Cell('SPRITE\??????_??????????????.png', 400, 600)
    font = pygame.font.Font(None, 50)
    text = font.render("?????????????? ???? ???????????????? ????????????", True, (100, 150, 100))
    text_x = cell.rect.x + 10
    text_y = cell.rect.y + 10
    screen.blit(cell.image, cell.rect)
    screen.blit(text, (text_x, text_y))


def dialog_2():
    global cell
    font = pygame.font.Font(None, 50)
    text = font.render("?????????????? ?? ??????-???? ????????????", True, (100, 150, 100))
    text_x = cell.rect.x + 10
    text_y = cell.rect.y + 10
    screen.blit(cell.image, cell.rect)
    screen.blit(text, (text_x, text_y))

def dialog_3():
    global cell
    font = pygame.font.Font(None, 50)
    text = font.render("?????????????? ???? ????????????????, ??????", True, (100, 150, 100))
    text_x = cell.rect.x + 10
    text_y = cell.rect.y + 10
    screen.blit(cell.image, cell.rect)
    screen.blit(text, (text_x, text_y))
    text = font.render("???? ?????? ????????????", True, (100, 150, 100))
    text_x = cell.rect.x + 10
    text_y = cell.rect.y + 10 + text.get_rect().bottom
    screen.blit(text, (text_x, text_y))

def war_3():
    global w
    War('SPRITE\war_3.png')
    w += 1


def dialog_4():
    global cell
    font = pygame.font.Font(None, 50)
    text = font.render("?????????????? ?????????? ????????", True, (100, 150, 100))
    text_x = cell.rect.x + 10
    text_y = cell.rect.y + 10
    screen.blit(cell.image, cell.rect)
    screen.blit(text, (text_x, text_y))


def war_4():
    global w
    WarTwo('SPRITE\BOMB_ATACK.png')
    w += 1


def war_5():
    global w
    WarTwo('SPRITE\BOMB_ENEMY.png')
    w += 1


def dialog_5():
    global cell
    cell = Cell('SPRITE\??????_??????????????.png', 400, 600)
    font = pygame.font.Font(None, 50)
    text = font.render("???????????????? ?????????????? ???? ??????", True, (100, 150, 100))
    text_x = cell.rect.x + 10
    text_y = cell.rect.y + 10
    screen.blit(cell.image, cell.rect)
    screen.blit(text, (text_x, text_y))


def dialog_6():
    global cell
    font = pygame.font.Font(None, 50)
    text = font.render("???? ???????????????????? ???????? ???? ??????????", True, (100, 150, 100))
    text_x = cell.rect.x + 10
    text_y = cell.rect.y + 10
    screen.blit(cell.image, cell.rect)
    screen.blit(text, (text_x, text_y))

def dialog_7():
    global cell
    font = pygame.font.Font(None, 50)
    text = font.render("???? ???? ??????????????????,", True, (100, 150, 100))
    text_x = cell.rect.x + 10
    text_y = cell.rect.y + 10
    screen.blit(cell.image, cell.rect)
    screen.blit(text, (text_x, text_y))
    text = font.render("?????? ?????????? ????????", True, (100, 150, 100))
    text_x = cell.rect.x + 10
    text_y = cell.rect.y + 10 + text.get_rect().bottom
    screen.blit(text, (text_x, text_y))

def war_6():
    global w
    WarTwo('SPRITE\BOMB_ENEMY.png')
    w += 1


def dialog_8():
    global cell
    font = pygame.font.Font(None, 50)
    text = font.render("???? ???????????? ????????", True, (100, 150, 100))
    text_x = cell.rect.x + 10
    text_y = cell.rect.y + 10
    screen.blit(cell.image, cell.rect)
    screen.blit(text, (text_x, text_y))


wars = {'dialog_1': dialog_1, 'war_1': war_1, 'dialog_2': dialog_2, 'war_2': war_2, 'dialog_3': dialog_3, 'war_3': war_3, 'dialog_4': dialog_4,
        'dialog_5': dialog_5, 'war_4': war_4, 'dialog_6': dialog_6, 'war_5': war_5, 'dialog_7': dialog_7, 'war_6': war_6, 'dialog_8': dialog_8} 
file_wars = open('wars.txt').readlines()
w = 0


def one(sorce, react):
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
    global w, Death_fLag
    if not heart.update_yes():
        if react == 'p' and q % 30 == 0 or react == 'c' and q % 40 == 0:
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
        if react == 'p' or q % 100 == 0:
            all_wars.update()
        screen.blit(heart.image, heart.rect)
        pygame.display.flip()
        if w == 0:
            s = sorce
            Fight = False
        elif w < 100 and flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\?????? update-export.png', 400, 750)
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
            cell = Cell('SPRITE\??????_??????????????.png', 400, 600)
            heart.death()
            s += 1
            b = 0
            flag = True
            Fight = False
        elif 100 < w < 200 and flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\?????? update-export.png', 400, 750)
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
            cell = Cell('SPRITE\??????_??????????????.png', 400, 600)
            heart.death()
            s += 1
            b = 0
            flag = True
            Fight = False
        elif 200 < w < 300 and flag:
            screen.fill((0, 0, 0), (cell.rect.x, cell.rect.y, cell.rect.right - cell.rect.x, 790 - cell.rect.y))
            cell = Cell('SPRITE\?????? update-export.png', 400, 750)
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
            cell = Cell('SPRITE\??????_??????????????.png', 400, 600)
            heart.death()
            s += 1
            b = 0
            flag = True
            Fight = False
        elif w > 300:
            w = 0
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
        screen.fill((0, 0, 0), (800, 100, 300, 300))
        pygame.display.update()
        image1 = pygame.image.load('SPRITE\Hide_2.png')
        screen.blit(image1, (800, 100))
        cell = Cell('SPRITE\??????_??????????????.png', 400, 600)
        font = pygame.font.Font(None, 50)
        text = font.render("?????????????? ????????.", True, (100, 150, 100))
        text_x = cell.rect.x + 10
        text_y = cell.rect.y + 10
        screen.blit(cell.image, cell.rect)
        screen.blit(text, (text_x, text_y))
        text = font.render("???? ???????????????? 10 HP", True, (100, 150, 100))
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
        cell = Cell('SPRITE\??????_??????????????.png', 400, 600)
        font = pygame.font.Font(None, 50)
        text = font.render("?????????????? ????????????.", True, (100, 150, 100))
        text_x = cell.rect.x + 10
        text_y = cell.rect.y + 10
        screen.blit(cell.image, cell.rect)
        screen.blit(text, (text_x, text_y))
        text = font.render("???? ???????????????? 1 HP", True, (100, 150, 100))
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


def start_fn(event, monstr):
    global texth, text_xh, text_yh, image1, flag, Fight, s, b, music_fight, hp_Hide, font, myfont, number, all_wars, q, running, heart, w, Death_fLag
    
    texth = ''
    text_xh = ''
    text_yh = ''
    w = 0

    screen.fill((0, 0, 0))
    
    if monstr == 1:
        image1 = pygame.image.load('SPRITE\Hide_1.png')
    if monstr == 2:
        image1 = pygame.image.load('SPRITE\ENEMY.png')
    music_fight = pygame.mixer.Sound('MUSIC\DOUBLE\IGHT_BOSS.mp3')
    music_fight.set_volume(0.20)
    with open('SETTING_FILES\SETTING.txt') as f:
            text_ms = f.read()
            text_ms = text_ms.split('=')
            if text_ms[0] == "music" and text_ms[2] == 0:
                music_fight.stop()
            else:
                music_fight.play(-1)
    
    hp_Hide = 20
    
    s = 0
    b = 0
    
    flag = True
    Fight = False
    
    screen.blit(image1, (800, 100))
    pygame.display.flip()
    
    font = pygame.font.Font(None, 50)
    myfont = pygame.font.SysFont("SimSun", 15)
    text = font.render("??????????", True, (100, 255, 100))
    text_x = 620
    text_y = 800
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    ataka = pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                        text_w + 20, text_h + 20), 1)
    
    text = font.render("???????????? ????????????", True, (100, 255, 100))
    text_x = text_x + text_w + 50
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    inventar = pygame.draw.rect(screen, (255, 255, 255), (text_x - 10, text_y - 10,
                                        text_w + 20, text_h + 20), 1)
    
    text = font.render("????????????", True, (100, 255, 100))
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

    Death_hide_class = Death_hide_cl()
    Live_hide_class = Live_hide_cl()
    
    while running:
        for event in pygame.event.get():
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
            one(0, 'p')
        if monstr == 2:
            one(8, 'c')
        if hp_Hide <= 0:
            Death_hide_class.death_hide()
            music_fight.stop()
        if hp_Hide > 30:
            Live_hide_class.live_hide()
            music_fight.stop()
    return Death_fLag