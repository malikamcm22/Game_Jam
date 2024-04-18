import pygame, sys, time
from settings import *
from bar import Bar

pygame.init()

class Student(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH//2 + 150, HEIGHT//2)

    def move(self):
        pressed_keys =pygame.key.get_pressed()
        if self.rect.left >= 0 and self.rect.right <= WIDTH:
          if pressed_keys[pygame.K_LEFT] and self.rect.left > 5:
              self.rect.move_ip(-5, 0)
          if pressed_keys[pygame.K_RIGHT] and self.rect.right < WIDTH - 5:
              self.rect.move_ip(5, 0)
        if self.rect.top >= 0 and self.rect.bottom <= HEIGHT:
          if pressed_keys[pygame.K_UP] and self.rect.top > 5:
              self.rect.move_ip(0, -5)
          if pressed_keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT - 5:
              self.rect.move_ip(0, 5)  

    def draw(self, surface):
        surface.blit(self.image, self.rect)

S1 = Student()

# кнопки меню
unpbplay = pygame.image.load("buttons/unpbplay.png")
unpbexit = pygame.image.load("buttons/unpbexit.png")
unpbinfo = pygame.image.load("buttons/unpbinfo.png")
pbplay = pygame.image.load("buttons/pbplay.png")
pbexit = pygame.image.load("buttons/pbexit.png")
pbinfo = pygame.image.load("buttons/pbinfo.png")

#спрайты зданий
kbtu = pygame.image.load("kbtuu.png")
kbtu_small = pygame.transform.scale(kbtu, (350, 200))
kbtu_small_rect = kbtu_small.get_rect()
kbtu_small_rect.center = (625,150)

#внутренности зданий
dormitory = pygame.image.load("dormitory.png")
dormitory_big = pygame.transform.scale(dormitory, (WIDTH, HEIGHT))
dormitory_big_rect = dormitory_big.get_rect()
dormitory_big_rect.center = (WIDTH//2, HEIGHT//2)

#коррекция масштаба картинок и их rectangles
unpbplay_small = pygame.transform.scale(unpbplay,(350,150))
unpbplay_small_rect = unpbplay_small.get_rect()
unpbplay_small_rect.center = (750,150)
unpbexit_small = pygame.transform.scale(unpbexit,(350,150))
unpbexit_small_rect = unpbexit_small.get_rect()
unpbexit_small_rect.center = (750,300)
unpbinfo_small = pygame.transform.scale(unpbinfo,(350,150))
unpbinfo_small_rect = unpbinfo_small.get_rect()
unpbinfo_small_rect.center = (750,450)

pbplay_small = pygame.transform.scale(pbplay,(350,150))
pbplay_small_rect = pbplay_small.get_rect()
pbplay_small_rect.center = (750,150)
pbexit_small = pygame.transform.scale(pbexit,(350,150))
pbexit_small_rect = pbexit_small.get_rect()
pbexit_small_rect.center = (750,300)
pbinfo_small = pygame.transform.scale(pbinfo,(350,150))
pbinfo_small_rect = pbinfo_small.get_rect()
pbinfo_small_rect.center = (750,450)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

x_margin_for_bars = 30

knowledge_bar = Bar(x_margin_for_bars,10,200,25,100,BROWN)
knowledge_bar.unit = 0
sleep_bar = Bar(x_margin_for_bars,45,200,25,100,BLUE)
satiety_bar = Bar(x_margin_for_bars,80,200,25,100,RED)
happiness_bar = Bar(x_margin_for_bars,115,200,25,100,YELLOW)

gaming = False


while True:
    clock.tick(FPS)
    pressed = pygame.key.get_pressed() 
    screen.fill(BG_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if S1.rect.colliderect(kbtu_small_rect):
            if knowledge_bar.unit<100:
                if knowledge_bar.unit+40>=100:
                    knowledge_bar.unit = 100
                    screen.fill("red")
                    pygame.display.flip()
                    time.sleep(2)
                    pygame.quit()
                    sys.exit()
                else:
                    knowledge_bar.unit += 40
                if sleep_bar.unit>=2:
                    sleep_bar.unit-=2
                if satiety_bar.unit>=2:
                    satiety_bar.unit-=2
                if happiness_bar.unit>=2:
                    happiness_bar.unit-=2 

            screen.blit(dormitory_big,dormitory_big_rect)
            pygame.display.flip()
            
            
               
            S1.rect.center = (625, HEIGHT//2)   

            time.sleep(2) 
    

    #добавляю выбор кнопок мышкой (для info пока не добавлял)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                if unpbplay_small_rect.collidepoint(mouse_pos):            
                    gaming = True
                elif unpbexit_small_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
    
        
    if gaming:

        pygame.draw.rect(screen, BLACK, (0,0, CHARACTERISTICS_BAR_WIDTH, CHARACTERISTICS_BAR_HEIGHT))

        #после добавки спрайтов зданий эти прямоугольники нужно убрать
        pygame.draw.rect(screen, WHITE, (CHARACTERISTICS_BAR_WIDTH+200,50, 350, 200))
        pygame.draw.rect(screen, BLUE, (CHARACTERISTICS_BAR_WIDTH+750,50, 350, 200))
        pygame.draw.rect(screen, BLUE, (CHARACTERISTICS_BAR_WIDTH+200,450, 350, 200))
        pygame.draw.rect(screen, BLUE, (CHARACTERISTICS_BAR_WIDTH+750,450, 350, 200))
        
        #здания
        screen.blit(kbtu_small, kbtu_small_rect)
        #screen.blit(dormitory_big, dormitory_big_rect)

        screen.blit(S1.image, S1.rect)
        S1.move()


        knowledge_bar.draw(screen)
        sleep_bar.draw(screen)
        satiety_bar.draw(screen)
        happiness_bar.draw(screen)

        #проверка коллизий и действия

            

              


    else:
        screen.blit(unpbplay_small,unpbplay_small_rect)
        screen.blit(unpbexit_small, unpbexit_small_rect)
        screen.blit(unpbinfo_small, unpbinfo_small_rect)   

    

    pygame.display.flip() 
    