from tkinter import *
from tkinter.ttk import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
# noinspection SpellCheckingInspection
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

SECONDS = 1000

# ---------------- True Values. Uncomment for true functionality
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------- Testing Values. Comment out for true functionality
# WORK_MIN = 1
# SHORT_BREAK_MIN = 0.3
# LONG_BREAK_MIN = 0.5
# -----------------------------------------
reps = 0
timer = ""


def reset_timer():
    """Reset the program to its default state."""
    global timer_label, reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label["text"] = ""

    # Activate Start Button
    start_button.state(["!disabled"])


def start_timer():
    """Start the program."""
    global reps
    reps += 1

    # Disable the Start Button
    start_button.state(["disabled"])
    
    # Enable the Reset Button
    reset_button.state(["!disabled"])

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    window.attributes('-topmost', 1)
    if reps % 8 == 0:
        timer_label.config(text="Break", foreground=RED)
        count_down(long_break_secs)
    elif reps % 2 == 0:
        timer_label.config(text="Break", foreground=PINK)
        count_down(short_break_secs)
    else:
        timer_label.config(text="Work", foreground=GREEN)
        count_down(work_secs)

    window.attributes('-topmost', 0)


def count_down(count):
    """Implement the timer count down functionality."""
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)

    if count_min < 10:
        count_min = "0" + str(count_min)

    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(SECONDS, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_label["text"] += "✔"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

check_label = Label(background=YELLOW, foreground=GREEN)
check_label.grid(row=3, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)
reset_button.state(["disabled"])

window.mainloop()
