from tkinter import Tk, BOTH, Canvas
from point_line import Point, Line
from global_variables import *

class Cell:
    
    def __init__(self, point1, point2, win=None):
        self._x1 = point1.x
        self._y1 = point1.y
        self._x2 = point2.x
        self._y2 = point2.y

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._win = win
        
        self.visited = False
    
    def draw(self):
        if self._win is None:
            return
        
        if self.has_left_wall:
            self.create_wall(self._x1, self._y1, self._x1, self._y2, CELL_COLOR)
        else:
            self.create_wall(self._x1, self._y1, self._x1, self._y2, BACKGROUND_COLOR)
        
        if self.has_right_wall:
            self.create_wall(self._x2, self._y1, self._x2, self._y2, CELL_COLOR)
        else:
            self.create_wall(self._x2, self._y1, self._x2, self._y2, BACKGROUND_COLOR)
            
        if self.has_top_wall:
            self.create_wall(self._x1, self._y1, self._x2, self._y1, CELL_COLOR)
        else:
            self.create_wall(self._x1, self._y1, self._x2, self._y1, BACKGROUND_COLOR)

        if self.has_bottom_wall:
            self.create_wall(self._x1, self._y2, self._x2, self._y2, CELL_COLOR)
        else:
            self.create_wall(self._x1, self._y2, self._x2, self._y2, BACKGROUND_COLOR)
    
    def create_wall(self, x1, y1, x2, y2, color):
        if self._win is not None:
            line = Line(Point(x1, y1), Point(x2, y2))
            return self._win.draw_line(line, f"{color}")
        return None
    
    def draw_move(self, to_cell, undo=False):
        # Should draw line from center of one cell to the other
        
        self_center = Point((self._x1 + self._x2)/2,(self._y1 + self._y2)/2)
        to_cell_center = Point((to_cell._x1 + to_cell._x2)/2,(to_cell._y1 + to_cell._y2)/2)
        middle_line = Line(self_center, to_cell_center)
        
        # Now Draw, Red if undo flag not set, gray otherwise
        if undo:
            self._win.draw_line(middle_line, WRONG_LINE_COLOR)
        else:
            self._win.draw_line(middle_line, CORRECT_LINE_COLOR)
        