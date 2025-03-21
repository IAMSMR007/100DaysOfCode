from art import logo
import random

print(logo)
print("Welcome to Guess The Number Game")
print("I'm thinking of a number between 1 and 100.")
main_number=random.randint(0,101)
print(f"Pssst, the correct answer is {main_number}") #Test

chance=0

diff=input("Choose a difficulty. Type 'easy' or 'hard': ")

if diff=="hard":
    chance=5
else:
    chance=10
print(f"You have {chance} attempts remaining to guess the number.")

guessed_number=-1

while (chance>0) and (guessed_number!=main_number):
    guessed_number=int(input("Make a guess:"))
    if main_number>guessed_number:
        print("Too Low . \nGuess Again")
    if main_number<guessed_number:
        print("Too High \nGuess Again")
    chance-=1
    print(f"You have {chance} attempts remaining to guess the number.")

if guessed_number==main_number:
    print(f"You Got It . The number Is {guessed_number}")
else:
    print(f"Ops You Loose . The number Is {main_number}")





