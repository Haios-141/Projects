from turtle import Turtle
import random

FOOD_WIDTH = 0.5
FOOD_LEN = 0.5
# RANDOM_X = random.randrange(-160, 160, 20)
# RANDOM_Y = random.randrange(-160, 160, 20)
RANDOM_X = random.randrange(-260, 260, 20)
RANDOM_Y = random.randrange(-260, 260, 20)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=FOOD_WIDTH, stretch_len=FOOD_LEN)
        self.color("purple")
        self.speed("fastest")
        self.refresh(RANDOM_X, RANDOM_Y)

    def refresh(self, x_cor, y_cor):
        self.goto(x_cor, y_cor)
