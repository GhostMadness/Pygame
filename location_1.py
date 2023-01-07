import pygame

Location_4_Flag = False


class Location_4():
    def start_location_4():
        global Location_4_Flag
        if __name__ == '__main__':
            class Heroy(pygame.sprite.Sprite):
                def __init__(self):
                    super().__init__()
                    infoObject = pygame.display.Info()
                    self.image= pygame.image.load('SPRITE\гг.png')
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    self.rect = self.image.get_rect()
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect.bottom = 1100
                    self.rect.right = 990

                    self.image_grass_bottom = pygame.image.load("location_house\sprite_collide\ottom_grass.png")
                    self.image_grass_right = pygame.image.load("location_house\sprite_collide\ght_grass.png")
                    
                
                def update(self):
                    pass
                
                def top(self):
                    global y
                    self.image= pygame.image.load('SPRITE\гг.png')
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    if not pygame.sprite.spritecollideany(self, bottom_sprite) and not pygame.sprite.spritecollideany(self, top_sprites):
                        self.rect.y -= 5
                
                def botton(self):
                    global y
                    self.image= pygame.image.load('SPRITE\гг.png')
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    if not pygame.sprite.spritecollideany(self, left_sprites):
                        self.rect.y += 5

                
                def right(self):
                    global x
                    self.image = pygame.image.load('SPRITE\гг_2.png')
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    if not pygame.sprite.spritecollideany(self, right_sprite) and not pygame.sprite.spritecollideany(self, top_sprites):
                        self.rect.x += 5

                
                def left(self):
                    global x
                    self.image = pygame.image.load('SPRITE\гг_1.png')
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    if not pygame.sprite.spritecollideany(self, left_sprites) and not pygame.sprite.spritecollideany(self, top_sprites):
                        self.rect.x -= 5

            class Stop(pygame.sprite.Sprite):
                def __init__(self, filename, coord):
                    super().__init__()
                    self.image = pygame.image.load(filename)
                    self.rect = self.image.get_rect()
                    self.rect.x = coord[0]
                    self.rect.y = coord[1]

            pygame.init()
            pygame.display.set_caption("Phantom")
            size = width, height = 1920, 1080
            screen = pygame.display.set_mode(size)

            image_background = pygame.image.load("location_5_men\RESULT\location_5_man.png")
            image_1 = pygame.image.load("location_5_men\RESULT\iblioteka.png")
            image_3 = pygame.image.load("location_5_men\RESULT\cover.png")
            image_4 = pygame.image.load("location_5_men\RESULT\oxes.png")
            image_5 = pygame.image.load("location_5_men\RESULT\object.png")

            image_npc_men = pygame.image.load("SPRITE\pNPC\Sprite-0001.png")
            image_npc_men_scale = pygame.transform.scale(image_npc_men, (100, 100))

            sc1 = pygame.Surface((1920, 1080))
            sc1.blit(image_background, (0, 0))
            sc1.blit(image_1, (0, 0))
            sc1.blit(image_3, (0, 0))
            sc1.blit(image_4, (0, 0))
            sc1.blit(image_5, (0, 0))
            sc1.blit(image_npc_men_scale, (200, 50))

            bottom_sprite = pygame.sprite.Group()
            right_sprite = pygame.sprite.Group()
            left_sprites = pygame.sprite.Group()
            top_sprites = pygame.sprite.Group()
            bottom_sprite.add(Stop("location_5_men\RESULT\iblioteka_bottom_collide.png", (1542, 220)))
            right_sprite.add(Stop("location_5_men\RESULT\iblioteka_right_collide.png", (1570, 8)))
            right_sprite.add(Stop("location_5_men\RESULT\iblioteka_other.png", (1670, 479)))
            left_sprites.add(Stop("location_5_men\RESULT\oxes_collide.png", (0, 913)))
            top_sprites.add(Stop("location_5_men\RESULT\object_collide.png", (895, 0)))

            music_4 = pygame.mixer.Sound('MUSIC\FIRST\HOME.mp3')

            clock = pygame.time.Clock()

            gg = Heroy()

            other_sprites_exit = pygame.sprite.Group()
            other_sprites_exit.add(Stop("SPRITE\VIXOD_LOC.png", (883, 1100)))

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

                music_4.set_volume(0.2)
                music_4.play(-1)

                if pygame.sprite.spritecollideany(gg, other_sprites_exit):
                    music_4.stop()
                    Location_4_Flag = True
                    Location_3.start_location_3()
                        
                pygame.display.flip()
                clock.tick(60)
        pygame.quit()



