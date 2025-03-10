import turtle
import pandas
screen=turtle.Screen()
screen.title("QUIZ GAME")
screen.bgpic("blank_states_img.gif")
tim=turtle.Turtle()
tim.hideturtle()
tim.penup()
data=pandas.read_csv("50_states.csv")
state_data=data["state"].to_list()
xcor=list(data.x)
ycor=list(data.y)
state_data=list(state_data)
game_on=True
guessed_list=[]
correct=0
prompt="guess  the state"
while game_on:
    user_guess=screen.textinput(title=f"Score:{correct}/50",prompt=prompt).title()
    if user_guess=="Exit":
        game_on=False
        missing_state=[state for state in state_data if state not in guessed_list]
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
    elif user_guess in state_data:
        prompt="guess  the state"
        index=state_data.index(user_guess)
        new_x=xcor[index]
        new_y=ycor[index]
        tim.goto(new_x,new_y)
        tim.write(user_guess,False,align="center",font=("Courier", 7, "normal"))
        if user_guess not in guessed_list:
            correct+=1
            guessed_list.append(user_guess)
    elif correct==50:
        game_on=False
    else:
        prompt="Wrong,guess again"

