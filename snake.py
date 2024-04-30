from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.head = None
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            self.add_segment()

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        if self.head is None or not self.segments:
            self.head = new_segment
        new_segment.penup()
        if new_segment is not self.head:
            new_segment.goto(x=self.segments[self.segments.index(self.segments[-1]) - 1].xcor() - 20,
                             y=self.segments[self.segments.index(self.segments[-1]) - 1].ycor())

        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,  1000)
        self.segments.clear()
        self.create_snake()

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
