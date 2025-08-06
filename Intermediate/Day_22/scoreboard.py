from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"Score: {self.score_r}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"Score: {self.score_l}", align=ALIGNMENT, font=FONT)

    def point_l(self):
        self.score_l += 1
        self.update_score()

    def point_r(self):
        self.score_r += 1
        self.update_score()
