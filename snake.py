from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.color = 'white'
        self.shape = 'circle'
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 40
        for turtle in range(3):
            turtles = Turtle(self.shape)
            turtles.penup()
            turtles.color(self.color)
            turtles.goto(x, 0)
            self.segments.append(turtles)
            x -= 20

    def snake_move(self):
        for segn in range(len(self.segments) - 1, 0, -1):
            self.segments[segn].goto(self.segments[segn - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def add_snake(self):
        new_turtle = Turtle(self.shape)
        new_turtle.penup()
        new_turtle.color(self.color)
        new_turtle.goto(self.segments[-1].pos())
        self.segments.append(new_turtle)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
