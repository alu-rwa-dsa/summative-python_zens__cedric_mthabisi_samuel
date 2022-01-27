from Cell import Cell
import time

class Board():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.grid = [[Cell(x, y, self) for x in range(0, w, 20)] for y in range(0, h, 20)]
        self.is_over = False
        self.started = False
        
    def __str__(self):
        return "|".join([str(cel) for row in self.grid for cel in row])
    
    def get_cell(self, x, y):
        if x in range(self.w) and y in range(self.h):
            return self.grid[y/20][x/20]
        
    def end_game(self):
        for row in self.grid:
            for cell in row:
                if cell.status == 1:
                    cell.show_mine()
        self.is_over = True
                    
    def show(self):
        for row in self.grid:
            for cel in row:
                cel.show()
    
