import turtle
import random

#* Because I have RGB as tuples AND I want to make my "turtle" change colors using the given RBG values
#* I use this to change to the turtle module to take in RGB valyes and change them into colors
turtle.colormode(255)

#* Construct a "turtle" object called timmy
timmy = turtle.Turtle()

#* Hides the cursor AKA "timmy" AKA the "turtle"
timmy.ht()

#* Increases the speed of the "turtle" AKA "timmy"
timmy.speed("fastest")

#* Makes sure when "timmy" moves he/him doesn't draw on the screen
timmy.penup()

#* Sets the y coordinate to -280
y_coordinate = -280

#* A list of RBG values
color_list = [
(206, 159, 112),    (138, 173, 192),    (223, 206, 119),    (43 , 106, 138),     (139, 183, 149),    (15 , 52 , 75 ),
(218, 88 , 65 ),    (36 , 126, 105),    (124, 81 , 95 ),    (193, 133, 145),     (71 , 164, 120),    (145, 81 , 71 ),
(12 , 58 , 49 ),    (55 , 153, 180),    (51 , 34 , 43 ),    (126, 37 , 50 ),     (205, 85 , 102),    (175, 206, 171),
(6  , 109, 87 ),    (229, 168, 182),    (147, 204, 230),    (157, 153, 67 ),     (33 , 64 , 101),    (16 , 84 , 100),
(47 , 30 , 27 ),    (184, 189, 203)
]

#* 2 for loops to make timmy move
for j in range(10):
    #* I put the x value inside the for loop so timmy can go back to the starting area
    x_coordinate = -320

    #* I subtract 50 from y_coordinate because I want timmy to start at the beginning but move up by 50 paces
    #* 50 paces because that's the distance between each dot
    y_coordinate += 50

    for i in range(10):
        #* Get random color
        timmy.goto(x_coordinate, y_coordinate)

        #* Draw dot
        timmy.dot(20, random.choice(color_list))

        #* Move right by 50 paces because that's what the space is between each dot
        x_coordinate += 50

#* making an object named screen
screen = turtle.Screen()

#* When I click the screen / window closes
screen.exitonclick()
