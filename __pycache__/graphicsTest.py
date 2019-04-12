from graphics import *
import time

def main():
        win = GraphWin("My Window", 500, 500)
        win.setBackground(color_rgb(20,20,20))

        txt = Text(Point(250,250), "What's up?")
        txt.setTextColor(color_rgb(200,100,20))
        txt.setSize(70)
        txt.draw(win)

        img = Image(Point(250,250),"QGo5isT.gif")
        img.draw(win)

        rect = Rectangle(Point(325,200),Point(425,300))
        rect.setOutline('green')
        rect.setWidth(10)
        rect.setFill(color_rgb(10,50,10))
        rect.draw(win)

        win.getMouse()

        win.close()

main()
