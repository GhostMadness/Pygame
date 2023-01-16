import pygame
import time
import random
from start import screen, start_fn, Death_fLag, go_or_no, Live_hide_cl, Death_hide_cl
from location_2 import start_dias
import sqlite3

# UTF-8
location_3 = False
location_2 = False
location_1 = False
ON = True
ON_2 = True
l_d = (False, False)
l_d1 = (False, False)
l_d2 = (False, False)

pygame.init()

music_location_4 = pygame.mixer.Sound('MUSIC\FIRST\HOME.mp3')
music_location_4.set_volume(0.2)

music_location_3 = pygame.mixer.Sound('MUSIC\FIRST\LOCATION_3_1.mp3')
music_location_3.set_volume(0.1)

music_location_2 = pygame.mixer.Sound('MUSIC\DOUBLE\location_2.mp3')
music_location_2.set_volume(0.2)

music_location_1 = pygame.mixer.Sound('MUSIC\DOUBLE\location_1.mp3')
music_location_1.set_volume(0.2)

music_settings = pygame.mixer.Sound('SETTING_FILES\SETTING.oga')
music_settings.set_volume(0.1)

music_menu = pygame.mixer.Sound('MUSIC\FIRST\MENU.mp3')
music_menu.set_volume(0.05)

music_locatioN_5 = pygame.mixer.Sound('MUSIC\DOUBLE\LOCATION_5.mp3')
music_locatioN_5.set_volume(0.2)

schet = 0
flagor = False


def update(one=False, two=False, three=False, four=False, five=False, six=False, seven=False):
    global flagor, music_settings, music_location_1, music_location_2, music_location_3, music_location_4, music_menu
    pygame.init()
    if flagor == False:
        music_settings.stop()
        music_location_1.stop()
        music_location_2.stop()
        music_location_3.stop()
        music_location_4.stop()
        music_locatioN_5.stop()
    elif flagor:
        if five:
            music_settings.play(-1)
        if one:
            music_location_1.play(-1)
        if two:
            music_location_2.play(-1)
        if three:
            music_location_3.play(-1)
        if four:
            music_location_4.play(-1)
        if six:
            music_menu.play(-1)
        if seven:
            music_locatioN_5.play(-1)


