#1 Error Handling for User Input:

#2 The user input is not validated. Add checks for invalid inputs like empty strings or inputs other than 'A' or 'B'.
# Game Termination:

#3 The loop could lead to an infinite loop if game_data becomes empty.
# Add a condition to check if game_data has fewer than two entries and exit gracefully.
# Global Variables:

#4 r1_data and r2_data are global. Consider passing them as function parameters for better encapsulation.
# Unused Variables:

#5 The variable vs is printed but not defined. It should contain the string or symbol used to visually separate the comparisons.
# Formatting:

#6 Use consistent indentation (PEP 8 style guide recommends 4 spaces).
# Add comments to improve readability.
# Code Cleanup:

#7 Remove commented-out code or ensure it's purposeful.

from game_data import data
from art import vs,logo
import random

print(logo)

#Global Variables
score=0
r1_data={}
r2_data={}
game_data=data


def random_data():
    """pick random slot of data from game data and remove it"""
    x=random.choice(game_data)
    game_data.remove(x)
    return x

def data_display(dict_found,x):
    """"display data for user to pridict"""
    print(f"Compare {x}: {dict_found['name']} ,a {dict_found['description']} ,from {dict_found['country']}")

def compare(data_a,data_b):
    """compare A and B data and return who has more follows"""
    if data_a['follower_count']>data_b['follower_count']:
        return 'A'
    elif data_b['follower_count']>data_a['follower_count']:
        return 'B'




while True:
    if score==0:
        r1_data=random_data()
        data_display(r1_data,"A")
    else:
        r1_data = r2_data
        data_display(r2_data, "A")
    print(vs)
    r2_data=random_data()
    data_display(r2_data,"B")

    more_followers = compare(r1_data, r2_data)
    high_or_low=input("Who has more followers? Type 'A' or 'B':")


    if high_or_low==more_followers:
        score+=1
        print(f"You're right! Current score {score}")
    elif high_or_low!=more_followers:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
    print("")
    if len(game_data)==2:
        break


