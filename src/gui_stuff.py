from tkinter import Tk, BOTH, Canvas



class Window:

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root,  bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    
    def wait_for_close(self):
        self.__running = True
        while self.__running is True:
            self.redraw()
    

    def close(self):
        self.__running = False

    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)



class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y



class Line:

    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2)
        canvas.pack(fill=BOTH, expand=1)



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