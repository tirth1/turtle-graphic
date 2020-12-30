from turtle import Turtle, Screen
import random
from colors import colors
# turtle.onkeypress(fun, key="Up")


def fwd(t):
    t.penup()
    color = random.choice(colors)
    t.dot(10, color)
    t.fd(4)


if __name__ == '__main__':
    turtle = Turtle(shape="turtle")
    turtle.penup()
    screen = Screen()
    screen.reset()
    screen.screensize(100, 100)
    screen.setworldcoordinates(0, 0, 100, 100)

    turtle.setpos(0, 0)
    x, y = turtle.position()
    print(x, y)
    turtle.penup()
    while y < 100:
        screen.onkeypress(fwd(turtle), key="Up")
        x, y = turtle.position()
        if x == 100:
            turtle.setpos(0, y+4)

    screen.exitonclick()







