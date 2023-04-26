# * i want my game to show one jojo stand at a time it changes the "shape" of the screen to the photo of the stand
# * if they type next it changes the photo to the next one but doesnt mean it's wrong if they type in "give up" then
# * it prints out the name of the stand and they get it wrong, but when they type in exit then it exits the game
# * I could put the name of the stand + the file name and put that in an array like the letter thing and remove it if
# * they get it wrong or correct

import turtle
import pandas

screen = turtle.Screen()
image = "jojo_stands_golden_wind.gif"
screen.addshape(image)
turtle.shape(image)
writing_names = turtle.Turtle()
writing_names.speed("fast")
writing_names.penup()
writing_names.hideturtle()

answer = screen.textinput(title="Guess The Stand", prompt="Name a Stand...").title()

data = pandas.read_csv("JoJo_stands_name.csv")
stand_names = data.stands.tolist()
correct_guesses = []

while len(correct_guesses) < 28:
    if (answer in stand_names) and (answer not in correct_guesses):
        correct_guesses.append(answer)
        x_cor = sum(data[data.stands == answer].x.tolist())
        y_cor = sum(data[data.stands == answer].y.tolist())
        writing_names.goto(x_cor, y_cor)
        if answer == "Gold Experience Requiem":
            writing_names.write("Gold Experience", font=('Arial', 10, 'bold'))
            writing_names.goto(-32, 18)
            writing_names.write("Requiem", font=('Arial', 10, 'bold'))
        else:
            writing_names.write(answer, font=('Arial', 10, 'bold'))
    answer = screen.textinput(title="Guess The Stand", prompt="Name another Stand...").title()
# def get_mouse_click_coor(x, y):
#     print(x,",", y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
