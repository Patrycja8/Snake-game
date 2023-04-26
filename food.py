from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.goto(random.randint(-280, 280),  random.randint(-280, 280))

    def refresh(self):
        self.goto(random.randint(-280, 280),  random.randint(-280, 280))