from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = ScoreBoard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(key="Up", fun= player.move_player)

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # Detect collision
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            is_game_on = False
            scoreboard.game_over()

    # If player crosses the screen, the cars speed up and score gets updated
    if player.ycor() > 280:
        scoreboard.update_score()
        car_manager.increase_distance()

screen.exitonclick()
