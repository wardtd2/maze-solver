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


    def test_maze_large(self):
        num_cols = 20
        num_rows = 22
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )


    def test_maze_no_rows(self):
        num_cols = 12
        num_rows = 0
        with self.assertRaises(ValueError):
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)


    
    def test_maze_no_cols(self):
        num_cols = 0
        num_rows = 0
        with self.assertRaises(ValueError):
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)


    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(
            False,
            m1._cells[0][0].has_top_wall,
        )
        self.assertEqual(
            False,
            m1._cells[11][9].has_bottom_wall,
        )


    def test_maze_resets_visited(self):
        num_cols = 16
        num_rows = 18
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(0, num_cols):
            for j in range(0, num_rows):
                self.assertEqual(
                    False,
                    m1._cells[i][j].visited
                )


