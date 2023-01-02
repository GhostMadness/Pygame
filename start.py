import pygame

class War():
    def __init__(self):
        pass
        

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1920, 1080
    
    screen = pygame.display.set_mode(size)
    
    screen.fill((0, 0, 0))
    
    image1 = pygame.image.load('SPRITE\Hide_1.png')
    
    screen.blit(image1, (800, 200))
    pygame.display.flip()
    
    image2 = pygame.image.load('SPRITE\для update-export.png')
    
    screen.blit(image2, (750, 500))
    pygame.display.flip()
    
    image3 = pygame.image.load('SPRITE\сердце-export.png')
    
    screen.blit(image3, (750, 500))
    pygame.display.update()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()