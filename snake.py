from turtle import Turtle

START_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

	def __init__(self):
		self.segments = []
		self.create_snake()

	def create_snake(self):
		for position in START_POSITIONS:
			self.add_segment(position)

	def add_segment(self, position):
		new_turtle = Turtle(shape="square")
		new_turtle.shapesize(stretch_wid=0.5, stretch_len=0.5)
		new_turtle.penup()
		new_turtle.color("white")
		new_turtle.goto(position)
		self.segments.append(new_turtle)

	def extend(self):
		self.add_segment(self.segments[-1].position())

	def move(self):
		for i in range(len(self.segments) - 1, 0, -1):
			x = self.segments[i - 1].xcor()
			y = self.segments[i - 1].ycor()
			self.segments[i].goto(x, y)
		self.segments[0].forward(MOVE_DISTANCE)

	def up(self):
		if self.segments[0].heading() != DOWN:
			self.segments[0].setheading(UP)

	def down(self):
		if self.segments[0].heading() != UP:
			self.segments[0].setheading(DOWN)

	def left(self):
		if self.segments[0].heading() != RIGHT:
			self.segments[0].setheading(LEFT)

	def right(self):
		if self.segments[0].heading() != LEFT:
			self.segments[0].setheading(RIGHT)
