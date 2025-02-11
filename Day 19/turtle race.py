from turtle import Turtle,Screen
import random


tim1=Turtle()
tim2=Turtle()



tim1.speed(1)
tim2.speed(1)

tim1.shape("turtle")
tim2.shape("turtle")
scr=Screen()
scr.setup(width=600,height=400)
choice = scr.textinput("Choose your turtle", "red or green:")

tim1.color("red")
tim2.color("green")





tim1.teleport(-600,20)
tim2.teleport(-600,-20)

while True:
    tim1.fd(random.randint(0,10))
    tim2.fd(random.randint(0,10))
    if tim1.position()[0]>=600 or tim2.position()[0]>=600:
        break


if tim1.position()[0]>=600:
    scr.title("Red turtle wins")
    scr.bgcolor("red")
if tim2.position()[0]>=600:
    scr.title("Green turtle wins")
    scr.bgcolor("green")

color=scr.bgcolor


if choice!=color:
    print("You Loose")
else:
    print("You Wins")


scr.exitonclick()


