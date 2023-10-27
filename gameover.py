from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 20, 'normal')


class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.write(arg=f'Game Over', align=ALIGNMENT, move=False, font=FONT)
