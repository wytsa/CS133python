# make graph paper
from turtle import *

def main():
    win = GraphWin("graph paper", 500, 500)
    
    # set first lines
    win.setCoords(0.0, 0.0, 3.0, 3.0)
    
    # vert lines
    Line(Point(1,0), Point(1,3)).draw(win)
    Line(Point(2,0), Point(2,3)).draw(win)
    
    # horizontal lines
    Line(Point(0,1), Point(3,1)).draw(win)
    Line(Point(0,2), Point(3,2)).draw(win)

main()
