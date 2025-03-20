from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
ROUND = 1
timer_mec = None
mark = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global ROUND, timer_mec, mark
    ROUND = 1
    if timer_mec is not None:  # Safe cancellation
        window.after_cancel(timer_mec)
        timer_mec = None
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    tick_label.config(text="")
    start_button.config(state=NORMAL)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global ROUND
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if ROUND == 8:
        label.config(text="LONG BREAK")
        timer = long_break_sec
    elif ROUND % 2 == 1:
        label.config(text="WORK HARD")
        timer = work_sec
    else:
        label.config(text="SHORT BREAK")
        timer = short_break_sec

    start_button.config(state=DISABLED)
    count_down(timer)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = count // 60
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    total_time = f"{min}:{sec}"
    canvas.itemconfig(timer_text, text=total_time)
    if count > 0:
        global timer_mec
        timer_mec = window.after(1000, count_down, count - 1)
    else:
        global ROUND, mark
        if ROUND % 2 == 1 and ROUND < 8:  # After work sessions (1, 3, 5, 7)
            mark += "#"
            tick_label.config(text=mark)
        if ROUND == 8:  # After long break, reset
            reset_timer()
        else:
            ROUND += 1
            start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)

# Canvas
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

# Labels
label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=PINK, fg=GREEN)
label.grid(column=1, row=0)

# Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Tick Label
tick_label = Label(text=mark, font=(FONT_NAME, 15, "bold"), bg=PINK, fg=GREEN)
tick_label.grid(column=1, row=3)

window.mainloop()