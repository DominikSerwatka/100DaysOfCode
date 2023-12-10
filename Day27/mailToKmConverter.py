from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize()
window.config(padx=40, pady=40)


def button_1_clicked():
    in_miles = float(user_input.get())
    x = 1.609
    output = round(in_miles*x, 1)
    label_2.config(text=output)


label_1 = Label(text="is equal to")
label_1.grid(column=0, row=1)
label_1.config(padx=10, pady=10)

label_2 = Label(text="0")
label_2.grid(column=1, row=1)

label_3 = Label(text="Miles")
label_3.grid(column=2, row=0)

label_4 = Label(text="Km")
label_4.grid(column=2, row=1)

button_1 = Button(text="Calculate", command=button_1_clicked)
button_1.grid(column=1, row=2)

user_input = Entry(width=10)
user_input.grid(column=1, row=0)

window.mainloop()
