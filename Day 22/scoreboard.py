from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.padr_score = 0
        self.padl_score = 0
        self.goto(100,200)
        self.write(self.padr_score, False, align="center", font=("Courier", 50, "normal"))
        self.goto(-100, 200)
        self.write(self.padl_score, False, align="center", font=("Courier", 50, "normal"))

    def l_score(self):
        self.padl_score +=1

    def r_score(self):
        self.padr_score +=1

    def refresh(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.padr_score, False, align="center", font=("Courier", 50, "normal"))
        self.goto(-100, 200)
        self.write(self.padl_score, False, align="center", font=("Courier", 50, "normal"))

    def l_data(self):
        return self.padl_score

    def r_data(self):
        return self.padr_score





