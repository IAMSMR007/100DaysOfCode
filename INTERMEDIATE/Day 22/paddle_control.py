from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.color("white")

        self.setheading(90)
        self.shapesize(stretch_len=5)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)







