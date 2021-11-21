from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

is_equal_to = Label(text='is equal to')
is_equal_to.grid(column=0, row=1)

converted_value = 0
converted_value = Label(text=converted_value)
converted_value.grid(column=1, row=1)
converted_value.config(padx=20, pady=20)

miles_lable = Label(text='Miles')
miles_lable.grid(column=2, row=0)
miles_lable.config(padx=20)

km_lable = Label(text='Km')
km_lable.grid(column=2, row=1)

user_input = Entry(width=8)
user_input.grid(column=1, row=0)


def button_clicked():
    user_value = float(user_input.get())
    new_value = round(user_value * 1.60934, 2)
    converted_value.config(text=new_value)


calculate_button = Button(text='Calculate', command=button_clicked)
calculate_button.grid(column=1, row=2)

window.mainloop()