def settings():
    global music_settings, music_location_1, music_location_2, music_location_3, music_location_4, schet, screen

    def click():
        global schet, flagor
        if schet % 2 == 0:
            flagor = True
        elif schet % 2 != 0:
            flagor = False
    background_img = pygame.image.load("SPRITE\SETTINGS_FON_2.jpg")
    button_menu_img = pygame.image.load("SPRITE\EXIT_MENU_BUTTON.png")
    button_menu_img_tr = pygame.transform.scale(button_menu_img, (50, 50))

    rect_but_menu = button_menu_img_tr.get_rect()
    rect_but_menu.x = 10
    rect_but_menu.y = 10

    font = pygame.font.Font(None, 50)
    text = font.render("УПРАВЛЕНИЕ", True, (230, 230, 230))
    text_x = 1920 // 2 - 50
    text_y = 1080 // 2 - 50

    text_w = font.render("ВВЕРХ - W", True, (230, 230, 230))
    text_w_x = 1920 // 2 - 50
    text_w_y = 1080 // 2 - 20

    text_s = font.render("ВНИЗ - S", True, (230, 230, 230))
    text_s_x = 1920 // 2 - 50
    text_s_y = 1080 // 2 + 10

    text_d = font.render("ВПРАВО - D", True, (230, 230, 230))
    text_d_x = 1920 // 2 - 50
    text_d_y = 1080 // 2 + 40

    text_a = font.render("ВЛЕВО - A", True, (230, 230, 230))
    text_a_x = 1920 // 2 - 50
    text_a_y = 1080 // 2 + 70

    text_enter = font.render("ГОВОРИТЬ - ENTER", True, (230, 230, 230))
    text_enter_x = 1920 // 2 - 50
    text_enter_y = 1080 // 2 + 100

    text_music = font.render("МУЗЫКА", True, (230, 230, 230))
    text_music_x = 1920 // 2 - 60
    text_music_y = 1080 // 2 - 305

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cute[0] < event.pos[0] < cute[0] + cute[2] and cute[1] < event.pos[1] < cute[1] + cute[3]:
                    click()
                    update(five=True)
                    schet += 1
                if rect_but_menu[0] < event.pos[0] < rect_but_menu[0] + rect_but_menu[2] and rect_but_menu[1] < \
                        event.pos[1] < rect_but_menu[1] + rect_but_menu[3]:
                    music_settings.stop()
                    return start_menu()
        if running:
            screen.blit(background_img, (0, 0))
            screen.blit(button_menu_img_tr, (10, 10))
            screen.blit(text, (text_x, text_y))
            screen.blit(text_w, (text_w_x, text_w_y))
            screen.blit(text_s, (text_s_x, text_s_y))
            screen.blit(text_a, (text_a_x, text_a_y))
            screen.blit(text_d, (text_d_x, text_d_y))
            screen.blit(text_enter, (text_enter_x, text_enter_y))
            screen.blit(text_music, (text_music_x, text_music_y))
            
            cute = pygame.draw.rect(screen, (0, 255, 0), (1920 // 2 + 100, 1080 // 2 - 300, 25, 25))
            pygame.display.flip()


def loading_death():
    size = 1920, 1080
    screen = pygame.display.set_mode(size)
    image_loading = pygame.image.load("SPRITE\APPLE_HILL.png")
    image_player = pygame.image.load("SPRITE\гг.png")
    music = pygame.mixer.Sound('MUSIC\WHAT\ZVEK_KYCANIA.mp3')
    running = True
    width_line = 0
    text_loading = "Загрузка"
    schet = 0
    apple_x = 2000
    a = True
    schet_2 = -30
    schet_3 = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render(text_loading, True, (100, 255, 100))
        text_x = 51
        text_y = 850
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (255, 255, 255), (51, 887, width_line, 50))
        screen.blit(image_player, (1920 // 2 - 100, 1080 // 2 - 100))
        if apple_x >= 1920 // 2:
            screen.blit(image_loading, (apple_x, 1080 // 2 - 100))
        elif a and apple_x <= 1920 // 2:
            music.set_volume(0.2)
            music.play(0)
            a = False
        if width_line >= 1800:
            time.sleep(1)
            width_line += 10
            time.sleep(0.5)
            start_location_1()
        width_line += 2
        if schet == 100:
            if text_loading == "Загрузка...":
                text_loading = "Загрузка"
            else:
                text_loading = text_loading + '.'
            schet = 0
        schet += 1
        apple_x -= 2
        text_hill = font.render("+20 HP", True, (0, 250, 0))
        text_hill_x = 1920 // 2
        if a == False and schet_2 != 400:
            schet_2 += 2
        if schet_2 >= 400:
            text_ok = font.render("НЕ СДАВАЙСЯ", True, (0, 200, 0))
            text_ok_x = 1920 // 2 - 50
            text_ok_y = 800
            screen.blit(text_ok, (text_ok_x, text_ok_y))
        if schet_3 <= 500:
            screen.blit(text_hill, (text_hill_x, schet_2))
        if schet_2 == 400:
            schet_3 += 2
        pygame.display.flip()


def start_menu():
    update(six=True)
    global music_menu, screen
    IMG_MENU = pygame.image.load("SPRITE\MAIN_10.png")
    IMG_EXIT_BUTTON = pygame.image.load("SPRITE\EXIT_BUTTON.png")
    IMG_PLAY_BUTTON = pygame.image.load("SPRITE\PLAY_BUTTON.png")
    IMG_SETTING_BUTTON = pygame.image.load("SPRITE\SETTING_BUTTON.png")
    rect_1 = IMG_EXIT_BUTTON.get_rect()
    rect_1.x = 43
    rect_1.y = 620 + 50
    rect_2 = IMG_SETTING_BUTTON.get_rect()
    rect_2.x = 43
    rect_2.y = 345 + 50
    rect_3 = IMG_PLAY_BUTTON.get_rect()
    rect_3.x = 43
    rect_3.y = 70 + 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect_1[0] < event.pos[0] < rect_1[0] + rect_1[2] and rect_1[1] < event.pos[1] < rect_1[1] + \
                        rect_1[3]:
                    running = False
                if rect_2[0] < event.pos[0] < rect_2[0] + rect_2[2] and rect_2[1] < event.pos[1] < rect_2[1] + \
                        rect_2[3]:
                    music_menu.stop()
                    return settings()
                if rect_3[0] < event.pos[0] < rect_3[0] + rect_3[2] and rect_3[1] < event.pos[1] < rect_3[1] + \
                        rect_3[3]:
                    music_menu.stop()
                    return start_location_1()
        screen.fill((0, 0, 0))
        screen.blit(IMG_MENU, (0, 0))
        screen.blit(IMG_PLAY_BUTTON, (43, 70 + 50))
        screen.blit(IMG_SETTING_BUTTON, (43, 345 + 50))
        screen.blit(IMG_EXIT_BUTTON, (43, 620 + 50))
        pygame.display.flip()


class NPC_BUILDING(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, nickname, rgb_nickname, men=False):
        super().__init__()
        self.name = nickname
        self.rgb_nickname = rgb_nickname
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.men = men

        self.text_res = ''
        self.text = ''
        self.font = pygame.font.Font(None, 50)
        self.schet = 0

    def dialog(self, text_npc):
        self.text_res = text_npc.split("N")
        self.image_dialog_window = pygame.image.load("SPRITE\для_диалога.png").convert_alpha()
        self.rect_dialog_window = self.image_dialog_window.get_rect()
        self.rect_dialog_window.x = 611
        self.rect_dialog_window.y = 760

    def click_update(self):
        if self.schet >= len(self.text_res):
            if self.name == "Мужик":
                self.text_name = self.font.render(self.name, False, self.rgb_nickname)
                self.text = self.font.render("Уже уходишь?", True, (255, 255, 255))
                screen.blit(self.text_name, (620, 720))
                screen.blit(self.image_dialog_window, self.rect_dialog_window)
                screen.blit(self.text, (620, 770))
                pygame.display.flip()
                fgl = False
                while True:
                    for resoult in pygame.event.get():
                        if resoult.type == pygame.KEYDOWN and resoult.key == pygame.K_RETURN:
                            fgl = True
                            break
                    if fgl:
                        break
                time.sleep(0.2)
                return
            if self.name == 'Рин':
                self.text_name = self.font.render(self.name, False, self.rgb_nickname)
                self.text = self.font.render("До скорой встречи путник!", True, (255, 255, 255))
                screen.blit(self.text_name, (620, 720))
                screen.blit(self.image_dialog_window, self.rect_dialog_window)
                screen.blit(self.text, (620, 770))
                pygame.display.flip()
                fgl = False
                while True:
                    for resoult in pygame.event.get():
                        if resoult.type == pygame.KEYDOWN and resoult.key == pygame.K_RETURN:
                            fgl = True
                            break
                    if fgl:
                        break
                time.sleep(0.2)
                return
            self.text_name = self.font.render(self.name, False, self.rgb_nickname)
            self.text = self.font.render("Мне больше нечего тебе сказать", True, (255, 255, 255))
            screen.blit(self.text_name, (620, 720))
            screen.blit(self.image_dialog_window, self.rect_dialog_window)
            screen.blit(self.text, (620, 770))
            pygame.display.flip()
            fgl = False
            while True:
                for resoult in pygame.event.get():
                    if resoult.type == pygame.KEYDOWN and resoult.key == pygame.K_RETURN:
                        fgl = True
                        break
                if fgl:
                    break
            screen.blit(self.text_name, (620, 720))
            self.text = self.font.render("уходи!", True, (255, 255, 255))
            screen.blit(self.image_dialog_window, self.rect_dialog_window)
            screen.blit(self.text, (620, 770))
            pygame.display.flip()
            fgl = False
            while True:
                for resoult in pygame.event.get():
                    if resoult.type == pygame.KEYDOWN and resoult.key == pygame.K_RETURN:
                        fgl = True
                        break
                if fgl:
                    break
            self.schet += 1
            time.sleep(0.2)
            return
        self.text_name = self.font.render(self.name, False, self.rgb_nickname)
        for i in self.text_res:
            pygame.event.pump()
            self.text = self.font.render(str(i), False, (255, 255, 255))
            self.schet += 1
            screen.blit(self.text_name, (620, 720))
            screen.blit(self.image_dialog_window, self.rect_dialog_window)
            screen.blit(self.text, (620, 770))
            pygame.display.flip()
            fgl = False
            while True:
                for resoult in pygame.event.get():
                    if resoult.type == pygame.KEYDOWN and resoult.key == pygame.K_RETURN:
                        fgl = True
                        break
                if fgl:
                    break
            time.sleep(0.2)


class NPC_BUILDING_SHIZA(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, nickname, rgb_nickname):
        super().__init__()
        self.name = nickname
        self.rgb_nickname = rgb_nickname
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.text_res = ''
        self.text = ''
        self.font = pygame.font.Font(None, 50)
        self.schet = 0

    def dialog(self, text_npc):
        self.text_res = text_npc.split("N")
        self.image_dialog_window = pygame.image.load("SPRITE\для_диалога.png").convert_alpha()
        self.rect_dialog_window = self.image_dialog_window.get_rect()
        self.rect_dialog_window.x = 611
        self.rect_dialog_window.y = 700

    def click_update(self):
        self.text_name = self.font.render(self.name, False, self.rgb_nickname)
        if self.schet >= len(self.text_res):
            self.image = pygame.image.load('SPRITE\Shiza_02.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.5)
            self.image = pygame.image.load('SPRITE\Shiza_03.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.5)
            self.image = pygame.image.load('SPRITE\Shiza_04.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.4)
            self.image = pygame.image.load('SPRITE\Shiza_05.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.3)
            self.image = pygame.image.load('SPRITE\Shiza_06.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.4)
            self.image = pygame.image.load('SPRITE\Shiza_07.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.4)
            self.image = pygame.image.load('SPRITE\Shiza_08.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.4)
            self.image = pygame.image.load('SPRITE\Shiza_09.png')
            self.image = pygame.transform.scale(self.image, (100, 100))
            screen.blit(self.image, self.rect)
            pygame.display.flip()
            time.sleep(0.4)

            self.rect.x -= 1500
        else:
            for i in self.text_res:
                pygame.event.pump()
                self.text = self.font.render(str(i), False, (255, 255, 255))
                screen.blit(self.text_name, (620, 650))
                screen.blit(self.image_dialog_window, self.rect_dialog_window)
                screen.blit(self.text, (620, 720))
                pygame.display.flip()
                fgl = False
                while True:
                    for resoult in pygame.event.get():
                        if resoult.type == pygame.KEYDOWN and resoult.key == pygame.K_RETURN:
                            fgl = True
                            break
                    if fgl:
                        break
                self.schet += 1
                time.sleep(0.1)

        # ПИСАТЬ КАЖДОЕ НОВОЕ СЛОВОСОЧЕТАНИЕ ЧЕРЕЗ N КОГДА ПЕРЕДАЁШЬ В ФУНКЦИЮ ТЕКСТ ПЕРСОНАЖА!!! ПРИМЕР СНИЗУ!!!


class Heroy(pygame.sprite.Sprite):
    def __init__(self, right=None, left=None, bottom=None, top=None, x=600, y=400):
        super().__init__()
        self.image = pygame.image.load('SPRITE\гг.png').convert_alpha()
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

        if self.bottom_sprites == None:
            self.bottom_sprites = pygame.sprite.Group()

    def update(self):
        pass

    def top(self):
        global y
        self.image = pygame.image.load('SPRITE\гг.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        if not pygame.sprite.spritecollideany(self, self.top_sprites):
            self.rect.y -= 5

    def botton(self):
        global y
        self.image = pygame.image.load('SPRITE\гг.png').convert_alpha()
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
            self.image = pygame.transform.scale(pygame.image.load(filename),
                                                (infoObject.current_w // 6 - 60, infoObject.current_h))
        elif i == 't':
            self.image = pygame.transform.scale(pygame.image.load(filename),
                                                (infoObject.current_w, infoObject.current_h // 3))
        elif i == 'b':
            self.image = pygame.transform.scale(pygame.image.load(filename),
                                                (infoObject.current_w, infoObject.current_h // 3))
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]


class Stop_2(pygame.sprite.Sprite):
    def __init__(self, filename, coord, *size):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]
        if size:
            self.image = pygame.transform.scale(self.image, size)

def start_loction_5():
    update(seven=True)

    image_background = pygame.image.load("location_6\esilt\map.png")
    image_1 = pygame.image.load("location_6\esilt\custle.png")
    image_3 = pygame.image.load("location_6\esilt\mogila_1.png")
    image_4 = pygame.image.load("location_6\esilt\mogila_2.png")

    sc1 = pygame.Surface((1920, 1080))
    sc1.blit(image_background, (0, 0))
    sc1.blit(image_1, (0, 982))
    sc1.blit(image_3, (1780, 0))
    sc1.blit(image_4, (0, 0))

    clock = pygame.time.Clock()

    bottom_sprite = pygame.sprite.Group()
    bottom_sprite.add(Stop_2("location_6\esilt\custle.png", (0, 982)))

    right_sprite = pygame.sprite.Group()
    right_sprite.add(Stop_2("location_6\esilt\mogila_1.png", (1780, 0)))

    left_sprite = pygame.sprite.Group()
    left_sprite.add(Stop_2("location_6\esilt\mogila_1.png", (0, 0)))

    gg_5 = Heroy(right=right_sprite, left=left_sprite, bottom=bottom_sprite, x=50, y=975)

    other_sprite_finish = pygame.sprite.Group()
    other_sprite_finish.add(Stop_2("SPRITE\VIXOD_LOC.png", (1920 // 2 + 100, 0)))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                print(event.pos)
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            gg_5.right()
        if key[pygame.K_a]:
            gg_5.left()
        if key[pygame.K_w]:
            gg_5.top()
        if key[pygame.K_s]:
            gg_5.botton()
        if key[pygame.K_ESCAPE]:
            running = False

        screen.blit(sc1, (0, 0))
        screen.blit(gg_5.image, gg_5.rect)
        pygame.display.flip()
        clock.tick(60)

def start_location_4():
    update(four=True)
    global location_3, music_location_4, screen

    image_background = pygame.image.load("location_5_men\RESULT\location_5_man.png")
    image_1 = pygame.image.load("location_5_men\RESULT\iblioteka.png")
    image_3 = pygame.image.load("location_5_men\RESULT\cover.png")
    image_4 = pygame.image.load("location_5_men\RESULT\oxes.png")
    image_5 = pygame.image.load("location_5_men\RESULT\object.png")

    menNpc = pygame.image.load("SPRITE\pNPC\Men.png")
    menNPC_tr = pygame.transform.scale(menNpc, (100, 100))

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

    clock = pygame.time.Clock()

    gg_4 = Heroy(bottom=bottom_sprite, right=right_sprite, left=left_sprites, top=top_sprites, x=1050, y=1000)

    other_sprite_exit = pygame.sprite.Group()
    other_sprite_exit.add(Stop_2("SPRITE\VIXOD_LOC.png", (932, 1100)))

    button_menu_img = pygame.image.load("SPRITE\EXIT_MENU_BUTTON.png")
    button_menu_img_tr = pygame.transform.scale(button_menu_img, (50, 50))

    menshik = NPC_BUILDING("SPRITE\pNPC\Men.png", 100, 100, "Мужик", (250, 0, 0))
    men_group = pygame.sprite.Group()
    men_group.add(Stop_2("SPRITE\pNPC\Men.png", (100, 100), (100, 100)))

    rect_but_menu = button_menu_img_tr.get_rect()
    rect_but_menu.x = 10
    rect_but_menu.y = 10

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_but_menu[0] < event.pos[0] < rect_but_menu[0] + rect_but_menu[2] and rect_but_menu[1] < \
                        event.pos[1] < rect_but_menu[1] + rect_but_menu[3]:
                    return start_menu()
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
        screen.blit(button_menu_img_tr, (10, 10))
        screen.blit(menNPC_tr, (100, 100))
        men_group.draw(screen)

        if pygame.sprite.spritecollideany(gg_4, other_sprite_exit):
            music_location_4.stop()
            location_3 = True
            start_location_3()
            running = False

        if pygame.sprite.spritecollideany(gg_4, men_group) and key[pygame.K_RETURN]:
            menshik.dialog(
                "Ты наверно не понимаешь Nчто здесь происходит? NСуть в твоём прошлом NИди дальше по дороге NНадеюсь, там ты всё вспомнишь NМожешь побыть у меня дома Nпока не решишь идти дальше NМне нужно работать NЖелаю удачи!")
            menshik.click_update()

        pygame.display.flip()
        clock.tick(60)


def start_location_3():
    update(three=True)
    global location_2, location_3, music_location_3, l_d2
    size = 1920, 1080
    screen = pygame.display.set_mode(size)
    image_background = pygame.image.load("location_house\ckground.png")
    image_1 = pygame.image.load("location_house\location_3.png")
    image_2 = pygame.image.load("location_house\location_3_house.png")
    sc1 = pygame.Surface((1920, 1080))
    sc1.blit(image_background, (0, 0))
    sc1.blit(image_2, (0, 0))
    sc1.blit(image_1, (0, 0))

    top_sprite = pygame.sprite.Group()
    left_sprite = pygame.sprite.Group()

    top_sprite.add(Stop_2("location_house\sprite_collide\ottom_grass.png", (0, 265)))
    left_sprite.add(Stop_2("location_house\sprite_collide\ght_grass.png", (830, 0)))

    other_sprite = pygame.sprite.Group()
    other_sprite.add(Stop_2("SPRITE\CHUDICK.png", (1920 // 2 + 5 - 80, 1080 // 2 + 80), 100, 100))

    img_hide = pygame.image.load("SPRITE\CHUDICK.png")
    img_hide_scale = pygame.transform.scale(img_hide, (100, 100))

    sdegfoin1 = True

    clock = pygame.time.Clock()

    gg_3 = Heroy(top=top_sprite, left=left_sprite, x=550, y=100)
    if location_3:
        gg_3.rect.x = 1230
        gg_3.rect.y = 500
        location_3 = False

    other_sprite_2 = pygame.sprite.Group()
    other_sprite_2.add(Stop_2("SPRITE\VIXOD_LOC.png", (1134, 86)))

    other_sprite_5 = pygame.sprite.Group()
    other_sprite_5.add(Stop_2("SPRITE\VIXOD_LOC.png", (811, 1077)))

    other_sprite_exit = pygame.sprite.Group()
    other_sprite_exit.add(Stop_2("SPRITE\VIXOD_LOC.png", (-350, 380)))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
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

        if pygame.sprite.spritecollideany(gg_3, other_sprite) and sdegfoin1:
            music_location_3.stop()
            a = start_fn(event, 3)
            one = Live_hide_cl()
            two = Death_hide_cl()
            l_d2 = (one.live_print(), two.death_print())
            if a:
                l_d2 = (False, False)
                loading_death()
        #other_sprite_5
        if pygame.sprite.spritecollideany(gg_3, other_sprite_5):
            music_location_3.stop()
            start_loction_5()
            running = False

        if l_d2[0] == True or l_d2[1] == True:
            sdegfoin1 = False
        if (l_d2[0] == False and l_d2[1] == False):
            screen.blit(img_hide_scale, (1920 // 2, 1080 // 2 + 80))

        if pygame.sprite.spritecollideany(gg_3, other_sprite_2):
            music_location_3.stop()
            start_location_4()
            running = False
        if pygame.sprite.spritecollideany(gg_3, other_sprite_exit):
            music_location_3.stop()
            location_2 = True
            start_location_2()
            running = False

        pygame.display.flip()
        clock.tick(60)

def start_location_2():
    update(two=True)
    global location_2, location_1, ON_2, Death_fLag, l_d1, music_location_2
    size = 1920, 1080
    screen_local_2 = pygame.display.set_mode(size)
    image_background = pygame.image.load("location_4\esult_sprite\map.png")
    image_1 = pygame.image.load("location_4\esult_sprite\house.png")
    image_2 = pygame.image.load("location_4\esult_sprite\other.png")
    sc1 = pygame.Surface((1920, 1080))
    sc1.blit(image_background, (0, 0))
    sc1.blit(image_2, (0, 0))
    sc1.blit(image_1, (0, 0))

    sdegfoin1 = True

    bottom_sprites = pygame.sprite.Group()
    top_sprites = pygame.sprite.Group()

    bottom_sprites.add(Stop_2("location_4\esult_sprite\ground_bottom.png", (0, 716)))
    top_sprites.add(Stop_2("location_4\esult_sprite\house_2.png", (0, 0)))

    clock = pygame.time.Clock()

    gg_2 = Heroy(top=top_sprites, bottom=bottom_sprites, x=580, y=70)
    if location_2:
        gg_2.rect.x = 1750
        gg_2.rect.y = 500
        location_2 = False

    other_sprite_2 = pygame.sprite.Group()
    other_sprite_2.add(Stop_2("SPRITE\VIXOD_LOC.png", (1919, 396)))

    other_sprite_exit = pygame.sprite.Group()
    other_sprite_exit.add(Stop_2("SPRITE\VIXOD_LOC.png", (-350, 384)))

    other_sprite = pygame.sprite.Group()
    other_sprite.add(Stop_2("SPRITE\ENEMY.png", (1920 // 2 + 5 - 80, 1080 // 2 + 80), 100, 100))

    menshik = NPC_BUILDING("SPRITE\pNPC\Men.png", 100, 100, "Мужик", (250, 0, 0))
    men_group = pygame.sprite.Group()
    men_group.add(Stop_2("SPRITE\pNPC\Men.png", (1800, 417), (100, 100)))

    img_hide = pygame.image.load("SPRITE\ENEMY.png")
    img_hide_scale = pygame.transform.scale(img_hide, (100, 100))

    npc_1 = NPC_BUILDING("SPRITE\pNPC\selski_men.png", 673, 408, "Алекс", (255, 36, 0))
    npc_1_group = pygame.sprite.Group()
    npc_1_group.add(npc_1)

    npc_2 = NPC_BUILDING("SPRITE\pNPC\cloyn.png", 97, 417, "Роберт", (255, 192, 203))
    npc_2_group = pygame.sprite.Group()
    npc_2_group.add(npc_2)

    npc_3 = NPC_BUILDING("SPRITE\pNPC\pcl_men.png", 1250, 417, "Рин", (14, 41, 75))
    npc_3_group = pygame.sprite.Group()
    npc_3_group.add(npc_3)

    img_apple_group_2 = pygame.sprite.Group()
    img_apple_group_2.add(Stop_2_Apple("SPRITE\APPLE_HILL.png", (1250, 640)))

    button_menu_img = pygame.image.load("SPRITE\EXIT_MENU_BUTTON.png")
    button_menu_img_tr = pygame.transform.scale(button_menu_img, (50, 50))

    rect_but_menu = button_menu_img_tr.get_rect()
    rect_but_menu.x = 10
    rect_but_menu.y = 10

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_but_menu[0] < event.pos[0] < rect_but_menu[0] + rect_but_menu[2] and rect_but_menu[1] < \
                        event.pos[1] < rect_but_menu[1] + rect_but_menu[3]:
                    return start_menu()
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
        npc_1_group.draw(screen)
        npc_2_group.draw(screen)
        npc_3_group.draw(screen)
        men_group.draw(screen)
        screen_local_2.blit(gg_2.image, gg_2.rect)
        screen_local_2.blit(button_menu_img_tr, (10, 10))

        if pygame.sprite.spritecollideany(gg_2, other_sprite) and sdegfoin1:
            music_location_2.stop()
            a = start_fn(event, 2)
            one = Live_hide_cl()
            two = Death_hide_cl()
            l_d1 = (one.live_print(), two.death_print())
            if a:
                l_d1 = (False, False)
                ON_2 = False
                Death_fLag = False
                loading_death()

        if pygame.sprite.spritecollideany(gg_2, men_group) and key[pygame.K_RETURN]:
            menshik.dialog("")
            menshik.click_update()

        if pygame.sprite.spritecollideany(gg_2, other_sprite_2):
            music_location_2.stop()
            start_location_3()
            running = False
        if pygame.sprite.spritecollideany(gg_2, other_sprite_exit):
            music_location_2.stop()
            location_1 = True
            start_location_1()
            running = False
        if pygame.sprite.spritecollideany(gg_2, npc_1_group) and key[pygame.K_RETURN]:
            npc_1.dialog("Ха..ха..ха.. NТебе здесь не рады..")
            npc_1.click_update()
        if pygame.sprite.spritecollideany(gg_2, npc_2_group) and key[pygame.K_RETURN]:
            npc_2.dialog(
                "Ух.. Это ты..NЗачем ты вернулся?NТы должен был Nсгнить в той пещере NА, ты не понимаешь? NВидимо у тебя амнезия NВсе здесь боятся твоего Nпрошлого...")
            npc_2.click_update()
        if pygame.sprite.spritecollideany(gg_2, npc_3_group) and key[pygame.K_RETURN]:
            npc_3.dialog(
                "Здравствуй путник NЯ недавно приехал сюда. NЗдесь совершенно нет никаких Nмонстров, хотя кто-то Nговорит, что здесь есть люди, Nкоторые могут видеть призраков")
            npc_3.click_update()

        if l_d1[0] == True or l_d1[1] == True:
            sdegfoin1 = False
        if (l_d1[0] == False and l_d1[1] == False):
            screen.blit(img_hide_scale, (1920 // 2, 1080 // 2 + 80))

        if ON_2:
            img_apple_group_2.draw(screen)

        if pygame.sprite.spritecollideany(gg_2, img_apple_group_2):
            ON_2 = False
            con = sqlite3.connect('SQL\Bag.db')
            cur = con.cursor()
            res = cur.execute("""update Bag
                                set Count = Count + 1
                                where Object = 'Яблоко'""").fetchall()
            con.commit()
            con.close()
        pygame.display.flip()
        clock.tick(60)


class Stop_2_Apple(pygame.sprite.Sprite):
    def __init__(self, filename, coord):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]


def start_location_1():
    update(one=True)
    global location_1, gg, Death_fLag, go_or_no, l_d, ON, enter, music_location_1
    running = True
    x, y = 0, 0
    infoObject = pygame.display.Info()
    enter = False
    screen.fill((0, 0, 0))
    top_sprites = pygame.sprite.Group()
    bottom_sprites = pygame.sprite.Group()
    right_sprites = pygame.sprite.Group()
    left_sprites = pygame.sprite.Group()
    left_sprites.add(Stop('SPRITE\location_1c0.png', (-50, 0), 'l'))
    top_sprites.add(Stop('SPRITE\location_1c1.png', (0, 50), 't'))
    bottom_sprites.add(Stop('SPRITE\location_1c2.png', (0, infoObject.current_h // 3 * 2 + 70), 'b'))
    gg = Heroy(top=top_sprites, bottom=bottom_sprites, right=right_sprites, left=left_sprites)
    if location_1:
        gg.rect.x = 1800
        gg.rect.y = 572
        location_1 = False
    sdegfoin = True
    clock = pygame.time.Clock()
    img = pygame.transform.scale(pygame.image.load("location_1\location_1.png").convert_alpha(), (2048, 1024))
    top_sprites.draw(screen)
    bottom_sprites.draw(screen)
    right_sprites.draw(screen)
    left_sprites.draw(screen)
    other_sprite = pygame.sprite.Group()
    other_sprite.add(Stop_2("Hide_1.png", (1920 // 2 + 5, 1080 // 2)))
    other_sprite_2 = pygame.sprite.Group()
    other_sprite_2.add(Stop_2("SPRITE\VIXOD_LOC.png", (1915, 485)))
    img_hide = pygame.image.load("SPRITE\HIDE_1_BACKGROUND.png")
    img_hide_scale = pygame.transform.scale(img_hide, (100, 100))
    img_apple_group = pygame.sprite.Group()
    img_apple_group.add(Stop_2_Apple("SPRITE\APPLE_HILL.png", (280, 720)))

    shiza_npc_1 = NPC_BUILDING_SHIZA("SPRITE\Shiza_01.png", 360, 680, "???", (200, 200, 200))
    shiza_npc_1_group = pygame.sprite.Group()
    shiza_npc_1_group.add(shiza_npc_1)

    button_menu_img = pygame.image.load("SPRITE\EXIT_MENU_BUTTON.png")
    button_menu_img_tr = pygame.transform.scale(button_menu_img, (50, 50))

    rect_but_menu = button_menu_img_tr.get_rect()
    rect_but_menu.x = 10
    rect_but_menu.y = 10

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_but_menu[0] < event.pos[0] < rect_but_menu[0] + rect_but_menu[2] and rect_but_menu[1] < \
                        event.pos[1] < rect_but_menu[1] + rect_but_menu[3]:
                    return start_menu()
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
        screen.blit(button_menu_img_tr, (10, 10))
        if pygame.sprite.spritecollideany(gg, other_sprite) and sdegfoin:
            music_location_1.stop()
            a = start_fn(event, 1)
            one = Live_hide_cl()
            two = Death_hide_cl()
            l_d = (one.live_print(), two.death_print())
            if a:
                l_d = (False, False)
                ON = False
                Death_fLag = False
                loading_death()
                running = False
        if pygame.sprite.spritecollideany(gg, other_sprite_2):
            music_location_1.stop()
            start_location_2()
            running = False
        if l_d[0] == True or l_d[1] == True:
            sdegfoin = False
        if (l_d[0] == False and l_d[1] == False):
            screen.blit(img_hide_scale, (1920 // 2, 1080 // 2))
        if ON:
            img_apple_group.draw(screen)
        if pygame.sprite.spritecollideany(gg, img_apple_group):
            ON = False
            con = sqlite3.connect('SQL\Bag.db')
            cur = con.cursor()
            res = cur.execute("""update Bag
                                set Count = Count + 1
                                where Object = 'Яблоко'""").fetchall()
            con.commit()
            con.close()

        shiza_npc_1_group.draw(screen)
        if pygame.sprite.spritecollideany(gg, shiza_npc_1_group) and key[pygame.K_RETURN]:
            shiza_npc_1.dialog(
                "Я не сомневался что ты проснёшся NЗа то время пока ты спал NТы успел растерять все силы. NДля начала возьми это яблоко NЭто позволит тебе NПожить подольше чем остальные. NЗатем NСразись вон с тем призраком. NЭто предаст тебе NУверенности в бою! NМне уже пора идти... NДумаю мы ещё свидимся...")
            shiza_npc_1.click_update()

        pygame.display.flip()
        clock.tick(60)
    con = sqlite3.connect('SQL\Bag.db')
    cur = con.cursor()
    res = cur.execute("""update Bag
                        set Count = 0""").fetchall()
    con.commit()
    con.close()


start_menu()

pygame.quit()