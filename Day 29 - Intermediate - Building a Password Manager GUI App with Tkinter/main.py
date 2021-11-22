from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_pass():
    pass


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50, )
window.title('Password Manager')

# Creating canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

Password_label = Label(text='Password:')
Password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=45)
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

# Buttons
generate_pass_button = Button(text="Generate Password", command=generate_pass)
generate_pass_button.grid(column=2, row=3)

add_pass_button = Button(text="Add", width=30, command=add_pass)
add_pass_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
