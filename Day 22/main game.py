from turtle import Turtle,Screen
from paddle_control import Paddle
from ball_controler import Ball
import time
from scoreboard import ScoreBoard



#setup of game screen
scr=Screen()
scr.bgcolor("black")

scr.setup(width=800,height=600)
scr.textinput("Welcome","Press Enter:")
scr.tracer(0)



#making turtle to write score
timmy=Turtle()
timmy.pencolor("yellow")
timmy.hideturtle()
timmy.penup()



# code for making a boundary for game
tim=Turtle()
tim.speed("fastest")
tim.color("red")
tim.pensize(10)
tim.hideturtle()
tim.teleport(-400,300)
tim.forward(800)
tim.setheading(270)
tim.forward(600)
tim.setheading(180)
tim.forward(800)
tim.setheading(90)
tim.forward(600)
tim.teleport(0,-300)
tim.forward(600)
tim.teleport(0,30)



scr.listen()



#making of paddle-1
paddle_r=Paddle()
paddle_r.goto(380, 0)
scr.onkey(paddle_r.up, "Up")
scr.onkey(paddle_r.down, "Down")



#making of paddle-2
paddle_l=Paddle()
paddle_l.goto(-380, 0)
scr.onkey(paddle_l.up, "w")
scr.onkey(paddle_l.down, "s")



ball=Ball()
scoreboard=ScoreBoard()

sleep_time=0.1

game_is_on=True
while game_is_on:
    scr.update()
    time.sleep(sleep_time)

    ball.move()
    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.bounce()



    #detect ball collision with paddle

    if ball.xcor() >= 360 and ball.distance(paddle_r)<=50:
        ball.deflect()
        sleep_time *= 0.9




    if ball.xcor() <= -360 and ball.distance(paddle_l)<=50:
        ball.deflect()
        sleep_time *= 0.9





    #detect ball goes out of boundary
    if ball.xcor()>=440:
        sleep_time = 0.1

        timmy.clear()
        scoreboard.l_score()
        scoreboard.refresh()
        timmy.goto(-300, 250)

        timmy.write("SCORE!!", move=False, font=("Arial", 30, "normal"), align="center")

        ball.deflect()
        ball.goto(0,0)



    if ball.xcor()<=-440:
        sleep_time = 0.1

        timmy.clear()
        scoreboard.r_score()
        scoreboard.refresh()
        timmy.goto(300,250)

        timmy.write("SCORE!!",move=False,font=("Arial",30,"normal"),align="center")

        ball.deflect()
        ball.goto(0, 0)


    if scoreboard.l_data() >= 7 :
        game_is_on =False
        timmy.goto(-280, -250)

        timmy.write("VICTORY!!", move=False, font=("Arial", 30, "normal"), align="center")

    if scoreboard.r_data() >= 7 :
        game_is_on =False
        timmy.goto(280, -250)

        timmy.write("VICTORY!!", move=False, font=("Arial", 30, "normal"), align="center")
















scr.exitonclick()