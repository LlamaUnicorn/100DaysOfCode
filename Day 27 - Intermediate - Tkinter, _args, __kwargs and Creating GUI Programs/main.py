# We're gonna import lots of classes here
# import tkinter
from tkinter import *

window = Tk()
window.title('My First GUI Program')
# Minimum window size
window.minsize(width=500, height=300)
# Padding (space on the edges of the window)
window.config(padx=20, pady=20)
# Label
my_lable = Label(text='I Am a Label', font=('Arial', 24, 'bold'))
# Padding around an element
my_lable.config(padx=20, pady=20)
# Placing the component onto the center of the screen
# using my_label.pack(side='center')
# my_lable.pack(side='center') #(expand=True)

# my_lable.place to place an object at specific place
# my_lable.place(x=0, y=0)

# placing using grid()
my_lable.grid(column=0, row=0)
# Changing the properties
my_lable['text'] = 'Label'
# another way to do that
my_lable.config(text='Label')

# Event listener for the button


def button_clicked():
    print("I got clicked")
    new_text = user_input.get()
    my_lable.config(text=new_text)


# Button
button = Button(text='Button', command=button_clicked)
button.grid(column=1, row=1)

# Button
new_button = Button(text='New Button', command=button_clicked)
new_button.grid(column=2, row=0)

# Entry (input)
user_input = Entry()
user_input.grid(column=3, row=2)

# Always at the end of the program
window.mainloop()

