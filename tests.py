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

    def test_maze_cell_initialization(self):
        # Test that cells are properly initialized
        num_cols = 3
        num_rows = 4
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    
        # Check if all cells have walls initially
        for i in range(num_cols):
            for j in range(num_rows):
                cell = m1._cells[i][j]
                self.assertTrue(cell.has_left_wall)
                self.assertTrue(cell.has_right_wall)
                self.assertTrue(cell.has_top_wall)
                self.assertTrue(cell.has_bottom_wall)

if __name__ == "__main__":
    unittest.main()