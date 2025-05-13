from window import Window
from point_line import Point, Line
from cell import Cell

def main():
    # Create window
    win = Window(800, 600)
    
    # Create points
    p1 = Point(50, 50)
    p2 = Point(200, 100)
    p3 = Point(50, 200)
    p4 = Point(500, 500)

    # Create Cells
    cell1 = Cell(p1, p2, win)
    cell2 = Cell(p2, p3, win)
    cell3 = Cell(p3, p4, win)

    # Testing with all walls False
    cell1.has_top_wall = False
    cell1.has_bottom_wall = False
    cell1.has_right_wall = False
    cell1.has_left_wall = False
    # Call on Cell.draw()
    cell1.draw()
    cell2.draw()
    cell3.draw()
    # Wait for window to be closed
    win.wait_for_close()





main()