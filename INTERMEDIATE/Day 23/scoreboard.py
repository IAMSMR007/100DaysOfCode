from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-200,250)
        self.hideturtle()
        self.pencolor("white")
        self.level=1
        self.write(f"level : {self.level}",move=False,align="center",font=FONT)

    def refresh(self):
        self.clear()
        self.write(f"level : {self.level}",move=False,align="center",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER MAN !",move=False,align="center",font=FONT)
