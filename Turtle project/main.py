import turtle
from turtle import Turtle, Screen
import random
from typing import Tuple

tim = Turtle()

turtle.colormode(255)
tim.width(1)
tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()

"""import turtle
from turtle import Turtle, Screen
import random
from typing import Tuple

tim = Turtle()

turtle.colormode(255)
tim.width(15)
tim.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

directions = [90, 180, 270, 0]
tim.width(15)

for i in range(200):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(random.choice(directions))




screen = Screen()
screen.exitonclick()
"""
