import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# Pomodoro actions
def start():
    global REPS
    REPS += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        count_down(long_break_secs)
        title.config(text="Long Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_secs)
        title.config(text="Short Break", fg=PINK)
    else:
        count_down(work_secs)
        title.config(text="Working", fg=GREEN)


def count_down(count):
    global TIMER
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start()
        marks = ""
        work_session = math.floor(REPS / 2)
        for i in range(work_session):
            marks += "✅"
        check_mark.config(text=marks)


def reset():
    global REPS
    window.after_cancel(TIMER)
    title.config(text="Timer", bg=YELLOW)
    check_mark.config(text="", bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    REPS = 0


# User Interface
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

start_button = Button(text="Start", command=start, font=(FONT_NAME, 12, "normal"))
start_button.grid(column=0, row=2)
start_button.config(width=8)
reset_button = Button(text="Reset", command=reset, font=(FONT_NAME, 12, "normal"))
reset_button.config(width=8)
reset_button.grid(column=2, row=2)

check_mark = Label(text="", bg=YELLOW, font=(FONT_NAME, 10, "normal"))
check_mark.grid(column=1, row=3)

blank_space = Label(text="")

window.mainloop()
