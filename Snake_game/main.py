from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("grey")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()

    if snake.square_list[0].distance(food)<20:
        #increase the scorecard whenever a snake catches food
        print("nom mop nom")
        food.refresh()
        score.increase_score()
        snake.extend_snake()

    if snake.square_list[0].xcor() >310 or snake.square_list[0].xcor() <-310 or snake.square_list[0].ycor() >310 or snake.square_list[0].ycor() <-310:
        #if snake hits a wall, its game over
        score.reset_score()
        snake.reset_snake()

    for square in snake.square_list:
        # detect collision with tail
        if square == snake.square_list[0]:
            pass

        elif snake.square_list[0].distance(square) < 10:
            score.reset_score()
            snake.reset_snake()




screen.exitonclick()