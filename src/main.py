from cell import Cell
from gui_stuff import Window, Point



def main():
    win = Window(800, 600)
    point_1 = Point(100, 0)
    point_2 = Point(100, 600)
    point_3 = Point(200, 0)   
    point_4 = Point(200, 600)
    point_5 = Point(300, 0)   
    point_6 = Point(300, 600)
    # win.draw_line(Line(point_1, point_2), "black")
    # win.draw_line(Line(point_3, point_4), "black")
    # win.draw_line(Line(point_5, point_6), "black")

    cell_0 = Cell(True, True, True, True, 100, 100, 150, 150, win)
    cell_1 = Cell(True, False, True, True, 200, 100, 250, 150, win)
    cell_2 = Cell(True, True, False, True, 300, 100, 350, 150, win)
    cell_3 = Cell(True, True, True, False, 400, 100, 450, 150, win)
    cell_4 = Cell(False, True, False, True, 500, 100, 550, 150, win)
    cell_5 = Cell(True, True, True, True, 600, 100, 650, 150, win)

    cell_0.draw(100, 100, 150, 150)
    cell_1.draw(200, 100, 250, 150)
    cell_2.draw(300, 100, 350, 150)
    cell_3.draw(400, 100, 450, 150)
    cell_4.draw(500, 100, 550, 150)
    cell_5.draw(600, 100, 650, 150)
    
    cell_0.draw_move(cell_1, False)
    cell_2.draw_move(cell_3, True)

    win.wait_for_close()



main()