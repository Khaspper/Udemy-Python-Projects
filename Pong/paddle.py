from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.setposition(coordinates)
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if self.ycor() < 240:
            self.setposition(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -240:
            self.setposition(self.xcor(), self.ycor() - 20)
