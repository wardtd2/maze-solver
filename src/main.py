from gui_stuff import Window, Point, Line



def main():
    win = Window(800, 600)
    point_1 = Point(100, 0)
    point_2 = Point(100, 600)
    point_3 = Point(200, 0)   
    point_4 = Point(200, 600)
    point_5 = Point(300, 0)   
    point_6 = Point(300, 600)
    win.draw_line(Line(point_1, point_2), "black")
    win.draw_line(Line(point_3, point_4), "black")
    win.draw_line(Line(point_5, point_6), "black")

    win.wait_for_close()



main()