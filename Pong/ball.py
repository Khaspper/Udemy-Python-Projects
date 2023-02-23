from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(45)

    def move(self):
        self.forward(2.5)

    def hit_the_top(self):
        if -290 >= self.ycor() or self.ycor() >= 290:
            self.change_directions()

    def change_directions(self):
        self.setheading(self.heading() * -1)

    def paddle_bounce(self):
        self.setheading(180 - self.heading())

    def right_paddle_won(self):
        self.home()
        self.setheading(-135)

    def left_paddle_won(self):
        self.home()
        self.setheading(45)