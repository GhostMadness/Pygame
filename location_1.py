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
l_d = (False, False)

def loading_death():
    if __name__ == "__main__":
        pygame.init()
        pygame.display.set_caption("Phantom")
        size = width, height = 1920, 1080
        screen = pygame.display.set_mode(size)
        image_loading = pygame.image.load("SPRITE\APPLE_HILL.png")
        image_player = pygame.image.load("SPRITE\гг.png")
        music = pygame.mixer.Sound('MUSIC\WHAT\ZVEK_KYCANIA.mp3')
        angle = 0
        running = True
        width_line = 0
        text_loading = "Загрузка"
        schet = 0
        apple_x = 2000
        a = True
        b = False
        schet_2 = -30
        schet_3 = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    print(event.pos)
            screen.fill((0, 0, 0))

            font = pygame.font.Font(None, 50)
            myfont = pygame.font.SysFont("SimSun", 15)
            text = font.render(text_loading, True, (100, 255, 100))
            text_x = 51
            text_y = 850
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))


            pygame.draw.rect(screen, (255, 255, 255), (51, 887, width_line, 50))

            screen.blit(image_player, (1920 // 2 - 100, 1080 // 2 - 100))
            if apple_x >= 1920 // 2:
                screen.blit(image_loading, (apple_x, 1080 // 2- 100))
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
            text_hill_y = schet_2
            text_hill_w = text_hill.get_width()
            text_hill_h = text_hill.get_height()

            if a == False and schet_2 != 400:
                schet_2 += 2
            if schet_2 >= 400:
                text_ok = font.render("НЕ СДАВАЙСЯ", True, (0, 200, 0))
                text_ok_x = 1920 // 2 - 50
                text_ok_y = 800
                text_ok_w = text_ok.get_width()
                text_ok_h = text_ok.get_height()
                screen.blit(text_ok, (text_ok_x, text_ok_y))
            if schet_3 <= 500:
                screen.blit(text_hill, (text_hill_x, schet_2))
            if schet_2 == 400:
                schet_3 += 2
            pygame.display.flip()

def loading():
    if __name__ == "__main__":
        global image_loading
        pygame.init()
        pygame.display.set_caption("Phantom")
        size = width, height = 1920, 1080
        screen = pygame.display.set_mode(size)
        image_loading = pygame.image.load("SPRITE\BOMB_ENEMY.png")
        angle = 0
        running = True
        width_line = 0
        text_loading = "Загрузка"
        schet = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    print(event.pos)
            screen.fill((0, 0, 0))

            font = pygame.font.Font(None, 50)
            myfont = pygame.font.SysFont("SimSun", 15)
            text = font.render(text_loading, True, (100, 255, 100))
            text_x = 51
            text_y = 850
            text_w = text.get_width()
            text_h = text.get_height()
            screen.blit(text, (text_x, text_y))

            pos_x = random.randint(1920 // 2 - 10, 1920 // 2 + 10)
            screen.blit(image_loading, (pos_x - 50, 1080 // 2 - 50))
            pygame.draw.rect(screen, (255, 255, 255), (51, 887, width_line, 50))
            if width_line >= 1800:
                time.sleep(1)
                width_line += 10
                time.sleep(0.5)
                start_location_1()
            width_line += 1
            if schet == 100:
                if text_loading == "Загрузка...":
                    text_loading = "Загрузка"
                else:
                    text_loading = text_loading + '.'
                schet = 0
            schet += 1
            pygame.display.flip()

def start_menu():
    if __name__ == "__main__":
        pygame.init()
        pygame.display.set_caption("Phantom")
        size = width, height = 1920, 1080
        screen = pygame.display.set_mode(size)
        music = pygame.mixer.Sound('MUSIC\FIRST\MENU.mp3')
        music.set_volume(0.05)
        music.play(-1)
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
                elif event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    print(str((x, y)))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if rect_1[0] < event.pos[0] < rect_1[0] + rect_1[2] and rect_1[1] < event.pos[1] < rect_1[1] + rect_1[3]:
                        running = False
                    if rect_2[0] < event.pos[0] < rect_2[0] + rect_2[2] and rect_2[1] < event.pos[1] < rect_2[1] + rect_2[3]:
                        print("baba boy")
                    if rect_3[0] < event.pos[0] < rect_3[0] + rect_3[2] and rect_3[1] < event.pos[1] < rect_3[1] + rect_3[3]:
                        music.stop()
                        loading()

            screen.fill((0, 0, 0))
            screen.blit(IMG_MENU, (0, 0))
            screen.blit(IMG_PLAY_BUTTON, (43, 70 + 50))
            screen.blit(IMG_SETTING_BUTTON, (43, 345 + 50))
            screen.blit(IMG_EXIT_BUTTON, (43, 620 + 50))
            pygame.display.flip()

class NPC_BUILDING(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, nickname, rgb_nickname):
        super().__init__()

        self.name = nickname
        self.rgb_nickname = rgb_nickname

        self.image= pygame.image.load(filename).convert_alpha()
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
        self.rect_dialog_window.y = 760
        
    def click_update(self):
        if self.schet >= len(self.text_res):
            if self.name == 'Рин':
                self.text_name = self.font.render(self.name, False, self.rgb_nickname)
                self.text = self.font.render("До скорой встречи путник!", True, (255, 255, 255))
                screen.blit(self.text_name, (620, 720))
                screen.blit(self.image_dialog_window, self.rect_dialog_window)
                screen.blit(self.text, (620, 770))
                pygame.display.flip()
                time.sleep(3)
                return

            self.text_name = self.font.render(self.name, False, self.rgb_nickname)
            self.text = self.font.render("Мне больше нечего тебе сказать", True, (255, 255, 255))
            screen.blit(self.text_name, (620, 720))
            screen.blit(self.image_dialog_window, self.rect_dialog_window)
            screen.blit(self.text, (620, 770))
            pygame.display.flip()
            time.sleep(3)
            screen.blit(self.text_name, (620, 720))
            self.text = self.font.render("урод!", True, (255, 255, 255))
            screen.blit(self.image_dialog_window, self.rect_dialog_window)
            screen.blit(self.text, (620, 770))
            pygame.display.flip()
            time.sleep(1)
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
            time.sleep(3)
        
        #ПИСАТЬ КАЖДОЕ НОВОЕ СЛОВОСОЧЕТАНИЕ ЧЕРЕЗ N КОГДА ПЕРЕДАЁШЬ В ФУНКЦИЮ ТЕКСТ ПЕРСОНАЖА!!! ПРИМЕР СНИЗУ!!!


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
            
            if self.bottom_sprites == None:
                self.bottom_sprites = pygame.sprite.Group()
        
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

        top_sprite = pygame.sprite.Group()
        left_sprite = pygame.sprite.Group()

        top_sprite.add(Stop_2("location_house\sprite_collide\ottom_grass.png", (0, 265)))
        left_sprite.add(Stop_2("location_house\sprite_collide\ght_grass.png", (830, 0)))

        music = pygame.mixer.Sound('MUSIC\FIRST\LOCATION_3_1.mp3')
        music.set_volume(0.1)
        music.play(-1)

        clock = pygame.time.Clock()

        gg_3 = Heroy(top=top_sprite, left=left_sprite, x=550, y=100)
        if location_3:
            gg_3.rect.x = 1230
            gg_3.rect.y = 500
            location_3 = False

        other_sprite_2 = pygame.sprite.Group()
        other_sprite_2.add(Stop_2("SPRITE\VIXOD_LOC.png", (1134, 86)))

        other_sprite_exit = pygame.sprite.Group()
        other_sprite_exit.add(Stop_2("SPRITE\VIXOD_LOC.png", (-350, 380)))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
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
        other_sprite_2.add(Stop_2("SPRITE\VIXOD_LOC.png", (1919, 396)))

        other_sprite_exit = pygame.sprite.Group()
        other_sprite_exit.add(Stop_2("SPRITE\VIXOD_LOC.png", (-350, 384)))

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
        ON = True

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
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
            screen_local_2.blit(gg_2.image, gg_2.rect)

            if pygame.sprite.spritecollideany(gg_2, other_sprite_2):
                music.stop()
                start_location_3()
            if pygame.sprite.spritecollideany(gg_2, other_sprite_exit):
                music.stop()
                location_1 = True
                start_location_1()
            if pygame.sprite.spritecollideany(gg_2, npc_1_group) and key[pygame.K_RETURN]:
                    npc_1.dialog("Пошёл вон отсюда NПока все мозги не выбил!")
                    npc_1.click_update()
            if pygame.sprite.spritecollideany(gg_2, npc_2_group) and key[pygame.K_RETURN]:
                    npc_2.dialog("Я вЕлИкИй Из СвОеГо РоДа NВ нАсЛеДиЕ мНе ОсТаЛсЯ NэТоТ бОжЕсТвЕнНыЙ NкОсТюМ! NКаК я ПоГлЕжУ тЫ NиЗ нИзШиХ сЛоЁв ОбЩеСтВа! NТы Не иМеЕшь ПрАвА NНаХоДиТьСя РяДоМ сО мНоЙ! NУбИрАйСя!")
                    npc_2.click_update()
            if pygame.sprite.spritecollideany(gg_2, npc_3_group) and key[pygame.K_RETURN]:
                    npc_3.dialog("Здравствуй путник NЯ недавно приехал сюда. NИногда я вижу странных существ NЕсли видишь не мешкая убивай NОни портят репутацию городу NДо скорых встреч!")
                    npc_3.click_update()
            
            if ON: 
                img_apple_group_2.draw(screen)
            if pygame.sprite.spritecollideany(gg_2, img_apple_group_2):
                ON = False
                con = sqlite3.connect('SQL\Bag.db')
                cur = con.cursor()
                res = cur.execute("""update Bag
                                    set Count = Count + 1
                                    where Object = 'Яблоко'""").fetchall()
                con.commit()
                con.close()

            pygame.display.flip()
            clock.tick(60)
    pygame.quit()

class Stop_2(pygame.sprite.Sprite):
    def __init__(self, filename, coord):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]

class Stop_2_Apple(pygame.sprite.Sprite):
    def __init__(self, filename, coord):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]

def start_location_1():
    if __name__ == '__main__':
        global location_1, gg, Death_fLag, go_or_no, l_d
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


        sh1 = Shiza()

        sdegfoin = True

        clock = pygame.time.Clock()

        img = pygame.transform.scale(pygame.image.load("location_1\location_1.png").convert_alpha(), (2048, 1024))

        sc1 = pygame.Surface((2048, 1024))

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
        ON = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

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
                a = start_fn(event)
                one = Live_hide_cl()
                two = Death_hide_cl()
                l_d = (one.live_print(), two.death_print())
                if a:
                    #gg.rect.x = 324
                    #gg.rect.y = 571
                    l_d = (False, False)
                    ON = False
                    Death_fLag = False
                    #screen.blit(gg.image, gg.rect)
                    loading_death()

            if pygame.sprite.spritecollideany(gg, other_sprite_2):
                music.stop()
                start_location_2()
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

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
start_menu()