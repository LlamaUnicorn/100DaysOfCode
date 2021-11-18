import tkinter

window = tkinter.Tk()
window.title('My First GUI Program')
# Minimum window size
window.minsize(width=500, height=300)

# Label
my_lable = tkinter.Label(text='I Am a Label', font=('Arial', 24, 'bold'))
# Placing the component onto the center of the screen
my_lable.pack() # my_lable.pack(side='left') #(expand=True)

# Unlimited Arguments






# Always at the end of the program
window.mainloop()

