from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect collision with food and update score
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if snake.head.xcor() >=280 or snake.head.xcor() <= -280 or snake.head.ycor() >=280 or snake.head.ycor() <= -280:
        is_game_on = False
        scoreboard.game_over()

    # Detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
