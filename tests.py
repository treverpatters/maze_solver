import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    def test_maze_large_dimensions(self):
        num_cols = 25
        num_rows = 30
        m1 = Maze(0, 0, num_rows, num_cols, 5, 5)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_single_cell(self):
        # Edge case - a 1x1 maze
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 6
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        entrance = m1._cells[0][0]
        exit = m1._cells[num_cols - 1][num_rows - 1]
        self.assertFalse(entrance.has_top_wall)
        self.assertFalse(exit.has_bottom_wall)

    def test_reset_visited(self):
        num_cols = 10
        num_rows = 6
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._reset_cells_visited()
        
        for i in range(num_cols):
            for j in range(num_rows):
                cell = m1._cells[i][j]
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()