from turtle import Turtle

FONT = ("Courier", 100, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(position)
        self.write(self.score, move=False, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, move=False, font=FONT)

    def game_over(self):
        #! Center this and add the dashed lines down the middle
        self.goto(-260, 0)
        self.write(f"GAME OVER", move=False, font=FONT)
