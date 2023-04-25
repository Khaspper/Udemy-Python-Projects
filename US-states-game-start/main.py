import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state = turtle.Turtle()
state.penup()
state.hideturtle()
state.speed(0)


answer_state = screen.textinput(title="Guess The State", prompt="Name a state...")

us_CSV = pandas.read_csv("50_states.csv")
state_list = us_CSV.state.tolist()

correct_guesses = []

while len(correct_guesses) < 50:
    if answer_state.lower() == "exit":
        break
    answer_state = answer_state.title()
    if (answer_state in state_list) and (answer_state not in correct_guesses):
        correct_guesses.append(answer_state)
        x_cor = sum(us_CSV[us_CSV.state == answer_state].x.to_list())
        y_cor = sum(us_CSV[us_CSV.state == answer_state].y.to_list())
        state.goto(x_cor, y_cor)
        state.write(answer_state, font=('Arial', 12, 'normal'))
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="Name a state...")







# screen.exitonclick()

# * to get the x and y values of where you clicked

# def get_mouse_click_cor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cor())
