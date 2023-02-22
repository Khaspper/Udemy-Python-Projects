from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(0, 270)
        self.color("white")
        self.score = 0
        self.write(f"Scoreboard : {self.score}", False, align="center", font=('Arial', 20, 'normal'))


    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Scoreboard : {self.score}", False, align="center", font=('Arial', 20, 'normal'))