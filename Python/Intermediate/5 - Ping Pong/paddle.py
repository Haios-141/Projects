from turtle import Turtle
from constants import SCREEN_HEIGHT

TURTLE_WIDTH = 5
TURTLE_LENGTH = 1
STEP = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=TURTLE_WIDTH, stretch_len=TURTLE_LENGTH)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() <= (SCREEN_HEIGHT / 2) - 70:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() >= (-SCREEN_HEIGHT / 2) + 70:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
