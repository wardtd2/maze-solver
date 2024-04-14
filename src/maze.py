import random
from cell import Cell
import time


class Maze:

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None,
        ):
        self.x1 = x1
        self.y1 = y1
        if num_rows <= 0:
            raise ValueError("Number of rows must be a positive integer")
        self.num_rows = num_rows
        if num_cols <= 0:
            raise ValueError("Number of columns must be a positive integer")
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = random.seed(seed) if seed is not None else seed
        self._cells = [[None for i in range(0, num_rows)] for i in range(0, num_cols)]
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    
    def _create_cells(self):
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._cells[i][j] = Cell(self.win)
        
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._draw_cell(i, j)
    

    def _draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []
            # Left
            if i - 1 >= 0 and self._cells[i-1][j].visited == False:
                possible_directions.append((i - 1, j))
            # Right
            if i + 1 < self.num_cols and self._cells[i + 1][j].visited == False:
                possible_directions.append((i + 1, j))
            # Up
            if j - 1 >= 0 and self._cells[i][j - 1].visited == False:
                possible_directions.append((i, j - 1))
            # Down
            if j + 1 < self.num_rows and self._cells[i][j + 1].visited == False:
                possible_directions.append((i, j + 1))
            
            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return
           
            # Pick a direction
            direction = random.randrange(0, len(possible_directions))
            next_cell_x = possible_directions[direction][0]
            next_cell_y = possible_directions[direction][1]

            # Break down the walls
            if next_cell_x == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[next_cell_x][next_cell_y].has_right_wall = False
                # print(f"Moving left from {i}:{j} to {next_cell_x}{next_cell_y}")
            if next_cell_x == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[next_cell_x][next_cell_y].has_left_wall = False
                # print(f"Moving right from {i}:{j} to {next_cell_x}{next_cell_y}")
            if next_cell_y == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[next_cell_x][next_cell_y].has_bottom_wall = False
                # print(f"Moving up from {i}:{j} to {next_cell_x}{next_cell_y}")
            elif next_cell_y ==  j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_cell_x][next_cell_y].has_top_wall = False
                # print(f"Moving down from {i}:{j} to {next_cell_x}{next_cell_y}")
            
            # Move to the next cell
            self._break_walls_r(next_cell_x, next_cell_y)
    

    def _reset_cells_visited(self):
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._cells[i][j].visited = False