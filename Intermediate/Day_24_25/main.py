# The State Guessing Game

import turtle
import pandas

FONT = ("Courier", 6, "normal")

guessed_states = []


'''def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
'''

state_data = pandas.read_csv("50_states.csv")
state_names = state_data.state.to_list()

def write_state(st, x_1, y_1):
    tim = turtle.Turtle()
    tim.hideturtle()
    tim.penup()
    tim.goto(x_1, y_1)
    tim.write(f"{st}", align="left", font=FONT)

while len(guessed_states) < 50:
    screen = turtle.Screen()
    screen.title("U.S. State Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states are correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_state = []
        for state in state_names:
            if state not in guessed_states:
                missing_state.append(state)
        df = pandas.DataFrame(missing_state)
        df.to_csv("state_to_learn.csv")
        break

    if answer_state in state_names:
        guessed_states.append(answer_state)
        state = state_data[state_data.state == answer_state]
        x_cord = state.x.item()
        y_cord = state.y.item()
        write_state(state.state.item(),x_cord,y_cord)



