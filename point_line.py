from tkinter import Tk, BOTH, Canvas

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:

    def __init__(self, point_1, point_2):
        self.__point_1 = point_1
        self.__point_2 = point_2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.__point_1.x, self.__point_1.y, 
            self.__point_2.x, self.__point_2.y, 
            fill = fill_color, width = 2)