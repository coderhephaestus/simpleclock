from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.resizable(False, False)
window.title("Clock")


def time():
    string = strftime("%H:%M:%S")
    label.config(text=string)
    label.after(1000, time)


label = Label(window, font=("Courier", 80), background="white", foreground="black")
label.pack(anchor="center")
time()

mainloop()
