from turtle import Turtle , Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
screen.setup(width=600,height=600)
snake = Snake()
food = Food()
scoreBoard = Scoreboard()

screen.onkey(key="w",fun=snake.moveup)
screen.onkey(key="s",fun=snake.movedown)
screen.onkey(key="d",fun=snake.moveright)
screen.onkey(key="a",fun=snake.moveleft)





game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreBoard.increase_score()
    if snake.head.xcor() > 295 or snake.head.xcor()<-295 or snake.head.ycor()>299 or snake.head.ycor()<-295:
       scoreBoard.reset()
       snake.reset()
        # game_is_on = False
        # scoreBoard.gameOver()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreBoard.reset()
            snake.reset()
            # game_is_on = False
            # scoreBoard.gameOver()


screen.exitonclick()