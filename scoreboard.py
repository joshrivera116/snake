from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 420)
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, move=False, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, move=False, font=FONT)
