import time
from turtle import Screen
from Day23.car_manager import CarManager
from Day23.player import Player
from Day23.scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.detect_finish():
        player.reset_position()
        car_manager.level_up()
        scoreboard.add_to_score()

screen.exitonclick()
