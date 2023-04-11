from turtle import Turtle

ALIGNMENT = "center"
FONT_TYPE = ("Courier", 16, "normal")
FILE_NAME = "data.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.__score = 0

        with open(FILE_NAME) as f:
            self.high_score = int(f.read())

        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 275)
        self.__update_scoreboard()

    def increase_score(self):
        # self.clear()
        self.__score += 1
        self.__update_scoreboard()

    def reset_score(self):
        if self.__score > self.high_score:
            self.high_score = self.__score

            with open(FILE_NAME, mode="w") as f:
                f.write(str(self.high_score))

        self.__score = 0
        self.__update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", False, ALIGNMENT, FONT_TYPE)

    def __update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.__score} High Score: {self.high_score}", False, ALIGNMENT, FONT_TYPE)
