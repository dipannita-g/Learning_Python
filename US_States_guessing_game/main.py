import pandas
import turtle

FONT = ("Ariel", 8, "bold")
ALIGNMENT = "center"

screen = turtle.Screen()
screen.setup(width=800,height=500)
screen.title("U.S. States Map Quiz")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
all_answers = []

while len(all_answers) < 50:

    answer_state = screen.textinput(title="Time to Guess", prompt="What's another US state?").title()

    if answer_state in all_answers:
        answer_state = screen.textinput(title="Guessed already",  prompt="What's another US state?").title()

    if answer_state == "Exit":
        break

    answer_state_row = data[data.state == answer_state]
    answer_x_cor = answer_state_row.x.item()
    answer_y_cor = answer_state_row.y.item()

    if answer_state in list(data.state):
        state_name = turtle.Turtle()
        state_name.penup()
        state_name.hideturtle()
        state_name.goto(answer_x_cor, answer_y_cor)
        state_name.write(arg=f"{answer_state}", font=FONT, align=ALIGNMENT)
        all_answers.append(answer_state)

# Get states which were not guessed by the user in a csv file
states_to_learn = [item for item in state_list if item not in all_answers]
pandas.DataFrame(states_to_learn, columns = ["State"]).to_csv("states_to_learn.csv", index=False)
