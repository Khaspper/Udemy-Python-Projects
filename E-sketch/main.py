from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

degree = 10


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.setheading(tim.heading() + degree)


def turn_right():
    tim.setheading(tim.heading() - degree)


def clear_drawings():
    tim.clear()
    tim.penup()
    tim.setposition(0,0)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawings)
screen.exitonclick()
