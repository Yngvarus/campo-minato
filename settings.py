import pygame
pygame.font.init()


#Colori
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
DBLUE = (0,0,139)
SLATE = (106,90,205)
DRED = (139,0,0)
RED = (255,0,0)
ORANGE = (255,165,0)
GOLD = (255,215,0)
KHAKI = (240,230,140)
GREEN = (173,255,47)
BROWN = (85, 65, 18)
TGREEN = (60,179,113)
OLIVE = (107,142,35)

#SETTINGS GENERALI
HEIGHT = 400
WIDTH = 300
FPS = 60
NUM_FONT = pygame.font.SysFont('comicsans', 20)
NUM_COLORS = {1 : GREEN,2 : KHAKI,3 : GOLD,4 : ORANGE,5 : RED,6 : DRED,7 : SLATE,8 : DBLUE}

#SETTING DEL GAMEPLAY
ROWS = 9
COLS = 9
TOT_MINE = 10
SIZE = WIDTH // ROWS

#NUMERI CHIAVE
VUOTA = 0
COPERTA = -1
MINA = -2
FLAG = -3
