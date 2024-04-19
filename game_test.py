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
        self.direction = "right"

    def move(self):
        pressed_keys =pygame.key.get_pressed()
        if self.rect.left >= 0 and self.rect.right <= WIDTH:
          if pressed_keys[pygame.K_LEFT] and self.rect.left > 5:
              self.direction = "right"
              self.rect.move_ip(-5, 0)
          if pressed_keys[pygame.K_RIGHT] and self.rect.right < WIDTH - 5:
              self.direction = "left"
              self.rect.move_ip(5, 0)
        if self.rect.top >= 0 and self.rect.bottom <= HEIGHT:
          if pressed_keys[pygame.K_UP] and self.rect.top > 5:
              self.direction = "up"
              self.rect.move_ip(0, -5)
          if pressed_keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT - 5:
              self.direction = "down"
              self.rect.move_ip(0, 5)  

    def draw(self, surface):
        if self.direction == "up":
            rotated_image = self.image
        elif self.direction == "down":
            rotated_image = pygame.transform.rotate(self.image, 180)
        elif self.direction == "right":
            rotated_image = pygame.transform.rotate(self.image, 90)
        elif self.direction == "left":
            rotated_image = pygame.transform.rotate(self.image, -90)
        surface.blit(rotated_image, self.rect)
        #surface.blit(self.image, self.rect)

S1 = Student()

# кнопки меню
unpbplay = pygame.image.load("buttons/unpbplay.png")
unpbexit = pygame.image.load("buttons/unpbexit.png")
unpbinfo = pygame.image.load("buttons/unpbinfo.png")
pbplay = pygame.image.load("buttons/pbplay.png")
pbexit = pygame.image.load("buttons/pbexit.png")
pbinfo = pygame.image.load("buttons/pbinfo.png")

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

#спрайты зданий снаружи
kbtu_outside = pygame.image.load("kbtuu.png")
kbtu_outside_small = pygame.transform.scale(kbtu_outside, (350, 200))
kbtu_outside_small_rect = kbtu_outside_small.get_rect()
kbtu_outside_small_rect.center = (625,150)
dormitory_outside = pygame.image.load("dormOutside.png")
dormitory_outside_small = pygame.transform.scale(dormitory_outside, (350, 200))
dormitory_outside_small_rect = dormitory_outside_small.get_rect()
dormitory_outside_small_rect.center = (1175,150)

