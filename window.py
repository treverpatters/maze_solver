from tkinter import Tk, BOTH, Canvas
from point_line import Point, Line
from global_variables import *

class Window:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.__root = Tk()
        self.__root.title(WINDOW_TITLE)
    
        self._canvas = Canvas(self.__root, width = self.__width, height = self.__height, bg=BACKGROUND_COLOR)
        self._canvas.pack()

        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self._canvas, fill_color)

