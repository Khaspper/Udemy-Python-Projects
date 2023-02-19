from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

timmy = Turtle(shape="turtle")
tommy = Turtle(shape="turtle")
thommy = Turtle(shape="turtle")
connie = Turtle(shape="turtle")
ronnie = Turtle(shape="turtle")
ponnie = Turtle(shape="turtle")
ponnie.color("purple")

turtles_list = [timmy, tommy, thommy, connie, ronnie, ponnie]

y_coordinate = -180

i = 0
for turtles in turtles_list:
    turtles.color(colors[i])
    turtles.penup()
    turtles.setposition(x=-240, y=y_coordinate)
    y_coordinate += 72.5
    i += 1

if user_bet:
    is_race_on = True

while is_race_on:

    i = 0
    for turtles in turtles_list:
        random_distance = random.randint(0, 10)
        turtles.forward(random_distance)
        if turtles.xcor() >= 250:
            is_race_on = False
            print(f"{colors[i].title()} WON!")
            if user_bet.lower() == colors[i]:
                print("You WON! You placed the winning bet!")
        i += 1
screen.bye()
