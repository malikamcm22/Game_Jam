import pygame,sys
from settings import *
from bar import Bar

pygame.init()

unpbplay = pygame.image.load("buttons/unpbplay.png")
unpbexit = pygame.image.load("buttons/unpbexit.png")
unpbinfo = pygame.image.load("buttons/unpbinfo.png")
pbplay = pygame.image.load("buttons/pbplay.png")
pbexit = pygame.image.load("buttons/pbexit.png")
pbinfo = pygame.image.load("buttons/pbinfo.png")

unpbplay_small = pygame.transform.scale(unpbplay,(350,150))
unpbexit_small = pygame.transform.scale(unpbexit,(350,150))
unpbinfo_small = pygame.transform.scale(unpbinfo,(350,150))
# стоит ли использовать transform scale или лучше вручную менять размер изображений?

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

# Характеристики персонажа
knowledge = 0   # знания
sleep = 100   # сон
satiety =  100    # сытость
happiness = 100   # счастье

radius = 30
x = 400
y = 300

x_margin_for_bars = 30

knowledge_bar = Bar(x_margin_for_bars,10,200,25,100,BROWN)
# knowledge_bar.unit = 0
sleep_bar = Bar(x_margin_for_bars,45,200,25,100,BLUE)
satiety_bar = Bar(x_margin_for_bars,80,200,25,100,RED)
happiness_bar = Bar(x_margin_for_bars,115,200,25,100,YELLOW)

gaming = False

while True:
    clock.tick(FPS)
    pressed = pygame.key.get_pressed() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
    screen.fill(BG_COLOR)


    if gaming:

        if pressed[pygame.K_UP] and y>radius and not (x<=CHARACTERISTICS_BAR_WIDTH+radius and y<=CHARACTERISTICS_BAR_HEIGHT+radius): y-=SPEED_OF_CHARACTER 
        if pressed[pygame.K_DOWN] and y<HEIGHT-radius: y+=SPEED_OF_CHARACTER
        if pressed[pygame.K_LEFT] and x>radius and not (x<=CHARACTERISTICS_BAR_WIDTH+radius and y<=CHARACTERISTICS_BAR_HEIGHT+radius): x-=SPEED_OF_CHARACTER
        if pressed[pygame.K_RIGHT] and x<WIDTH-radius: x+=SPEED_OF_CHARACTER

        pygame.draw.rect(screen, BLACK, (0,0, CHARACTERISTICS_BAR_WIDTH, CHARACTERISTICS_BAR_HEIGHT))

        pygame.draw.rect(screen, BLUE, (CHARACTERISTICS_BAR_WIDTH+200,50, 350, 200))
        pygame.draw.rect(screen, BLUE, (CHARACTERISTICS_BAR_WIDTH+750,50, 350, 200))
        pygame.draw.rect(screen, BLUE, (CHARACTERISTICS_BAR_WIDTH+200,400, 350, 200))
        pygame.draw.rect(screen, BLUE, (CHARACTERISTICS_BAR_WIDTH+750,400, 350, 200))
        
        
        pygame.draw.circle(screen,GREEN,(x,y),radius)

        knowledge_bar.draw(screen)
        sleep_bar.draw(screen)
        satiety_bar.draw(screen)
        happiness_bar.draw(screen)

    else:
        screen.blit(unpbplay_small,(600,150))
        screen.blit(unpbexit_small,(600,300))
        screen.blit(unpbinfo_small,(600,450))   

    

    pygame.display.flip() 
    