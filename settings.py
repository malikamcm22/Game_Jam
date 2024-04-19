import pygame
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BROWN = (150,75,0)
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 30)
font_very_small = pygame.font.SysFont("Verdana", 20)
win_font = font.render("You Win!", True, BLACK)
lose_font = font.render("You Failed!", True, BLACK)


BG_COLOR = WHITE

FPS = 120

WIDTH, HEIGHT = 1500, 700

CHARACTERISTICS_BAR_WIDTH = 250
CHARACTERISTICS_BAR_HEIGHT = 300

SPEED_OF_CHARACTER = 5

def get_font(size):
    return pygame.font.SysFont("comicsans",size)