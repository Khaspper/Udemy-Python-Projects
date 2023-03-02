from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.movement = STARTING_MOVE_DISTANCE
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.setposition(random.randint(-250, 280), random.randint(-250, 260))

    def go_vroom(self):
        self.forward(self.movement)

    def update_speed(self):
        self.movement += MOVE_INCREMENT

    #* When the car reaches the left border of the window set it back to the right side of the screen and put it at
    #* a different y coordinate to add randomness
    def reset_y_pos(self):
        self.setposition(300, random.randint(-250, 260))
