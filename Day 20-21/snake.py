from turtle import Turtle


class Snake:

    def __init__(self):

        self.segments=[]
        self.create_snake()


    def create_snake(self):
        x = 0
        for i in range(3):
            tim=Turtle()
            tim.color("white")
            tim.shape("square")
            tim.penup()
            tim.goto(x,0)  # Corrected from teleport to goto
            x-=20
            self.segments.append(tim)


    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].fd(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading()!=90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def extend(self):
        position=self.segments[-1].position()
        tim=Turtle()
        tim.color("white")
        tim.shape("square")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)





