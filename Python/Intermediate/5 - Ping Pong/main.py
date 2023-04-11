from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from middle_barrier import Divider
import keyboard
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BARRIER
import time

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.tracer(0)

l_paddle_position = (-350, 0)
r_paddle_position = (350, 0)

l_paddle = Paddle(l_paddle_position)
r_paddle = Paddle(r_paddle_position)
ball = Ball()
scoreboard = Scoreboard()
divider = Divider()
divider.draw_divider()

screen.listen()
# Left Paddle controls
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# Right Paddle controls
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

PADDLE_LEN = 100
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collisions with the top and bottom walls
    if ball.ycor() >= (SCREEN_HEIGHT / 2) - SCREEN_BARRIER or ball.ycor() <= (-SCREEN_HEIGHT / 2) + SCREEN_BARRIER:
        ball.bounce_y()

    # Detect collisions with the paddles
    if ball.xcor() < (l_paddle.xcor() + 30):
        if l_paddle.ycor() + (PADDLE_LEN / 2) > ball.ycor() > l_paddle.ycor() - PADDLE_LEN / 2:
            ball.bounce_x()
    elif ball.xcor() > (r_paddle.xcor() - 30):
        if r_paddle.ycor() + (PADDLE_LEN / 2) > ball.ycor() > r_paddle.ycor() - PADDLE_LEN / 2:
            ball.bounce_x()

    # Left Player Wins
    if ball.xcor() >= (SCREEN_WIDTH / 2) - SCREEN_BARRIER:
        ball.reset_position()
        scoreboard.l_point()

    # Right Player Wins
    if ball.xcor() <= (-SCREEN_WIDTH / 2) + SCREEN_BARRIER:
        ball.reset_position()
        scoreboard.r_point()

    if keyboard.is_pressed("Escape"):
        game_is_on = False

screen.bye()
# screen.exitonclick()
