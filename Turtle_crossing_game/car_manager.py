from turtle import Turtle
import random

COLOURS = ["cyan4", "midnight blue", "medium purple", "forest green", "red3", "orange"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.distance_to_move = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2, outline=None)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLOURS))
            new_car.goto((270, random.randint(-250,250)))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.distance_to_move)

    def increase_distance(self):
        self.distance_to_move += MOVE_INCREMENT
