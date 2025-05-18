from window import Window
from point_line import Point, Line
from cell import Cell
from maze import Maze
from global_variables import *

def main():
    # Create window
    win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
    
    # Creates and draws maze
    m1 = Maze(STARTING_X, STARTING_Y, ROWS, COLUMNS, CELL_WIDTH, CELL_HEIGHT, win)
    
    # Call solver method
    m1.solve()
    # Wait for window to be closed
    win.wait_for_close()





main()