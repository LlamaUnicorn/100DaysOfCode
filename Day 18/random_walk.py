from turtle import Turtle, Screen
import random

# import heroes
tim = Turtle()

# print(heroes.gen())
colors = ['red', 'green', 'yellow', 'orange', 'teal', 'cyan']
tim.color("deep sky blue")

# move in random direction
# random colors each move
# make thicker lines
# move faster



for shape_side_n in range(100):
    tim.width(5)
    tim.speed(10)
    tim.color(random.choice(colors))
    tim.right(random.randrange(0, 360, 90))
    tim.forward(10)

# for i in range(4):
#     tim.forward(100)
#     tim.left(90)

# for i in range(5):
#     tim.forward(100)
#     tim.left(72)


screen = Screen()
screen.exitonclick()
