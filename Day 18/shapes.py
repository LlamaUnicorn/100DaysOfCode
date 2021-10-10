from turtle import Turtle, Screen
import random

# import heroes
tim = Turtle()

# print(heroes.gen())
colors = ['red', 'green', 'yellow', 'orange', 'teal', 'cyan']
tim.shape("turtle")
tim.color("deep sky blue")

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.left(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

# for i in range(4):
#     tim.forward(100)
#     tim.left(90)

# for i in range(5):
#     tim.forward(100)
#     tim.left(72)


screen = Screen()
screen.exitonclick()
