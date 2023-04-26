# imports
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Extra
score=0

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("😈 My Snake Game 🎮")
screen.tracer(0)


# Scoreboard setup
scoreboard = Scoreboard()


# Snake setup
snake = Snake()


# Food setup
food = Food()

# Game setup
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




# functions


def start():
    screen.update()
    game_is_on = True
    while game_is_on == True:
        screen.update()
        time.sleep(0.1)
        snake.move(snake.snakes_body)

        #detect collision with food
        if snake.head.distance(food) < 15:
            snake.grow()
            food.refresh()
            scoreboard.increase_score()
        #direct collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:

            snake.reset()
            scoreboard.reset_score()

        #dietect collision with itself

        if snake.collision()==True:
            screen.clear()
            snake.reset()
            scoreboard.reset_score()











# Main game

start()

screen.exitonclick()