#внутренности зданий
kbtu_inside = pygame.image.load("kbtu-inside-pixilart (1).png")
kbtu_inside = pygame.transform.scale(kbtu_inside, (WIDTH, HEIGHT))
kbtu_inside_rect = kbtu_inside.get_rect()
kbtu_inside_rect.center = (WIDTH//2, HEIGHT//2)
dormitory_inside = pygame.image.load("dormitory.png")
dormitory_inside = pygame.transform.scale(dormitory_inside, (WIDTH, HEIGHT))
dormitory_inside_rect = dormitory_inside.get_rect()
dormitory_inside_rect.center = (WIDTH//2, HEIGHT//2)

#картинки характеристик студента
knowledge = pygame.image.load("knowledge.png")
knowledge = pygame.transform.scale(knowledge, (40, 40))
knowledge_position_rect = knowledge.get_rect()
knowledge_position_rect.center = (15, 20)
sleep = pygame.image.load("sleep.png")
sleep = pygame.transform.scale(sleep, (120, 120))
sleep_position_rect = sleep.get_rect()
sleep_position_rect.center = (35, 75)
satiety = pygame.image.load("satiety.png")
satiety = pygame.transform.scale(satiety, (70, 70))
satiety_position_rect = satiety.get_rect()
satiety_position_rect.center = (15, 90)

#звуки кнопок и зданий
knopka = pygame.mixer.Sound("zvuk-knopki.mp3")
magazin_sound = pygame.mixer.Sound("cash_register.mp3")
kbtu_sound = pygame.mixer.Sound("bell.mp3")
dormitory_sound = pygame.mixer.Sound("hrap.mp3")

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

x_margin_for_bars = 30
knowledge_bar = Bar(x_margin_for_bars,10,200,25,100,BROWN)
knowledge_bar.unit = 0
sleep_bar = Bar(x_margin_for_bars,45,200,25,100,BLUE)
satiety_bar = Bar(x_margin_for_bars,80,200,25,100,RED)
happiness_bar = Bar(x_margin_for_bars,115,200,25,100,YELLOW)

#Ingame timer
game_time_sec = -1
game_time_min = 0
game_time_fonts = pygame.font.SysFont('comicsansms', 30)
game_time_text = game_time_fonts.render(f"Time: {game_time_min}:{game_time_sec}", True, (0, 0, 0))
game_time_rect = game_time_text.get_rect()
game_time_rect.center = (120 , 240)


#Time counter
TIME_COUNT_SEC = pygame.USEREVENT + 2
pygame.time.set_timer(TIME_COUNT_SEC, 1000)

#кнопки подтверждения
arrow_up = pygame.image.load('arrow up.png')
arrow_down = pygame.image.load('arrow down.png')
arrow_up_rect = arrow_up.get_rect()
arrow_up_rect.center = (685, 155)
arrow_down_rect = arrow_down.get_rect()
arrow_down_rect.center = (695, 155)
"""
flag_kbtu = 0
flag_kbtu2 = 0
"""
gaming = False
course_counter = 1
flag_buttons = 0
while True:
    clock.tick(FPS)
    pressed = pygame.key.get_pressed()
    screen.fill(BG_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        if event.type == TIME_COUNT_SEC and gaming == True:
                game_time_sec += 1
                if game_time_sec == 60 and gaming == True:
                    game_time_min += 1
                    game_time_sec = 0
                

        if S1.rect.colliderect(kbtu_outside_small_rect):
                """
            #текстовое поле при косании со зданием
            pygame.draw.rect(screen, BLACK, (675, 145, 250, 100))
            KBTU_text = game_time_fonts.render("this is \n KBTU univercity", True, (0, 0, 0))
            screen.blit(KBTU_text, (700, 170))
            screen.blit(arrow_up, arrow_up_rect)
            screen.blit(arrow_down, arrow_down_rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
                    if arrow_up_rect.collidepoint(mouse_pos):
                        flag_kbtu2 = 1
                    if arrow_down_rect.collidepoint(mouse_pos):
                        flag_kbtu2 = 0

            if flag_kbtu2 == 1:
                """
                if knowledge_bar.unit<100:
                    if knowledge_bar.unit+50>=100:
                        knowledge_bar.unit += 50
                        course_counter += 1
                        knowledge_bar.unit -= 100
                        if course_counter >= 5:
                            screen.fill("red")
                            screen.blit(win_font, (WIDTH//2- 100, HEIGHT//2 -100))
                            game_win_time = game_time_fonts.render(f"Overall Time: {game_time_min}:{game_time_sec}", True, (0, 0, 0))
                            screen.blit(game_win_time, (WIDTH//2- 100, HEIGHT//2))
                            pygame.display.flip()
                            time.sleep(3)
                            pygame.quit()
                            sys.exit()
                    else:
                        knowledge_bar.unit += 50
                    if sleep_bar.unit>=2:
                        sleep_bar.unit-=2
                    if satiety_bar.unit>=2:
                        satiety_bar.unit-=2
                    if happiness_bar.unit>=2:
                        happiness_bar.unit-=2 
                screen.blit(kbtu_inside, kbtu_inside_rect)
                kbtu_sound.play()
                pygame.display.flip()
                S1.rect.center = (625, HEIGHT//2)
                time.sleep(2)
                

        
        if S1.rect.colliderect(dormitory_outside_small_rect):
            if sleep_bar.unit + 40 <100:
                sleep_bar.unit += 40
            if knowledge_bar.unit>=10:
                knowledge_bar.unit-=10
            if satiety_bar.unit>=2:
                satiety_bar.unit-=2
            if happiness_bar.unit>=2:
                happiness_bar.unit-=2
            else:
                sleep_bar.unit = 100
            
            screen.blit(dormitory_inside, dormitory_inside_rect)
            dormitory_sound.play()
            pygame.display.flip()
            S1.rect.center = (1175, HEIGHT//2)
            time.sleep(2)

        if sleep_bar.unit <= 0 or satiety_bar.unit <= 0 or happiness_bar.unit <= 0:
            screen.fill("red")
            screen.blit(lose_font, (WIDTH//2- 100, HEIGHT//2 -100))
            pygame.display.flip()
            time.sleep(2)
            pygame.quit()
            sys.exit()
    
        #добавляю выбор кнопок мышкой (для info пока не добавлял)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                if unpbplay_small_rect.collidepoint(mouse_pos) and flag_buttons == 0:  
                    knopka.play()
                    time.sleep(1)
                    gaming = True
                    flag_buttons = 1

                elif unpbexit_small_rect.collidepoint(mouse_pos) and flag_buttons == 0:
                    knopka.play()
                    time.sleep(0.5)
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
        screen.blit(kbtu_outside_small, kbtu_outside_small_rect)
        screen.blit(dormitory_outside_small, dormitory_outside_small_rect)

        #screen.blit(S1.image, S1.rect)

        S1.move()
        S1.draw(screen)


        knowledge_bar.draw(screen)
        sleep_bar.draw(screen)
        satiety_bar.draw(screen)
        happiness_bar.draw(screen)
        screen.blit(knowledge, knowledge_position_rect)
        screen.blit(sleep, sleep_position_rect)
        screen.blit(satiety, satiety_position_rect)

        course_counter_text = font_small.render(f'Year: {course_counter}', True, (255, 255, 255))
        course_counter_text_rect = course_counter_text.get_rect()
        course_counter_text_rect.center = (120, 180)
        screen.blit(course_counter_text, course_counter_text_rect)

        # Game timer
        game_time_text = game_time_fonts.render(f"Time: {game_time_min}:{game_time_sec}", True, (255, 255, 255))
        screen.blit(game_time_text, game_time_rect)




    else:
        screen.blit(unpbplay_small,unpbplay_small_rect)
        screen.blit(unpbexit_small, unpbexit_small_rect)
        screen.blit(unpbinfo_small, unpbinfo_small_rect)   

    pygame.display.flip() 