import random
import turtle as tu
timmy=tu.Turtle()
screen=tu.Screen()
timmy.teleport(0,100)

colour_list=["light sea green","dark goldenrod",
    "firebrick",
    "deep pink",
    "turquoise"
    ]
def draw_shape(side):
    angle=360/side
    color=""
    for i in range(side):
        timmy.right(angle)
        timmy.fd(100)

for sid in range(3,11):
    draw_shape(sid)
    timmy.color(random.choice(colour_list))

screen.exitonclick()