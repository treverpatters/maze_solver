from cell import Cell
from point_line import Point
class Maze:

    def __init__(self, 
                 x1, y1, 
                 num_rows, num_cols, 
                 cell_size_x, cell_size_y, 
                 win,
            ):
        self._x1, self._y1 = x1, y1
        self._num_rows, self._num_cols = num_rows, num_cols
        self._cell_size_x, self._cell_size_y = cell_size_x, cell_size_y
        self._win = win
        
        self._cells = []
        # Implement _create_cells then delete note
        # self._create_cells(self) 

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                
                point1 = Point(self._x1 + (i * self._cell_size_x), 
                               self._y1 + (j * self._cell_size_y))
                point2 = Point(self._x1 + ((i + 1) * self._cell_size_x), 
                               self._y1 + ((j + 1) * self._cell_size_y))
                
                current_cell = Cell(point1, point2)
                
                col.append(current_cell)
                
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        pass

    def _animate(self):
        pass
        