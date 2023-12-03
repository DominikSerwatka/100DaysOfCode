#Damien Hirst spot project

import colorgram
import turtle as t
import random
from turtle import Screen


def extract_color():
    colors = colorgram.extract('DamienHirst.jpg', 30)

    list_of_colors = []
    for item in colors:
        r = item.rgb[0]
        g = item.rgb[1]
        b = item.rgb[2]
        list_of_colors.append((r, g, b))
    print(list(list_of_colors))


color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50),
              (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132),
              (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177),
              (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185),
              (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83),
              (245, 205, 7), (35, 88, 88), (103, 24, 56)]


def draw_dot():
    tim.dot(20, random.choice(color_list))


def draw_dot_line(number):
    for _ in range(number):
        draw_dot()
        tim.penup()
        tim.forward(50)
    tim.forward(-50)


def draw_dot_painting(number_of_lines, number):
    for _ in range(number_of_lines):
        draw_dot_line(number)
        tim.forward(-((number - 1) * 50))
        tim.right(-90)
        tim.forward(50)
        tim.right(90)


tim = t.Turtle()
tim.hideturtle()
screen = Screen()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.forward(-200)
tim.right(90)
tim.forward(200)
tim.right(-90)
draw_dot_painting(10, 10)
screen.exitonclick()
