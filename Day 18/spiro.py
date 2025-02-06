import turtle
import random

timmy=turtle.Turtle()
screen=turtle.Screen()

timmy.speed(100)

turtle.colormode(255)

def random_colour():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color=(r,b,g)
    return random_color

def draw_spirograph(gap):
    for i in range(int(360/gap)):
        timmy.color(random_colour())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+gap)

draw_spirograph(1)
screen.exitonclick()