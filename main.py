from graphics import Window, Point, Line
from cell import Cell


def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_right_wall = False
    c.has_bottom_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_left_wall = False
    c.has_bottom_wall = False
    c.draw(100, 50, 150, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.has_bottom_wall = False
    c.draw(50, 100, 100, 150)

    c = Cell(win)
    c.has_top_wall = False
    c.has_left_wall = False
    c.draw(100, 100, 150, 150)

    win.wait_for_close()


main()
