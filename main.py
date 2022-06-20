import pygame
from settings import *
from classes import *

pygame.init()

FIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Campo Minato")

def printa_display(fin):
	fin.fill(WHITE)	
	pygame.display.update()






def main():
	fun = True

	while fun:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fun = False
				break


		printa_display(FIN)

	pygame.quit()

if __name__ == "__main__":
	main()


'''
COSA VA AGGIUNTO ****
-importare tutte le robe
-collegare le classi con il di sopra
-aggiungere la tutte le grafichine
-patchare tutto(?)
-scoprire un po' di TDD da aggiungere al nostro giuoco, prima di mandarlo alla francesca (pensa che roba)
'''