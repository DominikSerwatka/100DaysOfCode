import time
from turtle import Screen
from Day23.car_manager import CarManager
from Day23.player import Player

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
#car_list = []
car = CarManager()
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
iteration = 0
while game_is_on:
    time.sleep(0.1)
    iteration += 1
    # if iteration % 6 == 0:
    #     car = CarManager()
    #     car_list.append(car)
    # for item in car_list:
    #     item.move()
    if iteration % 6 ==0:
        car.car_generator()
        # Detect collision
        if player.distance(item) < 30:
            game_is_on = False
    if player.detect_finish():
        for item in car_list:
            item.increase_speed()





    screen.update()



screen.exitonclick()