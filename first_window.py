from tkinter import *
from app import app 

def next_window():
    app = Tk()
    first_window.destroy()

first_window = Tk()
Button(first_window,text='next',command=next_window).pack()

first_window.mainloop()