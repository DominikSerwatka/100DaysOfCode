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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    label_timer.config(text="Timer")
    label_checkmark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1

    if reps % 8 == 0:
        label_timer.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    else:
        label_timer.config(text="Work", fg=GREEN)
        count_down(WORK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    minute = int(count/60)
    second = count % 60
    if second <= 9:
        second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        number = int(reps/2)
        check_mark_text = ""
        for _ in range(number):
            check_mark_text += "✔️ "
        label_checkmark.config(text=check_mark_text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(117, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


label_timer = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

label_checkmark = Label(bg=YELLOW, fg=GREEN, pady=10, font=(20))
label_checkmark.grid(column=1, row=2)


button_start = Button(text="Start", fg=GREEN, font=(10), command=start_timer)
button_start.grid(column=0, row=2)

button_restart = Button(text="Reset", fg=GREEN, font=(10), command=reset_timer)
button_restart.grid(column=2, row=2)




window.mainloop()