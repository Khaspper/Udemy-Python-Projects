from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        with open("highscore.txt") as data:
            self.high_score = int(data.read())
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(0, 270)
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("highscore.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increment_score(self):
        self.score += 1
        self.update_score()
