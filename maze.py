from cell import Cell
from point_line import Point
import time
import random
from global_variables import *

class Maze:

    def __init__(self, 
                 x1, y1, 
                 num_rows, num_cols, 
                 cell_size_x, cell_size_y, 
                 win=None,
                 seed=None,
            ):
        self._x1, self._y1 = x1, y1
        self._num_rows, self._num_cols = num_rows, num_cols
        self._cell_size_x, self._cell_size_y = cell_size_x, cell_size_y
        self._win = win

        if seed is not None:
            random.seed(seed)
        
        self._cells = []
        # Create cells and draw to window if available
        self._create_cells()
        self._break_entrance_and_exit()

        self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                
                point1 = Point(self._x1 + (i * self._cell_size_x), 
                               self._y1 + (j * self._cell_size_y))
                point2 = Point(self._x1 + ((i + 1) * self._cell_size_x), 
                               self._y1 + ((j + 1) * self._cell_size_y))
                
                current_cell = Cell(point1, point2, self._win)
                
                col.append(current_cell)
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
                
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        current_cell = self._cells[i][j]

        current_cell.draw()
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(ANIMATE_SPEED)
    
    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        exit = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit.has_bottom_wall = False
        entrance.draw()
        exit.draw()

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            need_to_visit = []
            # Check up
            if j > 0:
                # if that cell visited = False, add to need_to_visit
                up_cell = self._cells[i][j - 1]
                if not up_cell.visited:
                    need_to_visit.append((i, (j - 1)))
            # Check down
            if j < self._num_rows - 1:    
                # if that cell visited = False, add to need_to_visit
                down_cell = self._cells[i][j + 1]
                if not down_cell.visited:
                    need_to_visit.append((i, (j + 1)))
            # Check left
            if i > 0:    
                # if that cell visited = False, add to need_to_visit
                left_cell = self._cells[i - 1][j]
                if not left_cell.visited:
                    need_to_visit.append(((i - 1), j))
            # Check right
            if i < self._num_cols - 1:
                # if that cell visited = False, add to need_to_visit
                right_cell = self._cells[i + 1][j]
                if not right_cell.visited:
                    need_to_visit.append(((i + 1), j))
            
            # if len(need_to_visit) == 0:
            if len(need_to_visit) == 0:
                return
            # Otherwise, pick random direction
            next_coordinates = random.choice(need_to_visit)
            next_cell = self._cells[next_coordinates[0]][next_coordinates[1]]
            # Knock down walls between current cell and chosen cell
            # up
            if j > next_coordinates[1]:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
                current_cell.draw()
                next_cell.draw()
                self._break_walls_r(next_coordinates[0], next_coordinates[1])
                continue
            # down
            elif j < next_coordinates[1]:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
                current_cell.draw()
                next_cell.draw()
                self._break_walls_r(next_coordinates[0], next_coordinates[1])
                continue
            # left
            elif i > next_coordinates[0]:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
                current_cell.draw()
                next_cell.draw()
                self._break_walls_r(next_coordinates[0], next_coordinates[1])
                continue
            # right
            elif i < next_coordinates[0]:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
                current_cell.draw()
                next_cell.draw()
                self._break_walls_r(next_coordinates[0], next_coordinates[1])
                continue
    
    def __reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        self.__reset_cells_visited()
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        else:
            deltas = [ 
                ((0, -1), "has_top_wall"),    # up
                ((1, 0), "has_right_wall"),   # right
                ((0, 1), "has_bottom_wall"),  # down
                ((-1, 0), "has_left_wall")    # left
            ]
            
            for (di, dj), wall_attr in deltas:
                ni = i + di
                nj = j + dj  # Now (ni, nj) is potential neighbor in direction

                # Check if neighbor is in bounds
                if 0 <= ni <= self._num_cols - 1 and 0 <= nj <= self._num_rows - 1:
                    neighbor_cell = self._cells[ni][nj]
                    has_wall = getattr(current_cell, wall_attr)

                    # Check if there's no wall and cell hasn't been visited
                    if not has_wall and not neighbor_cell.visited:
                        current_cell.draw_move(neighbor_cell)
                        test = self._solve_r(ni, nj)
                        if test:
                            return True
                        else:
                            current_cell.draw_move(neighbor_cell, undo=True)
            return False
