from turtle import Turtle
import random

colours = [
    "salmon3",
    "PaleTurquoise4",
    "LightSteelBlue2",
    "MistyRose2",
    "DarkGoldenrod2",
    "VioletRed1",
    "MediumPurple4",
    "DarkOrange2",
    "firebrick3",
    "ivory4",
]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(colours))
        self.setheading(random.randint(0,360))
        random_x = random.randint(-250,250)
        random_y = random.randint(-250,250)
        self.goto(random_x, random_y)
