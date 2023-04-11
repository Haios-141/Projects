from turtle import Turtle

ALIGNMENT = "center"
FONT_TYPE = ("Courier", 80, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.__l_score = 0
        self.__r_score = 0
        self.__update_scoreboard()

    def __update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.__l_score, align=ALIGNMENT, font=FONT_TYPE)
        self.goto(100, 200)
        self.write(self.__r_score, align=ALIGNMENT, font=FONT_TYPE)

    def l_point(self):
        self.__l_score += 1
        self.__update_scoreboard()

    def r_point(self):
        self.__r_score += 1
        self.__update_scoreboard()
