from turtle import Turtle

FONT = ("Ariel", 15, "normal")
ALIGNMENT = "center"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-270, 270)
        self.write(arg=f"Level: {self.score}", font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Level: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", font=FONT, align=ALIGNMENT)
