from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#* Setting up the screen my game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()

    #* Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    #* Detect collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 300:
        game_is_on = False
        scoreboard.game_over()

    for body in snake.snake_bodies[1:]:
        if snake.head.distance(body) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
