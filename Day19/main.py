import turtle
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
list_of_turtle = []
co_y = -70
for item in colors:
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(item)
    tim.goto(x=-230, y=co_y)
    co_y += 30
    list_of_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for item in list_of_turtle:
        if item.xcor() > 230:
            is_race_on = False
            winning_color = item.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_dist = random.randint(0, 10)
        item.forward(rand_dist)





screen.exitonclick()
