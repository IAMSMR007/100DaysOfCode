from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.teleport(random.randint(300,400),random.randint(-300,300))
        self.setheading(180)
        self.penup()





    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def new_car(self):
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.teleport(random.randint(300,400),random.randint(-300,300))
        self.setheading(180)




        


    
