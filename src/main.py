from cell import Cell
from gui_stuff import Window, Point
from maze import Maze



def main():
    win = Window(800, 600)
    # point_1 = Point(100, 0)
    # point_2 = Point(100, 600)
    # point_3 = Point(200, 0)   
    # point_4 = Point(200, 600)
    # point_5 = Point(300, 0)   
    # point_6 = Point(300, 600)
    # win.draw_line(Line(point_1, point_2), "black")
    # win.draw_line(Line(point_3, point_4), "black")
    # win.draw_line(Line(point_5, point_6), "black")

    # cell_0 = Cell(win)
    # cell_1 = Cell(win)
    # cell_2 = Cell(win)
    # cell_3 = Cell(win)
    # cell_4 = Cell(win)
    # cell_5 = Cell(win)

    # cell_0.draw(100, 100, 150, 150)
    # cell_1.draw(200, 100, 250, 150)
    # cell_2.draw(300, 100, 350, 150)
    # cell_3.draw(400, 100, 450, 150)
    # cell_4.draw(500, 100, 550, 150)
    # cell_5.draw(600, 100, 650, 150)
    
    # cell_0.draw_move(cell_1, False)
    # cell_2.draw_move(cell_3, True)
    maze_0 = Maze(50, 50, 10, 14, 50, 50, win)
    maze_0.solve()


    win.wait_for_close()



main()