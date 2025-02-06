from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score=0
        self.penup()
        self.goto(-270,280)
        self.write(f"Score: {self.score}",False,"center",("Arial", 10, "normal"))
        

    def gain(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}",False,"center",("Arial", 10, "normal"))
    
    def game_over(self):
        self.goto(0,0)

        self.write("GAME OVER",False,"center",("Arial", 30, "normal"))




