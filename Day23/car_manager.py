from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        new_y = random.randint(-250, 250)
        self.goto(x=400, y=new_y)
        self.move_speed_up = 0
        self.car_list = []

    def move(self):
        for item in self.car_list:
            new_x = item.xcor()-STARTING_MOVE_DISTANCE-item.move_speed_up
            item.goto(new_x, item.ycor())

    def increase_speed(self):
        self.move_speed_up += MOVE_INCREMENT

    def car_generator(self):
        car = CarManager()
        self.car_list.append(car)





