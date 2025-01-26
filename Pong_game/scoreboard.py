from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("red")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.setposition(-100, 260)
        self.write(arg=f"Score = {self.l_score}", align=ALIGNMENT, font=FONT)
        self.setposition(100, 260)
        self.write(arg=f"Score = {self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
