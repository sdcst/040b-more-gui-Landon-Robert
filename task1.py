import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
window.geometry("400x100")

label1 = tk.Label(window, text="Principal")
label2 = tk.Label(window, text="Interest Rate")
label3 = tk.Label(window, text="Years")
label4 = tk.Label(window, text="Amount")
box1 = tk.Entry(window)
box2 = tk.Entry(window)
box3 = tk.Entry(window)
box4 = tk.Entry(window)
label1.grid(row = 1, column = 1)
label2.grid(row = 1, column = 2)
label3.grid(row = 1, column = 3)
label4.place(x=75,y=80)
box1.grid(row = 2, column = 1)
box2.grid(row = 2, column = 2)
box3.place(x=124,y=80)
box4.grid(row = 2, column = 3)


label4.place()

window.mainloop()