from turtle import  *
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend_snake()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #scoreboard.game_over()
        #game_is_on = False
        scoreboard.reset_game()
        snake.reset_snake()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            #scoreboard.game_over()
            #game_is_on = False
            scoreboard.reset_game()
            snake.reset_snake()
screen.exitonclick()
