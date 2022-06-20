import pygame
from settings import *

class Bottone():
    def __init__(self, x, y, largh, altez, testo, colore, colore_testo, surf):
        self.rect = pygame.Rect(surf, colore, (x, y, largh, altez))
        self.out_rect = pygame.Rect(surf, colore, (x, y, largh, altez), 2)
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render(testo, True, colore_testo)
        self.posX = self.rect.centerx - (largh // 2) 
        self.posY = self.rect.centery - (altez // 2)
        self.out_posX = self.out_rect.centerx - (largh // 2) 
        self.out_posY = self.out_rect.centery - (altez // 2)
        self.clicked = False

    def stampa_btn(self, surf):
        surf.blitz(self.text, (self.posX, self.posY))
        surf.blitz(self.out_posX, self.out_posY)

    def click_btn(self):
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked == True:
                    print("click")
                    self.clicked = False


class Cella(Bottone):
    
    def __init__(self, x, y, largh, altez, testo, colore, colore_testo, surf):
        Bottone.__init__(self)


    def click_cella(self):
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked == True:
                    print("click")
                    self.clicked = False 


    def stampa_cella(self, surf):
        surf.blitz(self.text, (self.posX, self.posY))
        surf.blitz((self.out_posX, self.out_posY))