class Location_3():
    def __init__(self):
        pass


    def start_location_3():
        if __name__ == '__main__':
            global bottom_sprite, right_sprite
            global Location_4_Flag
            pygame.init()
            pygame.display.set_caption("Phantom")
            size = width, height = 1920, 1080
            screen_3 = pygame.display.set_mode(size)
            image_background = pygame.image.load("location_house\ckground.png")
            image_1 = pygame.image.load("location_house\location_3.png")
            image_2 = pygame.image.load("location_house\location_3_house.png")
            sc1 = pygame.Surface((1920, 1080))
            sc1.blit(image_background, (0, 0))
            sc1.blit(image_2, (0, 0))
            sc1.blit(image_1, (0, 0))


            class Heroy(pygame.sprite.Sprite):
                def __init__(self):
                    super().__init__()
                    global Location_4_Flag
                    infoObject = pygame.display.Info()
                    self.image= pygame.image.load('SPRITE\гг.png')
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    self.rect = self.image.get_rect()
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect.bottom = 570
                    self.rect.right = 100
                    if Location_4_Flag:
                        self.rect.bottom = 570
                        self.rect.right = 1350
                        Location_4_Flag = False

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
                    self.rect.x += 5

                
                def left(self):
                    global x
                    self.image = pygame.image.load('SPRITE\гг_1.png')
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    if not pygame.sprite.spritecollideany(self, right_sprite):
                        self.rect.x -= 5

            class Stop(pygame.sprite.Sprite):
                def __init__(self, filename, coord):
                    super().__init__()
                    self.image = pygame.image.load(filename)
                    self.rect = self.image.get_rect()
                    self.rect.x = coord[0]
                    self.rect.y = coord[1]




            bottom_sprite = pygame.sprite.Group()
            right_sprite = pygame.sprite.Group()
            bottom_sprite.add(Stop("location_house\sprite_collide\ottom_grass.png", (0, 265)))
            right_sprite.add(Stop("location_house\sprite_collide\ght_grass.png", (830, 0)))

            music_3 = pygame.mixer.Sound('MUSIC\FIRST\LOCATION_3_1.mp3')

            clock = pygame.time.Clock()

            gg_3= Heroy()

            other_sprites_exit = pygame.sprite.Group()
            other_sprites_exit.add(Stop("SPRITE\VIXOD_LOC.png", (-400, 535)))

            other_sprites = pygame.sprite.Group()
            other_sprites.add(Stop("SPRITE\VIXOD_LOC.png", (1236, 50)))

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
                screen_3.blit(sc1, (0, 0))
                screen_3.blit(gg_3.image, gg_3.rect)

                music_3.set_volume(0.2)
                music_3.play(-1)
                
                if pygame.sprite.spritecollideany(gg_3, other_sprites_exit):
                    music_3.stop()
                    Location_2.start_location_2()
                
                if pygame.sprite.spritecollideany(gg_3, other_sprites):
                    music_3.stop()
                    Location_4.start_location_4()

                pygame.display.flip()
                clock.tick(60)
        pygame.quit()


