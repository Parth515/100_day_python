import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


y_1 = -100
Not_finished = False
all_turtle = []

for i in colors:
    tim_i = Turtle(shape="turtle")
    tim_i.color(f"{i}")
    tim_i.penup()
    tim_i.goto(x=-230, y=y_1)
    y_1 += 45
    all_turtle.append(tim_i)

if user_bet:
    Not_finished = True

while Not_finished:
    for turtle in all_turtle:
        if turtle.xcor() > 225:
            Not_finished = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You have won! The {win_color} turtle is the winner.")
            else:
                print(f"You have lost! The winner is {win_color} turtle.")



        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)



'''def move_forward():
    tim.forward(100)

screen.onkey(key = "c", fun = clear_drawing)'''
screen.exitonclick()
