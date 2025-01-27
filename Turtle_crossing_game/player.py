from turtle import Turtle

START_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(START_POSITION)

    def move_player(self):
        if self.ycor() <290:
            self.forward(MOVE_DISTANCE)
        else:
            self.goto(START_POSITION)
