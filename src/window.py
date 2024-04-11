from tkinter import Tk, BOTH, Canvas



class Window:

    def __init__(self, height, width):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    

    def wait_for_close(self):
        self.running = True
        while self.__running is True:
            self.redraw()
    


    def close(self):
        self.__running = False