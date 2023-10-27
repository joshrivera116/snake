from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
from gameover import GameOver

screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title('snake.ia')
screen.tracer(0)
gameover = GameOver
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_snake()
        scoreboard.increase_score()
    if snake.head.xcor() > 440 or snake.head.xcor() < - 440 or snake.head.ycor() > 440 or snake.head.ycor() < -440:
        game_is_on = False
        gameover()

    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            gameover()


screen.exitonclick()