class Location_2():
    def __init__(self):
        pass

    def start_location_2():
        if __name__ == '__main__':
            pygame.init()

            class Heroy(pygame.sprite.Sprite):
                def __init__(self):
                    super().__init__()
                    class Stop(pygame.sprite.Sprite):
                        def __init__(self, filename, coord):
                            super().__init__()
                            self.image = pygame.image.load(filename)
                            self.rect = self.image.get_rect()
                            self.rect.x = coord[0]
                            self.rect.y = coord[1]


                    infoObject = pygame.display.Info()
                    self.image= pygame.image.load('SPRITE\гг.png')
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    self.rect = self.image.get_rect()
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect.bottom = 600
                    self.rect.right = 100
                    self.bottom_sprites_2 = pygame.sprite.Group()
                    self.top_sprites_2 = pygame.sprite.Group()
                    self.bottom_sprites_2.add(Stop("location_4\esult_sprite\house_2.png", (0, 0)))
                    self.top_sprites_2.add(Stop("location_4\esult_sprite\ground_bottom.png", (0, 716)))
                    
            
                def update(self):
                    pass
                
                def top(self):
                    global y
                    self.image= pygame.image.load('SPRITE\гг.png')
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    if not pygame.sprite.spritecollideany(self, self.bottom_sprites_2):
                        self.rect.y -= 5
                
                def botton(self):
                    global y
                    self.image= pygame.image.load('SPRITE\гг.png')
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    if not pygame.sprite.spritecollideany(self, self.top_sprites_2):
                        self.rect.y += 5

                
                def right(self):
                    global x
                    self.image = pygame.image.load('SPRITE\гг_2.png')
                    self.image = pygame.transform.scale(self.image, (100, 100))
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

            pygame.display.set_caption("Phantom")
            size = width, height = 1920, 1080
            screen_local_2 = pygame.display.set_mode(size)
            image_background = pygame.image.load("location_4\esult_sprite\map.png")
            image_1 = pygame.image.load("location_4\esult_sprite\house.png")
            image_2 = pygame.image.load("location_4\esult_sprite\other.png")

            image_npc_1 = pygame.image.load("SPRITE\pNPC\selski_men.png")
            image_npc_1_scale = pygame.transform.scale(image_npc_1, (100, 100))

            sc1 = pygame.Surface((1920, 1080))
            sc1.blit(image_background, (0, 0))
            sc1.blit(image_2, (0, 0))
            sc1.blit(image_1, (0, 0))
            sc1.blit(image_npc_1_scale, (672, 420))

            music_2 = pygame.mixer.Sound('MUSIC\DOUBLE\location_2.mp3')

            clock = pygame.time.Clock()

            gg_2 = Heroy()
            

            other_sprites = pygame.sprite.Group()
            other_sprites.add(Stop("SPRITE\VIXOD_LOC.png", (1950, 543)))

            other_sprites_exit = pygame.sprite.Group()
            other_sprites_exit.add(Stop("SPRITE\VIXOD_LOC.png", (-400, 535)))

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

                music_2.set_volume(0.2)
                music_2.play(-1)

                if pygame.sprite.spritecollideany(gg_2, other_sprites):
                    music_2.stop()
                    Location_3.start_location_3()

                if pygame.sprite.spritecollideany(gg_2, other_sprites_exit):
                    music_2.stop()
                    Location_1.start_location_1()

                pygame.display.flip()
                clock.tick(60)
        pygame.quit()
        #location_2



class Location_1():
    def start_location_1():
        if __name__ == '__main__':
            pygame.init()
            global left_sprites, right_sprites, top_sprites, bottom_sprites, screen, img, gg, sh1, music, x, y, image_background, image_1, image_2
            class Heroy(pygame.sprite.Sprite):
                def __init__(self):
                    super().__init__()
                    self.image= pygame.image.load('SPRITE\гг.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    self.rect = self.image.get_rect()
                    self.mask = pygame.mask.from_surface(self.image)
                    self.rect.bottom = 600
                    self.rect.right = 400
                
                def update(self):
                    pass
                
                def top(self):
                    global y
                    self.image= pygame.image.load('SPRITE\гг.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    if not pygame.sprite.spritecollideany(self, top_sprites):
                        self.rect.y -= 5
                
                def botton(self):
                    global y
                    self.image= pygame.image.load('SPRITE\гг.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    if not pygame.sprite.spritecollideany(self, bottom_sprites):
                        self.rect.y += 5
                
                def right(self):
                    global x
                    self.image = pygame.image.load('SPRITE\гг_2.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    if not pygame.sprite.spritecollideany(self, right_sprites):
                        self.rect.x += 5
                
                def left(self):
                    global x
                    self.image = pygame.image.load('SPRITE\гг_1.png').convert_alpha()
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    if not pygame.sprite.spritecollideany(self, left_sprites):
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

            class Stop_local_2(pygame.sprite.Sprite):
                def __init__(self, filename, coord):
                    super().__init__()
                    self.image = pygame.image.load(filename)
                    self.rect = self.image.get_rect()
                    self.rect.x = coord[0]
                    self.rect.y = coord[1]

            def local_1():
                music.set_volume(0.2)
                music.play(-1)
                screen.blit(img, (x, y))
                screen.blit(gg.image, gg.rect)
                screen.blit(sh1.image, sh1.rect)
                pygame.display.flip()


            running = True
            x, y = 0, 0
            pygame.display.set_caption("Phantom")
            infoObject = pygame.display.Info()
            width, height = 1920, 1080
            screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
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

            
            gg = Heroy()
            
            sh1 = Shiza()
            
            clock = pygame.time.Clock()

            img = pygame.transform.scale(pygame.image.load("location_1\location_1.png").convert_alpha(), (2048, 1024))
            
            sc1 = pygame.Surface((2048, 1024))
            
            top_sprites.draw(screen)
            bottom_sprites.draw(screen)
            right_sprites.draw(screen)
            left_sprites.draw(screen)

            other_sprites = pygame.sprite.Group()
            other_sprites.add(Stop_local_2("SPRITE\VIXOD_LOC.png", (1950, 590)))

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
                local_1()
                if pygame.sprite.spritecollideany(gg, other_sprites):
                    music.stop()
                    Location_2.start_location_2()
                clock.tick(60)
            pygame.quit()

Location_1.start_location_1()