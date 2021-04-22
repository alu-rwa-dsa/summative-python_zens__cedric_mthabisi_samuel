import random
import time

class Cell():
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.board = board
        self.colour = '#558B2F'
        self.status = random.randint(0, 3)
        if self.status == 2 or self.status == 3:
            self.status = 0
        self.revealed = False
        self.mines = 0
        
    def __str__(self):
        return '{}, {}'.format(self.x, self.y)
        
    def show(self):
        fill(self.colour)
        rect(self.x, self.y, 20, 20)
        
        if self.status != 1 and self.mines != 0:
            font = loadFont("Monospaced.bold-48.vlw")
            textFont(font, 10)
            fill(0)
            text(str(self.mines), self.x + 10, self.y + 14)
        
    def reveal(self):
        if(self.status == 1):
            self.colour = '#212121'
            self.board.end_game()
            
        elif(self.status == 0):
            if(self.revealed):
                return
            else:
                self.colour = '#AED581'
                self.revealed = True
                neighbours = self.find_neighbours()
                for coord in neighbours:
                    cell = self.board.get_cell(coord[0], coord[1])
                    if cell.status == 1:
                        self.mines += 1
                    else: continue
                
                if self.mines > 0:
                    return
                
                elif self.mines == 0:
                    for coord in neighbours:
                        cell = self.board.get_cell(coord[0], coord[1])
                        cell.reveal()
                    
    def show_mine(self):
        self.colour = '#212121'
           
    def find_neighbours(self):
        
        neighbors = []
        x_max = self.x + 20 if self.x + 20 < self.board.h else self.x
        x_min = self.x - 20 if self.x - 20 >= 0 else self.x
        y_max = self.y + 20 if self.y + 20 < self.board.h else self.y
        y_min = self.y - 20 if self.y - 20 >= 0 else self.y

        for i in range(x_min, x_max + 1, 20):
            for j in range(y_min, y_max + 1, 20):
                if i != self.x or j != self.y:  # DeMorgan's 1st Law: negating conjuctions
                    neighbors.append([i, j])

        return neighbors
