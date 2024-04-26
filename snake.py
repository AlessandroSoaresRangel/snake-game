from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            self.segments.append(Turtle(shape="square"))
            self.segments[i].penup()
            if i - 1 >= 0:
                self.segments[i].goto(x=self.segments[i - 1].xcor() - 20, y=0)
            self.segments[i].color("white")

    def move(self):
        for snake_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_number - 1].xcor()
            new_y = self.segments[snake_number - 1].ycor()

            self.segments[snake_number].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)