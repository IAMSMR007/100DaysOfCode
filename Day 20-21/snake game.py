from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from score import Score
screen=Screen()
screen.bgcolor("black")
# screen.bgpic("bg.jpg")
screen.title("Snake simulator")
screen.setup(width=600,height=600)
screen.textinput("Welcome to Snake Game","Press Enter to start the game")



border=Turtle()
border.pencolor("white")
border.speed("fastest")
border.teleport(300,300)
border.setheading(180)
border.hideturtle()
for _ in range(4):
    border.forward(600)
    border.left(90)

screen.tracer(0)

#snake body
snake=Snake()
food=Food()
score=Score()
#snake movement
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")





#snake move
game_on=True
while game_on:

    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.segments[0].distance(food)<15:
        food.refresh()
        score.gain()
        snake.extend()
    
    #detect collision with wall
    if snake.segments[0].xcor()>=300 or snake.segments[0].xcor()<=-300 or snake.segments[0].ycor()>=300 or snake.segments[0].ycor()<=-300:
        snake.reset()
        score.reset()
    
    #detect collision with body
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<=10:
            snake.reset()
            score.reset()

screen.exitonclick()