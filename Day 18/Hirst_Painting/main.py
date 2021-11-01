# import colorgram
import turtle as t
import random
from turtle import Screen

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
# 10 by 10
# dot size 20
# 50 paces apart
# repeat 10 times:
#   move 1 row up:
#       10 times repeat:
#           Move 50 paces right
#           pick a color from color_list
#           print a dot

tim = t.Turtle()
tim.pu()
t.colormode(255)
t.speed('fastest')
tim.setpos(-300, -100)
tim.hideturtle()

def random_color():
    picked_color = random.choice(color_list)
    return picked_color


def draw_a_row():
    for rows in range(-100, 400, 50):
        tim.setpos(-300, rows)
        for row in range(10):
            # print(tim.pos())
            color_print = random_color()
            tim.color(color_print)
            tim.pd()
            tim.dot(20)
            tim.pu()
            tim.forward(50)


draw_a_row()

screen = Screen()
screen.exitonclick()
