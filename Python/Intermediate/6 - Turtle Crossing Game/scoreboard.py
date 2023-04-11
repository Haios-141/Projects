from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.__level = 1
        self.penup()
        self.hideturtle()
        self.__display_score()

    def increase_level(self):
        self.__level += 1
        self.__display_score()

    def __display_score(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.__level}", align="left",  font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=FONT)
