from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("red")
        self.goto(-30, 275)
        self.write(arg=f"Score = {self.score}",align=ALIGNMENT, font=FONT)


    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score = {self.score}",align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER",align=ALIGNMENT, font=FONT)
