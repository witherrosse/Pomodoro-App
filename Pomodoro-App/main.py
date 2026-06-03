from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25          # Work session duration in minutes
SHORT_BREAK_MIN = 5    # Short break duration in minutes
LONG_BREAK_MIN = 20    # Long break duration in minutes
reps = 0               # Track number of sessions completed
timers = None          # Store timer ID for cancellation

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():

    ### Stop the running timer ###

    window.after_cancel(timers)

    ### Reset UI elements to default state ###

    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    canvas.itemconfig(timer, text="00:00")

    ### Reset session counter ###

    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():

    ### Increase session count ###

    global reps
    reps += 1

    ### Convert minutes to seconds ###

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    ### Decide which session to run based on rep count ###

    if reps % 8 == 0:          # Every 8th session = long break

        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)

    elif reps % 4 == 0:        # Every 4th session = short break

        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

    else:                      # Work session

        count_down(work_sec)
        timer_label.config(text="Work", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    ### Convert seconds to minutes and seconds format ###

    count_min = math.floor(count / 60)
    count_sec = count % 60

    ### Show "00" instead of "0" for seconds ###

    if count_sec == 0:
        count_sec = "00"

    ### Update the timer display ###

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")

    if count > 0:

        global timers

        ### Call this function again after 1 second ###

        timers = window.after(1000, count_down, count - 1)

    else:

        ### Timer finished - start next session ###

        start_timer()

        ### Add checkmark for completed work session ###

        marks = ""

        work_session = math.floor(reps / 2)   # Each work session takes 2 reps (work + break)

        for i in range(work_session):

            marks += "✔"

        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

### Tomato image as canvas background ###

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=2, column=1)

### Timer text inside the tomato image ###

timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))

### Labels and buttons ###

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer_label.grid(row=1, column=1)

check_label = Label(font=(FONT_NAME, 16, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
check_label.grid(row=4, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=3, column=2)

window.mainloop()