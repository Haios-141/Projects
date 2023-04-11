from turtle import Screen, textinput
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random

play = True
screen = Screen()

while play:
    screen.clear()
    screen.setup(width=600, height=600)
    # screen.setup(width=400, height=400)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")
    screen.onkeypress(snake.pause, "space")

    game_is_on = True
    while game_is_on:

        screen.update()
        time.sleep(0.1)

        if snake.pause_state is False:
            snake.move()

            # Detect collision with food
            if snake.head.distance(food) < 14:
                random_x = random.randrange(-260, 260, 20)
                random_y = random.randrange(-260, 260, 20)

                for segment in snake.segments:
                    if segment.position() != (random_x, random_y):
                        food.refresh(random_x, random_y)

                snake.extend_snake()
                scoreboard.increase_score()

            # Detect collision with wall
            if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or\
                    snake.head.ycor() < -280:
                scoreboard.reset_score()
                game_is_on = False
                scoreboard.game_over()

            # Detect collision with tail
            for segment in snake.segments[1:]:  # Skip over the first segment to avoid it colliding with itself
                if snake.head.distance(segment) < 10:
                    scoreboard.reset_score()
                    game_is_on = False
                    scoreboard.game_over()

    response = textinput(title="Play again?", prompt="Play again? Enter 'Yes' or 'No': ").lower()
    while response != "yes" and response != "y" and response != "no" and response != "n":
        response = textinput(title="Play again?", prompt="Play again? Enter 'Yes' or 'No': ").lower()

    if response == "no" or response == "n":
        play = False


screen.exitonclick()
