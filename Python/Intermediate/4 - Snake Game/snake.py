from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.__create_snake()
        self.head = self.segments[0]
        self.head.color("brown")
        self.__direction_change = False
        self.pause_state = False

    def __create_snake(self):
        for pos in STARTING_POSITIONS:
            self.__add_segment(pos)

    def __add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.color("orange")
        # snake_segment.shapesize(0.9, 0.9)
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend_snake(self):
        """Add a new segment to the snake."""
        self.__add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.__direction_change = False

    def up(self):
        if self.head.heading() != DOWN and self.__direction_change is False:
            self.head.setheading(UP)
            self.__direction_change = True

    def down(self):
        if self.head.heading() != UP and self.__direction_change is False:
            self.head.setheading(DOWN)
            self.__direction_change = True

    def left(self):
        if self.head.heading() != RIGHT and self.__direction_change is False:
            self.head.setheading(LEFT)
            self.__direction_change = True

    def right(self):
        if self.head.heading() != LEFT and self.__direction_change is False:
            self.head.setheading(RIGHT)
            self.__direction_change = True

    def pause(self):
        if self.pause_state is False:
            self.pause_state = True
        else:
            self.pause_state = False
