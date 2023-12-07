from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.start_position()

    def start_position(self):
        self.color("black")
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.goto(STARTING_POSITION)

    def move(self):
        next_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=0, y=next_y)

    def reset_position(self):
        self.reset()
        self.start_position()

    def detect_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.reset_position()
            return True



