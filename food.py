from turtle import Turtle, Screen
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 1)
        self.color("white")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-380, 380)
        self.goto(random_x, random_y)
