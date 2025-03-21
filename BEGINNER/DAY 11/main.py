import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def result(user_data,computer_data):
    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's Final Hand : {computer_cards}, Computer score: {sum(computer_cards)} ")
    if ((11 in computer_data) or (1 in computer_data)) and (10 in computer_data) and (len(computer_data)==2):
        print("Computer Has Black Jack . You Lose")
    elif ((11 in user_data) or (1 in user_data)) and (10 in user_data) and (len(user_data)==2):
        print("You Have Black Jack . You Wins")
    elif (sum(computer_data)>21) and (sum(user_data)>21):
        print("You both Went Over . Draw")
    elif sum(computer_data) > 21:
        print("Computer Went over . You Wins")
    elif sum(user_data)>21:
        print("You Went Over . You Lost")
    elif sum(computer_data) > sum(user_data):
        print("You Lost")
    elif sum(computer_data) < sum(user_data):
        print("You Wins")
    elif sum(computer_data) == sum(user_data):
        print("Draw")

def ace_check(data_type):
    if 11 in data_type:
        if sum(data_type) > 21:
            data_type[data_type.index(11)] = 1

user_cards=[]
computer_cards=[]

restart="y"
while restart=="y":

    restart = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if restart=="n":
        break

    user_cards = []
    computer_cards = []
    print("\n"*30)
    print(logo)
    for i in range(0,2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card:{computer_cards[0]}")

    while sum(computer_cards)<16:
        computer_cards.append(random.choice(cards))
        ace_check(computer_cards)
    ace_check(user_cards)
    while True:
        extra = input("Type 'y' to get another card, type 'n' to pass: ")

        if extra == "n":
            break

        user_cards.append(random.choice(cards))
        ace_check(user_cards)
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")

        if sum(user_cards)>21:
            break

    print("")
    result(user_cards,computer_cards)