import turtle
import random

timmy=turtle.Turtle()
screen=turtle.Screen()

timmy.pensize(15)
timmy.speed("fastest")

turtle.colormode(255)

def random_colour():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color=(r,b,g)
    return random_color


direction=[0,90,180,270]
for i in range(100):
    timmy.color(random_colour())
    timmy.forward(random.randint(0,50))
    timmy.setheading(random.choice(direction))



screen.exitonclick()