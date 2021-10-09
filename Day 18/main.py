from turtle import Turtle, Screen

# import heroes
tim = Turtle()

# print(heroes.gen())

tim.shape("turtle")
tim.color("deep sky blue")


# for i in range(4):
#     tim.forward(100)
#     tim.left(90)

def dashes(name, num_dashes, dash_length):
    """Create a dashed line with turtle"""
    for i in range(num_dashes):
        name.pendown()
        name.forward(dash_length)
        name.penup()
        name.forward(dash_length)


dashes(tim, 50, 10)

tim.pendown()
screen = Screen()
screen.exitonclick()
