MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
emoji = "☕"
profit = 0

def get_user_choice():
    """Asks user for their choice of coffee"""
    while True:
        try:
            user_coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if user_coffee_choice not in  ["espresso", "latte", "cappuccino", "off", "report"]:
                raise ValueError("Invalid input! Please try again.")
            return user_coffee_choice
        except ValueError as e:
              print(f"Error: {e}")

def check_resources(user_choice):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in MENU[user_choice]["ingredients"]:
        if MENU[user_choice]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def ask_for_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    user_payment = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    return user_payment

# Note: quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
def check_coins(user_choice, user_money):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if user_money < MENU[user_choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif user_money > MENU[user_choice]["cost"]:
        to_refund = round(user_money - MENU[user_choice]["cost"], 2)
        print(f"Here is ${to_refund} dollars in change.")
    else:
        print(f"Thanks for the payment.")
    return True

# If transaction successful, deduct resources to make coffee and print final coffee statement.
machine_is_on = True
while machine_is_on:
    user_drink = get_user_choice()
    if user_drink == "off":
        machine_is_on = False
    elif user_drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif user_drink in  ["espresso", "latte", "cappuccino"]:
        enough_resources = check_resources(user_drink)
        if enough_resources is True:
            user_pays = ask_for_coins()
            is_enough_money = check_coins(user_drink, user_pays)
            if is_enough_money is True:
                for i in MENU[user_drink]["ingredients"]:
                    resources[i] -= MENU[user_drink]["ingredients"][i]
                profit+= MENU[user_drink]["cost"]
                print(f"Here is your {user_drink} {emoji}. Enjoy!")
