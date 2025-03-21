from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SPAWNPOINT=[200,160,120,80,40,0,-40,-80,-120,-160,-200]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.carlist=[]
        self.STARTING_MOVE_DISTANCE = 5
        self.carno=10
        

    def move(self):
        for tut in self.carlist:
            tut.forward(self.STARTING_MOVE_DISTANCE)

    def carfactory(self):
        for i in range(1):
            if random.randint(1,self.carno)==1:
                turtle=Turtle()
                turtle.shape("square")
                turtle.setheading(180)
                turtle.shapesize(stretch_len=2)
                turtle.color(random.choice(COLORS))
                turtle.teleport(300,random.choice(SPAWNPOINT))
                turtle.setheading(180)
                turtle.penup()
                self.carlist.append(turtle)
    
    def finish_line(self):
        tut=Turtle()
        tut.hideturtle()
        tut.speed("fastest")
        tut.pencolor("white")
        tut.teleport(-300,250)
        for i in range(30):
            tut.pendown()
            tut.fd(10)
            tut.penup()
            tut.fd(10)

    def speedup(self):
        self.STARTING_MOVE_DISTANCE+=3
        self.carno-=1


        









        


    
