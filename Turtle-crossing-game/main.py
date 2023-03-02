import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#* Initializing objects
scoreboard = Scoreboard()
turtle = Player()

#* Array of cars
cars = []
for i in range(23):
    car = CarManager()
    cars.append(car)

#* User inputs
screen.onkey(turtle.move_up, "Up")
screen.onkey(turtle.move_down, "Down")
screen.onkey(turtle.move_left, "Left")
screen.onkey(turtle.move_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for i in range(23):
        cars[i].go_vroom()
        if cars[i].xcor() <= -290:
            cars[i].reset_y_pos()
        if turtle.distance(cars[i]) < 23:
            game_is_on = False
            scoreboard.game_over()

    if turtle.reached_end():
        time.sleep(1)
        scoreboard.update_score()
        turtle.reset_position()
        for i in range(23):
            cars[i].update_speed()

screen.exitonclick()
