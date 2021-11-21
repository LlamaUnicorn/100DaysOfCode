from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 4
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0
timer_str = "Timer"
timer = None
# checkmark = "✓"
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text=timer_str, fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    check_marks_label.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 1
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_sec = LONG_BREAK_MIN * 1
    # 8
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='Long Break', fg=RED)
    # 2/4/6
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Short Break', fg=PINK)
    # 1/3/5/7
    else:
        count_down(work_sec)
        timer_label.config(text='Work', fg=GREEN)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    # math.floor returns largest whole number lower than "count"
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    # Editing Canvas is different (not like Labels)
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✓"
        check_marks_label.config(text=marks)
        # My attempt
        # if reps % 2 == 0:
        #     number_of_check_marks = reps // 2
        #     check_marks_label.config(text=check_mark*number_of_check_marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title('Pomodoro')

# Creating canvas
canvas = Canvas(width=202, height=226, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(101, 113, image=tomato_img)
timer_text = canvas.create_text(101, 130, text="00:00", fill='white', font=(FONT_NAME, 35))
canvas.grid(column=1, row=1)

# Other Widgets
timer_label = Label(text=timer_str, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
timer_label.grid(column=1, row=0)

check_marks_label = Label(fg=GREEN, bg=YELLOW, font="bold")
check_marks_label.grid(column=1, row=3)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
