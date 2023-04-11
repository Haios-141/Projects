from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.setheading(180)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.randrange(-250, 250, 10))
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def car_reuse(self):
        for car in self.all_cars:
            if car.xcor() < -800:
                self.all_cars.remove(car)
