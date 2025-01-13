import art
import game_data
import random

# Generate two random indices from the game data which will be used as the initial index values of items.
# The two numbers should never be equal.
def generate_two_random_numbers():
    while True:
        random_number_a = random.randint(0, len(game_data.data) - 1)
        random_number_b = random.randint(0, len(game_data.data) - 1)
        if random_number_a != random_number_b:
            return random_number_a, random_number_b

def generate_only_b_number(ind_a):
    while True:
        new_ind_b = random.randint(0, len(game_data.data) - 1)
        if ind_a != new_ind_b:
            return new_ind_b

# Function to get the user input and catch any input errors.
def get_user_input():
    while True:
        try:
            user_answer = input("Who has more followers? Type A or B: ").lower()
            if user_answer not in ["a", "b"]:
                raise ValueError("Invalid input! Please try again.")
            return user_answer

        except ValueError as e:
              print(f"Error: {e}")

# Compare the parameters to decide the correct answer
def check_follower_count():
    if a_follower_count > b_follower_count:
        return "a"
    elif b_follower_count > a_follower_count:
        return "b"

# Function to check if the user input is equal to the correct answer or not.
# Update total score.
# Convert Choice A to Choice B and generate new Choice B if the user input is correct.
def is_user_correct(user_score, ind_b):
    if check_follower_count() != user_choice:
        print(f"Sorry, that's wrong. Final score is {user_score}")
        exit()
    else:
        user_score += 1
        print(f"You are right! Your current score is {user_score}")
        ind_a = ind_b
        new_ind_b = generate_only_b_number(ind_a)
        return user_score, ind_a, new_ind_b


print(art.logo)

index_for_a, index_for_b = generate_two_random_numbers()
total_user_score = 0
game_on = True # Set condition so that the game keeps playing until the user gives incorrect answer using while loop.

while game_on:
    a_name = (game_data.data[index_for_a]["name"])
    a_description = (game_data.data[index_for_a]["description"])
    a_country = (game_data.data[index_for_a]["country"])
    a_follower_count = (game_data.data[index_for_a]["follower_count"])

    b_name = (game_data.data[index_for_b]["name"])
    b_description = (game_data.data[index_for_b]["description"])
    b_country = (game_data.data[index_for_b]["country"])
    b_follower_count = (game_data.data[index_for_b]["follower_count"])

    # print(f"{a_follower_count}, {b_follower_count}")
    print(f"Compare A: {a_name}, {a_description}, {a_country}")
    print(art.vs)
    print(f"Compare B: {b_name}, {b_description}, {b_country}")

    user_choice = get_user_input()
    total_user_score, index_for_a, index_for_b = is_user_correct(total_user_score, index_for_b)
