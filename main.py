from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
head = snake.segments[0]
food = Food()

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

	# detect colision with food
	if head.distance(food) < 15:
		food.refresh()
		snake.extend()
		scoreboard.increase_score()

	# detect colision with tail
	for segment in snake.segments[1:]:
		if head.distance(segment) < 10:
			game_is_on = False
			scoreboard.game_over()

	# detect collision with screen border
	if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
		scoreboard.game_over()
		game_is_on = False


screen.exitonclick()
