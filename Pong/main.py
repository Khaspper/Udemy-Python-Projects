from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()

r_score = Scoreboard((100, 200))
l_score = Scoreboard((-100, 200))

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.001)
    ball.move()
    ball.hit_the_top()

    if ball.xcor() >= 330 or ball.xcor() <= -330:
        if ball.distance(right_paddle) < 60 or ball.distance(left_paddle) < 60:
            ball.paddle_bounce()
        else:
            if ball.xcor() >= 380:
                l_score.update_score()
                time.sleep(.5)
                ball.left_paddle_won()
            elif ball.xcor() <= -380:
                r_score.update_score()
                time.sleep(.5)
                ball.right_paddle_won()

    if r_score.score == 7 or l_score.score == 7:
        r_score.game_over()
        game_is_on = False
















screen.exitonclick()