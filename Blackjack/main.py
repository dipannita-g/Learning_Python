import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():
    return random.choice(cards)

def calculate_hand_score(hand):
    if sum(hand) > 21:
        print("You lose.")
        return False
    return True

def win_condition(user_score, dealer_score):
    if dealer_score > 21:
        print("You win!")
    elif user_score == dealer_score:
        print("Its a draw!")
    else:
        print("You lose.")


def check_ace_value(card_score,total):
    if card_score == 11:
        if total+card_score > 21:
            card_score = 1
            return card_score
    return card_score

def play_blackjack():
    user_hand = []
    dealer_hand = []
    user_hand.append(draw_card())
    dealer_hand.append(draw_card())
    ### Check Ace criteria here
    user_hand.append(check_ace_value(draw_card(), sum(user_hand)))
    print(f"Your cards are {user_hand}. Your score is {sum(user_hand)}.")
    print(f"Computer's first card is {dealer_hand}")
    game_not_over = True
    while game_not_over:
        continue_draw = input("Do you want to draw another card? Type Y or N: ").lower()
        if continue_draw == "y":
            ### Check Ace criteria here
            user_hand.append(check_ace_value(draw_card(), sum(user_hand)))
            print(f"Your cards are {user_hand}. Your score is {sum(user_hand)}.")
            game_not_over = calculate_hand_score(user_hand)

        elif continue_draw == "n":
            while sum(dealer_hand) < 21:
                ### Check Ace criteria here
                dealer_hand.append(check_ace_value(draw_card(), sum(dealer_hand)))
            print(f"Your final cards are {user_hand}. Your final score is {sum(user_hand)}.")
            print(f"Computer's final cards are {dealer_hand}. Its final score is {sum(dealer_hand)}.")
            win_condition(sum(user_hand), sum(dealer_hand))
            game_not_over = False

is_play = True
while is_play:
    user_play_choice = input("Do you want to play a game of Blackjack? Type Y or N: ").lower()
    if user_play_choice == "n":
        is_play = False
        exit()
    elif user_play_choice == "y":
        print(art.logo)
        play_blackjack()
    else:
        print("Incorrect input.")