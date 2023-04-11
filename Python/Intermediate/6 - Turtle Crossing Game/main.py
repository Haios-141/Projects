import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("azure")
screen.title("Turtle Crossing the Road")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

create_car_counter = 1
car_speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(car_speed)
    screen.update()

    if create_car_counter == 6:

        car_manager.create_car()
        create_car_counter = 0

    if len(car_manager.all_cars) > 0:
        car_manager.move_cars()

        if player.reached_finish_line():
            player.go_to_start()
            car_speed *= 0.6
            scoreboard.increase_level()

        # Detect collision with cars
        for car in car_manager.all_cars:
            if car.distance(player.position() + (10, 5)) <= 20:
                game_is_on = False
                scoreboard.game_over()

        # Remove car objects from the list after it reaches an x co-ordinate of -320
        car_manager.car_reuse()

    create_car_counter += 1

screen.exitonclick()
