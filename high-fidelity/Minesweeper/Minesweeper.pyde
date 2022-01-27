from Board import Board
from Cell import Cell
import time

add_library("sound")
restart = False

def setup():
    global board
    global file
    global restart
    size(500, 500)
    background(0)
    board = Board(width, height)
    file = SoundFile(this, "sound.mp3")
    file.loop()
    restart = False
    
def draw():
    global restart
    
    if not board.started:
        font = loadFont("Monospaced.bold-48.vlw")
        textFont(font, 16)
        textAlign(CENTER)
        fill(255)
        text("There we GO! Welcome to Mineswepper\nTo start the game press your LEFT keyboard key\n", width/2, 100)
        text("Once you press on a cell,\nIt reveals how many mined cells are around.\n", width/2, 150)
        text("Pressing on a mined cell will end your life.\nThere is just one life per game", width/2, 200)
        text("The Objective is to reveal all the empty cells.\nNon mined cells", width/2, 250)
            
    else:
        # Display board on the screen with a ll the cells
        board.show()    
    
    if board.is_over:
        font = loadFont("Monospaced.bold-48.vlw")
        textFont(font, 40)
        textAlign(CENTER)
        fill(255)
        text("GAME OVER", width/2, height/3 + 14)
        textFont(font, 20)
        text(" TO RESTART,\nPRESS RIGHT KEYBOARD KEY", width/2, height/3 + 50)
        
    if board.is_over and restart:
        setup()
            
    # For each mouse click (LEFT) on a cell, reveal a cell if it's not yet revealed
    if (mouseButton == RIGHT):
        if board.is_over and board.started and not restart:
            file.stop()
            restart = True
        
    if (mouseButton == LEFT):
        if not board.started:
            board.started = True
            
        if not board.is_over:
            for row in board.grid:
                for cel in row:
                    if cel.x == ((mouseX/20) * 20) and cel.y == ((mouseY/20) * 20):
                        cel.reveal()
