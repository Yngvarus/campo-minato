import random
import pygame
from settings import *

class Grid():
	'''
	Classe base della gliglia di gioco, serve come contenitore delle variabili
	che derivano dal file settings.py
	il succo del discorso si discorre nelle sotto classi SubGrid per la griglia
	sottostante dove avvengono i magheggi e SuperGrid per la griglia superiore 
	dove invece il player si vede apparire cose
	'''
	def __init__(self):
		self.height = HEIGHT - 100
		self.width = WIDTH
		self.rows = ROWS
		self.cols = COLS 
		self.cell_altez = int(WIDTH // COLS)
		self.cell_largh = int((HEIGHT - 100) // ROWS)
		



class SubGrid(Grid):
	'''
	Sotto classe di griglia definita altrove come soluzione_grid nella quale avviene la generazione e il 
	dislocamento di bombe nell'area di gioco, si inizia il numero totale di mine per la partita e il numero
	iniziale (di 0) di mine, insieme al campo di gioco come lista vuota in attesa della generazione. 
	'''
	def __init__(self):
		Grid.__init__(self)
		self.mine = TOT_MINE
		self.campo = self.prepara_null_campo()
		self.nr_mine = 0

		###### testing funzioni ######

	def printa_campo(self):
		#self.prepara_null_campo()
		#print(self.campo)
		for row in self.campo:
			print(row)
		#print(type(self.campo))


		###### ###### ###### ######

	def prepara_null_campo(self):
		temp_grid = []
		for row in range(0, self.rows):
			temp_row = []
			for col in range(0, self.cols):
				temp_row.append(VUOTA)
			temp_grid.append(temp_row)
		return temp_grid	
		

	def prepara_game(self):
		posizione_mine = set()
		self.prepara_null_campo()

		while self.nr_mine <= self.mine:
			x = random.randrange(0, len(self.campo))
			y = random.randrange(0, len(self.campo[0]))
			pos = x, y

			if pos in posizione_mine:
				continue

			posizione_mine.add(pos)
			self.campo[x][y] = MINA
			self.nr_mine += 1

	def count_cell(self, riga, coln):
		intorno_cella = ((-1,-1),(-1,0),(-1,1),(0,-1),(1,-1),(1,0),(1,1),(0,1))
		mine_intorno = 0
		for intorno in intorno_cella:
			cella_iriga = riga + intorno[0]
			cella_icoln = coln + intorno[1]
			#print(f"{intorno} intorno, {cella_iriga} riga, {cella_icoln} coln")	

			#controlla per il bordo
			if((cella_iriga>=0 and cella_iriga<=8) and (cella_icoln>=0 and cella_icoln<=8)):
				#print(f"{intorno} intorno, {cella_iriga} riga, {cella_icoln} coln")
				if self.campo[cella_iriga][cella_icoln] == MINA:
					mine_intorno += 1
					#print(f"{intorno} intorno, {mine_intorno} mine trovate")
		return mine_intorno




class SuperGrid(Grid):
	def __init__(self):
		Grid.__init__(self)
		self.campo = self.prepara_playa_campo()

		###### testing funzioni ######

	def printa_campo(self):
		#self.prepara_null_campo()
		#print(self.campo)
		#for row in self.campo:
		#	print(row)

		simboli = {-3: "§", -1: "@"}
		for row in range(len(self.campo)):
			for col in range(len(self.campo[row])):
				cella = self.campo[row][col]
				if cella in simboli:
					simbolo = simboli[cella]
				else:
					simbolo = str(cella)
				print(f"{simbolo} ", end='') 
			print("")

		#print(type(self.campo))


		###### ###### ###### ######

	def prepara_playa_campo(self):
		temp_grid = []
		for row in range(0, self.rows):
			temp_row = []
			for col in range(0, self.cols):
				temp_row.append(COPERTA)
			temp_grid.append(temp_row)
		return temp_grid	

	def set_flag(self, row, col):
		if self.campo[row][col] == COPERTA:
			self.campo[row][col] = FLAG

		elif self.campo[row][col] == FLAG:
			self.campo[row][col] = COPERTA

	def click(self, solution_grid, riga, colon):
	#check se è una bomba
		if solution_grid.campo[riga][colon] == MINA:
			print("BOOM!")
		elif self.campo[riga][colon] == COPERTA:
			self.campo[riga][colon] = solution_grid.count_cell(riga, colon)

			#cerca intorno e restituisce i valori
			celle = [(riga, colon)]
			offsets = ((-1,-1),(-1,0),(-1,1),(0,-1),(1,-1),(1,0),(1,1),(0,1))

			while len(celle) > 0:
				cella = celle.pop()
				for offset in offsets:
					riga = offset[0] + cella[0]
					colon = offset[1] + cella[1]
					if((riga>=0 and riga<len(self.campo)) and (colon>=0 and colon<len(self.campo[riga]))):
						if ((self.campo[riga][colon] == COPERTA) and (solution_grid.campo[riga][colon] == VUOTA) and (solution_grid.count_cell(riga, colon) >= 0)):
							self.campo[riga][colon] = solution_grid.count_cell(riga,colon)

							if solution_grid.count_cell(riga, colon) == VUOTA and (riga, colon) not in celle:
								celle.append((riga, colon))
							else:
								self.campo[riga][colon] = solution_grid.count_cell(riga, colon)


def main():
	
	soluzione.printa_campo()
	print("\n")

	print("\n")
	x = int(input(">x: "))
	y = int(input(">y: "))
	print(f"Click a ({x},{y})")
	giocatore.click(soluzione, x, y)
	giocatore.printa_campo()

soluzione = SubGrid()
soluzione.prepara_game()
	
giocatore = SuperGrid()
giocatore.prepara_playa_campo()

giocatore.printa_campo()
while __name__ == "__main__":
	main()






'''
COSA VA AGGIUNTO ****
-testing della funzione SubGrid.count_cell()
-testing della funzione SuperGrid.clicl()
-class bottoni cover_sopra 
-class bottoni cover_sotto 
'''
