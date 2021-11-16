import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# Adding image as a shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct',
                                    prompt="What's another State? ")
    # Convert the guess to Title case
    answer_state = answer_state.title()
    # Original solution
    # if answer_state == 'Exit':
    #     missing_states = []
    #     for state in all_states:
    #         if state not in guessed_states:
    #             missing_states.append(state)
    #     new_data = pandas.DataFrame(missing_states)
    #     new_data.to_csv('final_csv')

    # Refactoring with comprehensions
    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('final_csv')

        break
    # Check if the guess is among the 50 states
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(answer_state)


# My googled solution to exporting csv to learn (with diffs):

# states_to_learn = set(all_states).difference(set(guessed_states))
# df = pandas.DataFrame(states_to_learn)
# print(df)
# df.to_csv('states_to_learn.csv')


# Write correct guesses onto the map
# Use a loop to allow the user to keep guessing
# Record correct guesses in a list
# Keep track of the score

# Getting the coordinates of mouse clicks
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
