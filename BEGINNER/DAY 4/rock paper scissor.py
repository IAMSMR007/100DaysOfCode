rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Lets plar rock paper scissors")
user_input=int(input("Type 0 for rock ,1 for paper and 2 for scissors "))
if user_input==0:
    print('You chosses "ROCK" ')
    print(rock)
elif user_input==1:
    print('You chosses "PAPER" ' )
    print(paper)
elif user_input==2:
    print('You chosses "SCISSORS" ' )
    print(scissors)
else:
    print("Please Enter Valid Data")
import random
random_num=random.randint(0,2)
if (user_input==0) or (user_input==1) or (user_input==2):
    if random_num==0:
        print('Computer chosses "ROCK" ')
        print(rock)
    elif random_num==1:
        print('Computer chosses "PAPER" ' )
        print(paper)
    elif random_num==2:
        print('Computer chosses "SCISSORS" ' )
        print(scissors)


if random_num==user_input:
    print("DRAW")
elif (random_num==0) and (user_input==1):
    print("____________________YOU WIN ________________________")
elif (random_num == 1) and (user_input == 0):
    print("YOU LOOSE")
elif (random_num==0) and (user_input==2):
    print("YOU LOOSE")
elif (random_num==2) and (user_input==0):
    print("____________________YOU WIN ________________________")
elif (random_num==1) and (user_input==2):
    print("____________________YOU WIN ________________________")
elif (random_num==2) and (user_input==1):
    print("YOU LOSSE")
print("WANNA TRY AGAIN")
