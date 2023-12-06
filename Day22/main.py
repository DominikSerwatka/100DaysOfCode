from turtle import Screen
import time
from Day22.ball import Ball
from Day22.paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_right = Paddle(x=350, y=0)
paddle_left = Paddle(x=-350, y=0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, 'w')
screen.onkey(paddle_left.down, 's')
# lfdfd

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()
    # Detect collision with right paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        # Detect Right paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        # Detect Left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()