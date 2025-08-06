# Pong Game

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()
ball = Ball()
paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))

screen.listen()
screen.onkey(paddle_r.go_up, 'Up')
screen.onkey(paddle_r.go_down, 'Down')
screen.onkey(paddle_l.go_up, 'w')
screen.onkey(paddle_l.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #colision of ball with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    #colision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #ball misses the paddle_r
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.point_l()

    #ball misses the paddle_l
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.point_r()


screen.exitonclick()
