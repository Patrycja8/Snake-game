from turtle import Turtle

SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    snakes_body = []

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in SNAKE_POSITION:
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.speed(1)
            snake.goto(position)
            self.segments.append(snake)

    def move(self, snakes_body):
        for num_segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[num_segment - 1].xcor()
            new_y = self.segments[num_segment - 1].ycor()
            self.segments[num_segment].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270 :
           self.head.setheading(90)


    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def grow(self):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.speed(1)
        posix= self.segments[-1].xcor()
        posiy= self.segments[-1].ycor()
        snake.goto(posix,posiy)
        self.segments.append(snake)

    def collision(self):
        lengh = len(self.segments)
        x = range(3,lengh )
        for y in x:
            segment = self.segments[y]
            if segment.distance(self.head) < 20:
                return True
        return False

    def reset(self):
        for segment in self.segments:
            segment.goto(10000, 0)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
