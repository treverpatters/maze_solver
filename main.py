from window import Window
from point_line import Point, Line

def main():
    # Create window
    win = Window(800, 600)
    
    # Create points
    p1 = Point(50, 50)
    p2 = Point(200, 100)
    p3 = Point(50, 200)
    p4 = Point(200, 50)

    #Create lines using points
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)
    line3 = Line(p1, p3)

    # Draw lines with different colors
    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    win.draw_line(line3, "green")

    # Wait for window to be closed
    win.wait_for_close()





main()