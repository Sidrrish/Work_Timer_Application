from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
ORANGE = "#FF8F00"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text, text="00:00")
    timer_text.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_text.config(text="20 Mins Break Bro", fg=ORANGE)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_text.config(text="5 Mins Short Break, Rest Up Bro", fg=GREEN)

    else:
        count_down(work_sec)
        timer_text.config(text="Its time to Work Bro", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=224, height=200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 88, image=tomato_img)
text = canvas.create_text(103, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


timer_text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_text.grid(column=2, row=1)

start_button = Button(text="Start", fg=YELLOW, bg=ORANGE, font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="RESET", fg=YELLOW, bg=ORANGE, font=(FONT_NAME, 15, "bold"), command=reset_timer)
reset_button.grid(column=3, row=3)

check_marks = Label()
check_marks.grid(column=2, row=3)


window.mainloop()
