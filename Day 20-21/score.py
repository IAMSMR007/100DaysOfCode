from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score=0
        self.high_score=0
        self.penup()
        self.goto(0,280)
        self.write(f"Score: {self.score}",False,"center",("Arial", 10, "normal"))

        

    def gain(self):
        self.score+=1
        # self.write(f"Score: {self.score}",False,"center",("Arial", 10, "normal"))
        self.update_scoreboard()

    


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score : {self.high_score}",align="center",font=("Arial", 10, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("high.txt", mode="w") as data:
            data.write(f"{self.high_score}")
        self.update_scoreboard()




