# import colorgram
# colors=colorgram.extract("image.jpeg",25)
#
#
# def get_color(how_many, ext_color):
#     lst = []
#     for i in range(how_many):
#         new_color=ext_color[i]
#         rgb=new_color.rgb
#         r=rgb.r
#         b=rgb.b
#         g=rgb.g
#         tup=(r,g,b)
#         lst.append(tup)
#     return lst
#
# print(get_color(25,colors))
import turtle
import random
tim=turtle.Turtle()
turtle.colormode(255)
colours=[(189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64),(64, 43, 43), (136, 149, 69), (127, 160, 172), (101, 79, 89), (83, 133, 108), (108, 39, 44), (39, 61, 47),  (211, 196, 124), (174, 150, 152), (36, 71, 88), (179, 106, 80), (36, 67, 84), (99, 140, 119)]
tim.teleport(-225,-220)
tim.pensize(20)
tim.penup()

for i in range(1,101):
    tim.dot(20,random.choice(colours))
    tim.forward(50)
    if (i%10)==0:
        x = tim.xcor()
        y = tim.ycor()
        tim.teleport(x-500,y+50)









screen=turtle.Screen()
screen.exitonclick()