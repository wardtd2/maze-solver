from gui_stuff import Line, Point



class Cell:
    
    def __init__(
            self, has_left_wall, has_right_wall,
                 has_top_wall, has_bottom_wall, x1, y1, x2, y2, window
                 ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._window = window


    def draw(self, x1, y1, x2, y2):
        if self.has_left_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x1,y2)))
        if self.has_right_wall:
            self._window.draw_line(Line(Point(x2, y1), Point(x2,y2)))
        if self.has_top_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x2,y1)))
        if self.has_bottom_wall:
            self._window.draw_line(Line(Point(x1, y2), Point(x2,y2)))

    
    def draw_move(self, to_cell, undo=False):
        start = Point(((self._x1 + self._x2) / 2), ((self._y1 + self._y2) / 2))
        end = Point(((to_cell._x1 + to_cell._x2) / 2), ((to_cell._y1 + to_cell._y2) / 2))
        if undo:
            self._window.draw_line(Line(start, end), "gray")
        else:
            self._window.draw_line(Line(start, end), "red")