from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    #* The constructor to build the object
    def __init__(self):
        self.snake_bodies = []
        self.create_snake()
        self.head = self.snake_bodies[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)

    def move(self):
        #* You first want to set the tails to the new position
        for i in range(len(self.snake_bodies) - 1, 0, -1):
            self.snake_bodies[i].goto(self.snake_bodies[i - 1].pos())
        #* Then move your snake head because you are moving the tail to the correct position then you move the head
        #* position place ahead
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        #* adds a new segment to the snake
        self.add_body(self.snake_bodies[-1].position())

    def add_body(self, position):
        body_part = Turtle("square")
        body_part.penup()
        body_part.color("white")
        body_part.setposition(position)
        self.snake_bodies.append(body_part)

    def reset(self):
        for body in self.snake_bodies:
            body.goto(1000, 1000)
        self.snake_bodies.clear()
        self.create_snake()
        self.head = self.snake_bodies[0]