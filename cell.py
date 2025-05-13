from tkinter import Tk, BOTH, Canvas
from point_line import Point, Line

class Cell:
    
    def __init__(self, point1, point2, win):
        self._x1 = point1.x
        self._y1 = point1.y
        self._x2 = point2.x
        self._y2 = point2.y

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._win = win
    
    def draw(self):
        if self.has_left_wall:
            self.create_wall(self._x1, self._y1, self._x1, self._y2)
        
        if self.has_right_wall:
            self.create_wall(self._x2, self._y1, self._x2, self._y2)
            
        if self.has_top_wall:
            self.create_wall(self._x1, self._y1, self._x2, self._y1)

        if self.has_bottom_wall:
            self.create_wall(self._x1, self._y2, self._x2, self._y2)
    
    def create_wall(self, x1, y1, x2, y2):
        point1 = Point(x1, y1)
        point2 = Point(x2, y2)
        line = Line(point1, point2)
        return self._win.draw_line(line, "black")
    
    def draw_move(self, to_cell, undo=False):
        # Should draw line from center of one cell to the other
        
        self_center = Point((self.x1 + self.x2)/2,(self.y1 + self.y2)/2)
        to_cell_center = Point((to_cell.x1 + to_cell.x2)/2,(to_cell.y1 + to_cell.y2)/2)
        
        # Now Draw, Red if undo flag not set, gray otherwise
        