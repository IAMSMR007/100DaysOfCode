import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)




player = Player()

screen.listen()
screen.onkey(player.go_up,"Up")
car_manager=CarManager()
car_manager.finish_line()

scoreboard=Scoreboard()

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_manager.move()
    car_manager.carfactory()
    if player.ycor()>=250:
        player.teleport(0,-270)
        car_manager.speedup()
        scoreboard.level+=1
        scoreboard.refresh()

    for car in car_manager.carlist:
        if player.distance(car)<=20:
            game_is_on=False


