import turtle
import random

vibgyor_colors = [
    "violet",
    "indigo",
    "blue",
    "green",
    "yellow",
    "orange",
    "red"
]

# screen set-up and user input to place bet:
screen = turtle.Screen()
screen.setup(600,600)
screen.title("Welcome to Turtle Race")
screen.bgcolor("linen")
user_choice = screen.textinput("Time to Bet", "Choose your turtle's color from the following: Violet, Indigo, Blue, Green, Yellow, Orange, Red: ").lower()

# generate random colour for the turtles from a list:
def get_colour(color_list):
    new_colour = random.choice(color_list)
    color_list.remove(new_colour)
    return new_colour

# generate turtles of different colours and coordinates:
def create_turtle(colour, y_coordinate):
    my_turtle = turtle.Turtle(shape="turtle")
    my_turtle.color(colour)
    my_turtle.teleport(-280, y_coordinate)
    return my_turtle

race_turtles = []
start_point = -150

for i in range (0, 7):
    turtle_colour = get_colour(vibgyor_colors)
    new_turtle = create_turtle(colour=turtle_colour, y_coordinate=start_point)
    race_turtles.append(new_turtle)
    start_point += 50

is_race_on = False
if user_choice:
    is_race_on = True

winner_colour = ""

# keep the race on until one of the turtle reaches the end of the screen
while is_race_on:
    for current_turtle in race_turtles:
        available_speeds = ["fastest", "fast", "normal", "slow", "slowest"]
        random_distance = random.randint(5,40)
        current_turtle.penup()
        current_turtle.speed(random.choice(available_speeds))

        # ensure the turtles stop the race when a winner reaches the end of the screen
        if current_turtle.xcor() < 280:
            current_turtle.forward(random_distance)
        else:
            winner_colour = current_turtle.pencolor()
            is_race_on = False

# determine if the user has won or lost the bet
if winner_colour == user_choice:
    turtle.TK.messagebox.showinfo(title=f"{winner_colour.title()} turtle won!", message="Congratulations!")
else:
    turtle.TK.messagebox.showinfo(title=f"{winner_colour.title()} turtle won!", message="You lost the bet.")

screen.bye()